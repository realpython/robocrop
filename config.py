import envconfig

# Deployment specific settings
port = envconfig.int('PORT')
debug = envconfig.bool('DEBUG')

# Resizer behavior
mode = 'clip'

# Quality
filter = 'antialias'
optimize = True
progressive = True
quality = '90'
