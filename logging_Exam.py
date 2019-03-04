import logging
from main1 import getCustomLogger
class LoggingDemo:
    def m1(self):
        logger = getCustomLogger(logging.DEBUG)
        logger.debug('m1:debug message')
        logger.info('m1:info message')
        logger.warning('m1:warning message')
        logger.critical('m1:critical message')
    def m2(self):
        logger = getCustomLogger(logging.DEBUG)
        logger.debug('m2:debug message')
        logger.info('m2:info message')
        logger.warning('m2:warning message')
        logger.critical('m2:critical message')
    def m3(self):
        logger = getCustomLogger(logging.DEBUG)
        logger.debug('m3:debug message')
        logger.info('m3:info message')
        logger.warning('m3:warning message')
        logger.critical('m3:critical message')
    def m4(self):
        logger = getCustomLogger(logging.DEBUG)
        logger.debug('m4:debug message')
        logger.info('m4:info message')
        logger.warning('m4:warning message')
        logger.critical('m4:critical message')

l=LoggingDemo()
l.m1()
l.m2()
l.m3()
l.m4()  
