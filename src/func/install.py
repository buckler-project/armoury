import os, re, urllib.request
import yaml

from utils import config as _config
from utils import path as _url

from package.scanner import Scanner, ScannerFactory
from package.signature import Signature, SignatureFactory


def install(url, _factory):
    factory = _factory()

    if re.match(r"^https?:\/\/", url):
        package = factory.generate_from_url(url)
    else:
        package = factory.generate_from_name(url)

    cmd = f"mkdir {package.parent_path}/{package.auther}"
    print(cmd)
    os.system(cmd)

    cmd = f"cd {package.parent_path}/{package.auther} && git clone {package.url}"
    print(cmd)
    os.system(cmd)

    path = package.get_config_path()        
    with open(path) as f:
        package.config = yaml.load(f)
    
    return package

def install_scanner(url):
    scanner = install(url, ScannerFactory)
    
    path = scanner.config['path'].split('/')
    path = '/'.join(path[:-1])
    path = f"{scanner.get_path()}/{path}"
    os.makedirs(path)

    print(f'download : {scanner.config["url"]}')

    urllib.request.urlretrieve(
        scanner.config['url'],
        f"{scanner.get_path()}/{scanner.config['path']}"
    )

def install_signature(url):
    signature = install(url, SignatureFactory)

