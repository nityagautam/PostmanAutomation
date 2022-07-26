# ======================================================================================
# META:
# Created: 15 July 2022
# Last modified: 18 July 2022
# Description: This contains the utility functions for the framework
# CAUTION : DO NOT TOUCH ANYTHING BELOW THIS, 
#           IF U R NOT SURE OF UR ACTION.
# ======================================================================================

# Imports 
# ---------
from time import time
from subprocess import Popen, PIPE
from core.logger import Logger

# Getting the logger
# ------------------------
log = Logger().get_logger(__name__)


# --------------------------------------------------
# Class to proivde various utilities
# --------------------------------------------------
class Utilities():
    
    def __init__(self) -> None:
        pass
        
    def timer(self, function):
        def new_function(*argv, **d):
            start_time = time()
            data = function(*argv, **d)
            elapsed = time() - start_time
            log.debug(f"Function: {function} took {elapsed} seconds to complete")
            return data

    # Run command
    def run_system_command(self, *argv, log_cmd=True, log_cmd_out=True, errfile=False):
        tmp_stdout_str = ""
        tmp_stderr_str = ""
        cmd = " ".join(str(x) for x in argv)

        # if logging of command is set to true
        if log_cmd:
            log.debug(f"Executing Command ==> {cmd}")

        # Execute the command now
        with Popen(cmd, shell=True, stdout=PIPE, bufsize=1, universal_newlines=True, encoding="UTF-8", errors="ignore") as process:
            # Collect the stdout from the process
            if process.stdout:
                for line in process.stdout:
                    tmp_stdout_str += line
                if log_cmd_out: 
                    log.info("STDOUT: output")
                    log.info(tmp_stdout_str.encode("UTF-8"))
                
            # Collect the stderr from the process
            if process.stderr:
                for line in process.stderr:
                    tmp_stderr_str += line
                if log_cmd_out: 
                    log.error("STDERR: output")
                    log.error(tmp_stderr_str)
        
        # Return 
        return tmp_stdout_str, tmp_stderr_str

