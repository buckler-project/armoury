import subprocess
from package import package

parent_path = '.scanners'
config_path = 'scanner.yml'

class Scanner(package.Package):
    def __init__(self, url, name, auther):
        super().__init__(url, name, auther)

        self.parent_path = parent_path
        self.config_path = config_path

class ScannerFactory(package.PackageFactory):
    def __init__(self):
        self.parent_path = parent_path
        self.config_path = config_path

    def _generate(self, url, name, auther):
        return Scanner(url=url, name=name, auther=auther)
