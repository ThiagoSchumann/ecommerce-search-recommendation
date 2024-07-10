import logging

class LoggerAdapter:
    def __init__(self) -> None:
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
    
    def info(self,message):
        self.logger.info(message)
        
    def error(self,message,*args,**kwargs):
        self.logger.error(message,*args,**kwargs)
