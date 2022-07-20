# ======================================================================================
# Logger Class
# META:
# Created: 18 July 2022
# Last modified: 21 July 2022
# Description: This contains the loggers for the framework
# CAUTION : DO NOT TOUCH ANYTHING BELOW THIS, 
#           IF U R NOT SURE OF UR ACTION.
# ======================================================================================

# Import section
# ----------------------------
import os, datetime, logging


# Class
# ----------------------------
class Logger:

    LOG_DIR = "logs/"
    LOG_FILE = LOG_DIR + "Log_" + datetime.datetime.now().strftime("%A_%d_%B_%Y_%I_%M_%p") + ".log"
    LOG_FORMATTER_STR = "%(asctime)s - %(name)s - %(levelname)s - %(message)s  "
    
    def __init__(self) -> None:
        # Create log dir, in case not not created
        folder = os.path.join(os.getcwd(), self.LOG_DIR)
        if not os.path.isdir(folder):
            os.mkdir(folder)

    def get_logger(self, logger_name):
        # Create a logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)
        
        # create formatter 
        formatter = logging.Formatter(self.LOG_FORMATTER_STR, datefmt='%Y-%m-%d %H:%M:%S')
        
        # create file handler, and add formatter
        fh = logging.FileHandler(self.LOG_FILE)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)

        # create console handler with a higher log level, and add formatter
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        
        # now, add the handlers to logger
        logger.addHandler(ch)
        logger.addHandler(fh)

        # Return
        return logger




"""
# Logger Class : Experimental code
# ---------------
class Logger:

    # Logging formatter
    # log_formatter_str = "%(asctime)s : %(name)s : %(levelname)s : %(message)s : %(filename)s : %(lineno)d :: "
    log_formatter_str = "%(asctime)s : %(name)s : %(levelname)s : %(message)s  "
    LOG_FORMATTER = logging.Formatter(log_formatter_str)
    LOG_DIR = "logs/"
    LOG_FILE_INTIAL = "Logs_"


    def __init__(self) -> None:
        # Create log dir, in case not not created
        folder = os.path.join(os.getcwd(), self.LOG_DIR)
        if not os.path.isdir(folder):
            os.mkdir(folder)

    def get_stdout_stream(self):
        stdout_stream = logging.StreamHandler(sys.stdout)
        stdout_stream.setFormatter(self.LOG_FORMATTER)
        return stdout_stream

    def get_stderr_stream(self):
        stderr_stream = logging.StreamHandler(sys.stderr)
        stderr_stream.setFormatter(self.LOG_FORMATTER)
        return stderr_stream

    def get_logfile_handler(self):
        file_handler = TimedRotatingFileHandler(self.LOG_DIR+self.LOG_FILE_INTIAL + datetime.datetime.now().strftime("%A_%d_%B_%Y_%I_%M_%p") + ".log", when="D")
        file_handler.setFormatter(self.LOG_FORMATTER)
        return file_handler
    
    def get_console_handler(self):
        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        # add formatter to ch
        ch.setFormatter(self.LOG_FORMATTER)
        # Return the console handler now
        return ch

    def get_file_handler(self):
        pass


    def get_logger(self, logger_name):
        logger = logging.getLogger(logger_name)
        try:
            logger.setLevel(logging.INFO)
            # Adding std stream
            logger.addHandler(self.get_console_handler())
            # Adding the file handler now    
            #logger.addHandler(self.get_logfile_handler())
        except:
            print("Error during getting the logger.")

        # Return the logger now
        return logger

    # Usage
    # log = Logger.get_logger(__name__)
    # log.info("")
    # 

"""
