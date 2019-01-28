import os

class Package:
    path = ''

    def __init__(self):
        pass

    def install(self, url):
        os.system(f"cd {self.path} && git clone {url}")

    def uninstall(self, package):
        os.system(f"cd {self.path} && rm -rf {package}")

