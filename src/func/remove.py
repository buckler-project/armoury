import re
import yaml

from utils import setting as _setting
from utils import cmd as _cmd
from utils.config import config

from package.package import Package, PackageFactory
from package.scanner import Scanner, ScannerFactory
from package.signature import Signature, SignatureFactory


def remove(args):
    factory = PackageFactory()
    if re.match(r"^https?:\/\/", args.repository):
        package = factory.generate_from_url(args.repository)
    else:
        package = factory.generate_from_name(args.repository)

    name = package.get_name()
    scanners = config.load()['scanners']

    if name in scanners:
        factory = ScannerFactory()
        package = factory.generate_from_package(package)

        config.delete(
            'scanners',
            package.get_name()
        )

    signatures = config.load()['signatures']
    if name in signatures:
        factory = SignatureFactory()
        package = factory.generate_from_package(package)

        config.delete(
            'signatures',
            package.get_name()
        )

    cmd = f"rm -rf ./{package.get_path()}"
    _cmd.run_cmd(cmd)

    cmd = f"rm -r ./{package.parent_path}/{package.auther}"
    _cmd.run_cmd(cmd)

