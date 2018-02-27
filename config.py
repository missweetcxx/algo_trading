import yaml
from os import path

ROOT_PATH = path.abspath(path.join(path.dirname(__file__)))
CONF_FILE = path.join(ROOT_PATH, 'common/conf.yaml')

with open(CONF_FILE, 'r') as f:
    CONFIG = yaml.load(f)
