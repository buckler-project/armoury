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
        name = url.split('/')
        package = factory.generate(auther=name[0], name=name[1])

    os.system(f"mkdir {package.parent_path}/{package.auther}")
    os.system(f"cd {package.parent_path}/{package.auther} && git clone {package.url}")

    return package

def install_scanner(url):
    install(url, ScannerFactory)

def install_signature(url):
    install(url, SignatureFactory)