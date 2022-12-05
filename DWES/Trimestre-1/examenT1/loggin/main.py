import logging

logger = logging.getLogger(__name__)

handlerC = logging.FileHandler('log.log')

format_C = logging.Formatter('%(asctime)s - %(name)s - %(message)s')

handlerC.setLevel(logging.WARNING)

handlerC.setFormatter(format_C)

logger.addHandler(handlerC)

logger.warning('This is a warning')

