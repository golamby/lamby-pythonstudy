import configparser


config =configparser.ConfigParser()
config.read('data/test.ini',encoding='utf-8')

print(config.sections())
print(config.options('default'))
print(config.items('db'))

print(config.get('db','db_type'))
delay = config.getint('default','delay')
compression = config.getboolean('default','compression')
print(delay,type(delay))
print(compression,type(compression))