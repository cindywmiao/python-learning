import logging
from logging.config import fileConfig

# load my module
import my_module

# load the logging configuration
fileConfig('logging.ini')

my_module.foo()
bar = my_module.Bar()
bar.bar()