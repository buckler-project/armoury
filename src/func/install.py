import os
import yaml

from ..utils import config as _config
from ..utils import url as _url



def install(url, config):
    os.system(f"cd {config.parent_path} && git clone {url}")

    name = _url.get_repo_name(url)
    with open(f"{config.parent_path}/{name}/{config.config_path}") as f:
        config = yaml.load(f)

    return config

def install_scanner(url):
    config = install(url, _config.scanner)
    # TODO

def install_signature(url):
    config = install(url, _config.signature)
    # TODO
