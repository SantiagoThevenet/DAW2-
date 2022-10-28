import logging


logger = logging.getLogger('__name__')

# c_header = logging.StreamHandler()
c_header = logging.FileHandler('file.log')
c_format = logging.Formatter('%(name)s - %(asctime)s')

c_header.setLevel(logging.DEBUG)
c_header.setFormatter(c_format)

logger.addHandler(c_header)

logger.error('su')
