import logging
import logging.handlers


class CustomLogger:
    def __init__(self,logging_dir,logging_level=logging.DEBUG):
        self.logging_dir = logging_dir
        self.arch_logger = logging.getLogger('ArchLogger')
        self.arch_logger.setLevel(logging_level)
        self.arch_logger.addHandler(logging.handlers.SysLogHandler(address=logging_dir))
    
    def debug_log(self, data):
        self.arch_logger.debug(data)
    
    def error_log(self,data):
        self.arch_logger.error(data)
    
    def critical_log(self,data):
        self.arch_logger.critical(data)

