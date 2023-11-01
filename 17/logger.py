import logging

class Logger:
    '''A logger. It logs stuff.'''

    def __init__(self):
        self.logger = logging.getLogger("Logger")
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.DEBUG)

    def log_something(self, msg):
        self.logger.debug(msg)

if __name__ == "__main__":
    logger = Logger()
    logger.log_something("Just logging something.")
