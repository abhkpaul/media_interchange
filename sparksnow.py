import os
from sp_sf_converter.config import configs as cfg
from sp_sf_converter.lib import wrapper as wrp
from sp_sf_converter.lib import utils as utl

'''
Spark (Python) - Snowpark (Park) Automation Entry Point
input: Read Contents from path configured on yml. Tag used : feed.
'''
def main():
    # out = open('out.py', 'w')
    # out.write(conf.type+'\n')
    # out.write(conf.language+'\n')
    # out.write(conf.source+'\n')
    # out.write(conf.destination+'\n')
    # out.write(str(wrp.funcA()))
    # out.
    # out.close()
    input = utl.read(conf.feed)
    '''
    Write your code here
    '''
    utl.write(input, '\n', conf.out)
    utl.write(str(wrp.funcA()), '\n', conf.out)



if __name__ == '__main__' :
    basepath = os.getcwd()
    filename = os.path.splitext(os.path.basename(__file__))[0]
    format = 'yml'
    confpath = os.path.join(os.getcwd(), filename + '.' + format)
    confRaw = cfg.getConfig(confpath)
    conf = cfg.Config()
    conf.type = confRaw.get('type')
    conf.language = confRaw.get('language')
    conf.source = confRaw.get('source')
    conf.destination = confRaw.get('destination')
    conf.feed = confRaw.get('feed')
    conf.out = confRaw.get('out')
    main()
