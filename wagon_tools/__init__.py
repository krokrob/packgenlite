from os.path import abspath
from os.path import dirname

with open('{}/version.txt'.format(dirname(__file__))) as version_file:
    __version__ = version_file.read().strip()
