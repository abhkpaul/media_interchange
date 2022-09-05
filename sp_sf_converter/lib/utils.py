'''
Write to data path
Params: _out : data | term : terminator | path : filename with path
'''
def write(_out, term='', path=''):
    if not path or not term:
        raise ValueError("term/path missing")
    else:
        file = open(path, 'a')
        file.write(_out + term)

'''
Read from data path
Params: _in : filename with path
'''
def read(_in):
    if not _in:
        raise ValueError("_in missing")
    else:
        file = open(_in, "r")
        file = file.read()
        return file
