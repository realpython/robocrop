import envconfig

# Deployment specific settings
port = envconfig.int('PORT')
debug = envconfig.bool('DEBUG')
client_key = envconfig.str('CLIENT_KEY')

# Resizer behavior
mode = 'clip'

# Quality
filter = 'antialias'
optimize = True
progressive = True
quality = '90'
