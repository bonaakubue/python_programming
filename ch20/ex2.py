# Creating and configuring the logger

import logging

#logging to a file
logging.basicConfig(filename='data.log', level=logging.DEBUG)
logging.warning('This is a warning message')
