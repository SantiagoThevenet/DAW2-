import logging

##1-Configuracion basica
# logging.basicConfig(level=logging.DEBUG)


##logging.debug('This will get logged')

##logging.debug('Mensaje debug')
##logging.info('Mensaje info')
##logging.warning('Mensaje warning')
##logging.error('Mensaje error')
##logging.critical('Mensaje critico')

##2-Volcamos salida a archivo

#logging.basicConfig(filename='app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')

##logging.warning('This will get logged to a file')
##logging.info('Mensaje info')
##logging.critical('Mensaje critico')
##
##logging.basicConfig(filename='app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')


##logging.critical('Mensaje critico')

##logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
##logging.warning('This is a Warning')

#logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
#logging.info('Admin logged in')

##logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
##logging.info('Admin logged in')

# name = 'John'
# ##logging.error('%s raised an error', name)

# logging.error('{} raised an error'.format(name))


# Excepcion

# a = 5
# b = 0
# try:
#     c = a / b
# except Exception as e:
#     logging.error("Exception occurred", exc_info=True)

##a = 5
##b = 0
##try:
##
##    
##    c = a / b
##    
##except Exception as e:
##    logging.exception("Exception occurred")




#logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s')

# logger = logging.getLogger('example_logger')
# logger.warning('This is a warning')
