import os, re, urllib.request
import yaml

from utils import config as _config
from utils import path as _url

from package.scanner import Scanner, ScannerFactory


def install(url, config):
    os.system(f"cd {config.parent_path} && git clone {url}")

    name = _url.get_repo_name(url)


    return config

def _install(package):
    os.system(f"mkdir {package.parent_path}/{package.auther}")
    os.system(f"cd {package.parent_path}/{package.auther} && git clone {package.url}")

def install_scanner(name):
    if re.match(r"^https?:\/\/", name):
        url = name
    else:
        url = f"{_config.url}{name}"

    factory = ScannerFactory()
    scanner = factory.generate_from_url(url)

    _install(scanner)

def install_signature(url):
    config = install(url, _config.signature)
    print(config["scanner"])
    # TODO
