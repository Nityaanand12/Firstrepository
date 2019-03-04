import logging
import inspect
def getCustomLogger(level):
    logname = inspect.stack()[1][3]
    logger = logging.getLogger(logname)
    logger.setLevel(level)
    fileHandler = logging.FileHandler('{}'.format(logname),'a')
    fileHandler.setLevel(level)
    formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s: %(message)s')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    return logger
