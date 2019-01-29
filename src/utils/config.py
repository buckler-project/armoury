import yaml

buckler_config = './buckler.yml'

class Dumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(Dumper, self).increase_indent(flow, False)

class Config:
    def __init__(self, name):
        self.name = name
    
    def load(self):
        with open(self.name, 'r') as f:
            self.dict = yaml.load(f)
        
        return self.dict

    def save(self):
        with open(self.name, 'w') as f:
            yaml.dump(
                self.dict, f,
                Dumper=Dumper,
                default_flow_style=False,
                indent=2
            )

    def add(self, key, value):
        self.load()
        self.dict[key].append(value)
        self.save()
    
    def delete(self, key, value):
        self.load()
        self.dict[key].remove(value)
        self.save()

config = Config(buckler_config)