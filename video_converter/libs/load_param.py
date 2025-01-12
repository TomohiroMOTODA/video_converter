import yaml

def load_yaml(path):
    with open(path, 'r') as yml:
        config = yaml.safe_load(yml)
    return config