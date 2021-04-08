import envconfig

# Deployment specific settings
port = envconfig.int('PORT')
debug = envconfig.bool('DEBUG')
client_key = envconfig.str('CLIENT_KEY')
workers = envconfig.int('WEB_CONCURRENCY')
timeout = float(envconfig.int('TIMEOUT'))

# Resizer behavior
mode = 'clip'

# Quality
filter = 'antialias'
progressive = True
quality = 'keep'
