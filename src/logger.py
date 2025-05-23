import logging
from datetime import datetime


class Logger():
    _logger = None
    
    @staticmethod
    def setup(name="pirv1", log_file=None, level=logging.INFO):
        # Loger has been set up
        if Logger._logger is not None:
            return
        
        # Default log file name based on date ex. 12-05-2025-priv1.log
        if log_file is None:
            log_file = datetime.now().strftime("%d-%m-%Y") + "-" + name + ".log"
        
        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.propagate = False
        
        if not logger.handlers:
            formatter = logging.Formatter(
                "[%(asctime)s] [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S"
            )
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

        Logger._logger = logger
    
    @staticmethod
    def info(msg):
        if Logger._logger:
            Logger._logger.info(msg)

    @staticmethod
    def warning(msg):
        if Logger._logger:
            Logger._logger.warning(msg)

    @staticmethod
    def error(msg):
        if Logger._logger:
            Logger._logger.error(msg)

    @staticmethod
    def debug(msg):
        if Logger._logger:
            Logger._logger.debug(msg)
        
    