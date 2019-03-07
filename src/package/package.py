import os
from abc import *
import yaml

from utils import setting as _setting
from utils import cmd as _cmd

class Package:
    def __init__(self, url, name, auther):

        self.url = url
        self.name = name
        self.auther = auther

        self.parent_path = ''
        self.config_path = ''

    def get_name(self):
        return f'{self.auther}/{self.name}'

    def get_path(self):
        return f'{self.parent_path}/{self.auther}/{self.name}'

    def get_config_path(self):
        return f'{self.parent_path}/{self.auther}/{self.name}/{self.config_path}'

class PackageFactory:
    def __init__(self):
        self.parent_path = ''
        self.config_path = ''
    
    def generate(self, url, name, auther):
        package = self._generate(url=url, name=name, auther=auther)
        
        if not os.path.isdir(package.get_path()):
            return package

        path = package.get_config_path()        
        with open(path) as f:
            package.config = yaml.load(f)
        
        return package

    def generate_from_name(self, name):
        name = name.split('/')
        return self.generate_from_directory(auther=name[0], name=name[1])

    def generate_from_directory(self, auther, name):
        if os.path.isdir(f'{self.parent_path}/{auther}/{name}'):
            cmd = f'''cd {self.parent_path}/{auther}/{name}/ \\
                && git config --get remote.origin.url
                '''
            
            url = _cmd.run_cmd(cmd, subprocess=True, output=False)
        
        else:
            url = f'{_setting.url}{auther}/{name}'

        return self.generate(url=url, name=name, auther=auther)

    def generate_from_url(self, url):
        if url[-1] == '/':
            url = url[:-1]

        list = url.split('/')

        return self.generate(url=url, name=list[-1], auther=list[-2])

    def generate_from_package(self, package):
        return self.generate(url=package.url, name=package.name, auther=package.auther)

    def _generate(self, url, name, auther):
        #raise NotImplementedError()
        return Package(url=url, name=name, auther=auther)
        
