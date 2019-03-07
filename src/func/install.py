import os, sys, re, urllib.request
from abc import *

import yaml


from utils import setting as _setting
from utils import cmd as _cmd
from utils.config import config
from utils import setting as _config

from package.package import Package, PackageFactory
from package.scanner import Scanner, ScannerFactory
from package.signature import Signature, SignatureFactory



def install(args):
    factory = PackageFactory()

    if re.match(r'^https?:\/\/', args.repository):
        package = factory.generate_from_url(args.repository)
    else:
        package = factory.generate_from_name(args.repository)

    # clone repository
    has_faild = os.system(f'git clone {package.url} {package.name}')
    if has_faild:
        print("[err] Error occues around clone.")
        sys.exit(1)

    # check config file
    if os.path.isfile(f'{package.name}/signature.yml'):
        factory = SignatureFactory()
        opt_func = signature_opt
    elif os.path.isfile(f'{package.name}/scanner.yml'):
        factory = ScannerFactory()
        opt_func = scanner_opt
    else:
        print('[err] config file not found.')
        sys.exit(1)

    package = factory.generate_from_package(package)

    # move folder
    cmd = f'mkdir {package.parent_path}/{package.auther}'
    _cmd.run_cmd(cmd)

    has_failed = os.rename(f'{package.name}', f'{factory.parent_path}/{package.auther}/{package.name}')
    if has_failed:
        print("[err] Error occues around clone.")
        sys.exit(1)

    path = package.get_config_path()
    with open(path) as f:
        package.config = yaml.load(f)

    has_failed = opt_func(package)
    if has_faild:
        print('Abroad')
        return None

    return package

def scanner_opt(scanner):
    path = scanner.config['path'].split('/')
    path = '/'.join(path[:-1])
    path = f'{scanner.get_path()}/{path}'
    os.makedirs(path)

    print(f'download : {scanner.config["url"]}')

    urllib.request.urlretrieve(
        scanner.config['url'],
        f'{scanner.get_path()}/{scanner.config["path"]}'
    )

    config.add(
        'scanners',
        scanner.get_name()
    )

    return False

def signature_opt(signature):
    class Args:
        def __init__(self, repo):
            self.repository = repo

    scanners = config.load()['scanners']
    if signature.config['scanner'] in scanners:
        config.add(
            'signatures',
            signature.get_name()
        )
    else:
        print('not found scanner')
        scanner = signature.config['scanner']
        check = input(f'install {scanner}? [y/n] : ')

        if check == 'y':
            args = Args(scanner)
            install(args)

            config.add(
                'signatures',
                signature.get_name()
            )
            return False
        else:
            pass
   
    return True
