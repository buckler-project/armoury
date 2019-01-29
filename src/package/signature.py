from package import package

parent_path = '.signatures'
config_path = 'signature.yml'

class Signature(package.Package):
    def __init__(self, url, name, auther):
        super().__init__(url, name, auther)

        self.parent_path = parent_path
        self.config_path = config_path

class SignatureFactory(package.PackageFactory):
    def __init__(self):
        self.parent_path = parent_path
        self.config_path = config_path

    def _generate(self, url, name, auther):
        return Signature(url=url, name=name, auther=auther)
