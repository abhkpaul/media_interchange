import yaml
from yaml.loader import SafeLoader
'''
Getter/Setter Properties
'''
class Config:
    def __init__(self):
        self._type = None
        self._language = None
        self._source = None
        self._destination = None
        self._feed = None
        self._out = None

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        if len(value) != 0:
            self._type = value
        else:
            raise ValueError("Mandatory Configuration")


    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        if len(value) != 0:
            self._language = value
        else:
            raise ValueError("Mandatory Configuration")

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        if len(value) != 0:
            self._source = value
        else:
            raise ValueError("Mandatory Configuration")

    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, value):
        if len(value) != 0:
            self._destination = value
        else:
            raise ValueError("Mandatory Configuration")

    @property
    def feed(self):
        return self._feed

    @feed.setter
    def feed(self, value):
        if len(value) != 0:
            self._feed = value
        else:
            raise ValueError("Mandatory Configuration")

    @property
    def out(self):
        return self._out

    @out.setter
    def out(self, value):
        if len(value) != 0:
            self._out = value
        else:
            raise ValueError("Mandatory Configuration")

'''
Get Config body
'''
def getConfig(confpath=''):
    if (confpath != ''):
        with open(confpath) as f:
            data = yaml.load(f, Loader=SafeLoader)
            return data
    else:
        raise ValueError('Config Missing !!')



