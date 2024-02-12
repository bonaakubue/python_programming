# Formatting your messages

import logging

#logging with timestamps
logging.basicConfig(format='%(asctime)s %(message)s', filename='data.log', level=logging.DEBUG)
logging.info('Logged a message.')

#logging with severity level
logging.basicConfig(format='%(levelname)s:%(message)s', filename='data.log', level=logging.DEBUG)
logging.critical('This is critical.')

#logging with custom message
logging.basicConfig(format='%(message)s:%(message)s', filename='data.log', level=logging.DEBUG)
logging.warning('This is a Warning!')
