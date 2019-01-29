import subprocess
from abc import *


class Package:
    def __init__(self, url, name, auther):

        self.url = url
        self.name = name
        self.auther = auther

        self.parent_path = ''
        self.config_path = ''

    def get_path(self):
        return f'{self.parent_path}/{self.auther}/{self.name}'

    def get_config_path(self):
        return f'{self.parent_path}/{self.auther}/{self.name}/{self.config_path}'

class PackageFactory(metaclass=ABCMeta):
    def __init__(self):
        self.parent_path = ''
        self.config_path = ''

    def generate(self, name, auther):
        cmd = f'''cd {self.parent_path}/{auther}/{name}/ \\
            && git config --get remote.origin.url
            '''
        url = subprocess.getoutput(cmd)

        return self._generate(url=url, name=name, auther=auther)

    def generate_from_url(self, url):
        if url[-1] == '/':
            url = url[:-1]

        list = url.split('/')

        return self._generate(url=url, name=list[-1], auther=list[-2])

    @abstractmethod
    def _generate(self, url, name, auther):
        raise NotImplementedError()
