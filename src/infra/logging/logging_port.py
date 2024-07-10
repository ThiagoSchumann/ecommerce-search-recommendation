from .logger.logger_adapter import LoggerAdapter


class LoggingPort:
    def __init__(self,adapter):
        self.adapter = adapter
    
    def info(self,message):
        self.adapter.info(message)
    
    def error(self,message,*args,**kwargs):
        self.adapter.error(message,*args,**kwargs)


logger = LoggingPort(LoggerAdapter())