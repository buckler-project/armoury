import os, re, subprocess
import yaml

from utils import config as _config

from package.scanner import Scanner, ScannerFactory
from package.signature import Signature, SignatureFactory


def uninstall(url, _factory):
    factory = _factory()

    if re.match(r"^https?:\/\/", url):
        package = factory.generate_from_url(url)
    else:
        package = factory.generate_from_name(url)
    
    cmd = f"rm -rf {package.get_path()}"
    print(cmd)
    os.system(cmd)

    cmd = f"rm -r {package.parent_path}/{package.auther}"
    print(cmd)
    subprocess.getoutput(cmd)

def uninstall_scanner(url):
    uninstall(url, ScannerFactory)
    # TODO

def uninstall_signature(url):
    uninstall(url, SignatureFactory)
    # TODO
