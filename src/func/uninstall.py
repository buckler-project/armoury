import os, re
import yaml

from utils import config as _config

from package.scanner import Scanner, ScannerFactory
from package.signature import Signature, SignatureFactory


def uninstall(url, _factory):
    factory = _factory()

    if re.match(r"^https?:\/\/", url):
        package = factory.generate_from_url(url)
    else:
        name = url.split('/')
        package = factory.generate(auther=name[0], name=name[1])
    
    cmd = f"rm -rf {package.get_path()}"
    print(cmd)

    os.system(cmd)

def uninstall_scanner(url):
    uninstall(url, ScannerFactory)
    # TODO

def uninstall_signature(url):
    uninstall(url, SignatureFactory)
    # TODO
