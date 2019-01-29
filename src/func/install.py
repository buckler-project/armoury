import os
import yaml

from utils import config as _config


def install(name, config):
    os.system(f"cd {config.parent_path} && git clone {_config.url}/{name}")

    name = name.split('/')[-1]
    with open(f"{config.parent_path}/{name}/{config.config_path}") as f:
        config = yaml.load(f)

    return config

def install_scanner(name):
    config = install(name, _config.scanner)
    # TODO

def install_signature(name):
    config = install(name, _config.signature)
    # TODO
