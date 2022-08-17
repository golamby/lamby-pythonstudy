import logging

'''
    critical--50
    error--40
    warning--30
    info--20
    debug--10
    '''
logging.basicConfig(
    # filename='./data/mylogging.log',
    format='%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',

    level=10,
    encoding='utf-8'

)
logging.warning('warn11\n')
logging.error('hhhh')
