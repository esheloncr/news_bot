import os
import logging


class Environ:
    """
    Class with environment variables.
    Should be defined .env file with variables like KEY=value
    """
    def __init__(self):
        self.file_name = '.env'

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def read_env(self):
        """
        Method which reads .env file and set up variables as object attribute.
        """
        assert self.file_name in os.listdir(), 'Should be define .env file'
        with open(self.file_name, 'r') as f:
            variables = f.readlines()
            for variable in variables:
                variable_name, value = variable.replace('\n', '').split('=')
                setattr(self, variable_name, value)


class Logger:
    """
    Logger class based on python logging module
    """

    def __init__(self, logger_name: str):
        self.logger = logging.getLogger(logger_name)
        self.error_counter = 0
        self._setup()

    def add(self, msg: str):
        """
        Append in log file a row with information from formatter
        :param msg: String with text information
        :return: None
        """
        self.logger.info(msg)

    def add_error(self, msg: str):
        """
        Append an error in log file and increase error counter
        :param msg: error traceback
        :return: None
        """
        self.error_counter += 1
        self.logger.error(str(msg))

    def _setup(self):
        logger = self.logger
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        self.logger = logger
