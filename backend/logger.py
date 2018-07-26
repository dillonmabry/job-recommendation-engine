import os
import logging 
import config

class Logger(object):

    def __init__(self, name):
        name = name.replace('.log','')
        logger = logging.getLogger('log_namespace.%s' % name)
        logger.setLevel(logging.DEBUG)
        if not logger.handlers:
            if not os.path.isdir(config.LOGGING_DIR):
                os.mkdir('log')
            file_name = os.path.join(config.LOGGING_DIR, '%s.log' % name)   
            handler = logging.FileHandler(file_name)
            formatter = logging.Formatter('%(asctime)s %(levelname)s:%(name)s %(message)s')
            handler.setFormatter(formatter)
            handler.setLevel(logging.DEBUG)
            logger.addHandler(handler)
        self._logger = logger

    def get(self):
        return self._logger
