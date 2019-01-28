import os
import yaml

from utils import config as _config


def uninstall(name, config):
    os.system(f"cd {config.parent_path} && rm -rf {name}")

def uninstall_scanner(name):
    with open(f"{_config.scanner.parent_path}/{name}/{_config.scanner.config_path}") as f:
        config = yaml.load(f)

    uninstall(name, _config.scanner)
    # TODO

def uninstall_signature(name):
    with open(f"{_config.signature.parent_path}/{name}/{_config.signature.config_path}") as f:
        config = yaml.load(f)

    uninstall(name, _config.signature)
    # TODO
