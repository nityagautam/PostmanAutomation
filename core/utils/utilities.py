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
from core.utils.logger import Logger

# Getting the logger
# ------------------------
log = Logger(__name__).get_logger()


# format a string to print the error/info msg
# --------------------------------------------------
def log_special_message(msg, typ: str = "info"):
    if typ.lower() == 'info':
        log.info("\n" + "=-" * 50 + f"\n{msg} \n" + "=-" * 50)
    elif typ.lower() == 'error':
        log.error("\n" + "=-" * 50 + f"\n{msg} \n" + "=-" * 50)
    elif typ.lower() == 'debug':
        log.debug("\n" + "=-" * 50 + f"\n{msg} \n" + "=-" * 50)
    elif typ.lower() == 'warning':
        log.warning("\n" + "=-" * 50 + f"\n{msg} \n" + "=-" * 50)
    else:
        log.info("\n" + "=-" * 50 + f"\n{msg} \n" + "=-" * 50)


# --------------------------------------------------
# Class to provide various utilities
# --------------------------------------------------
class Utilities:
    
    def __init__(self) -> None:
        pass
        
    def timer(self, function):
        def new_function(*argv, **d):
            start_time = time()
            data = function(*argv, **d)
            elapsed = time() - start_time
            log.debug(f"Function: {function} took {elapsed} seconds to complete")
            return data

    # Check the binaries
    def check_the_binaries(self):
        # Test the package
        log_special_message("Checking the installed binaries in the system")
        stdo, stde = Utilities().run_system_command("node --version")
        log.info(stdo)
        stdo, stde = Utilities().run_system_command("npm --version")
        log.info(stdo)
        # stdo, stde = Utilities().run_system_command("npm install newman --location=global")
        # log.info(stdo)
        stdo, stde = Utilities().run_system_command("c:/Users/nfaruqe/AppData/Roaming/npm/newman --version")
        # stdo, stde = Utilities().run_system_command("npm newman --version")
        log.info(stdo)

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
                    log.info("[STDOUT]>>> : output")
                    #log.info(tmp_stdout_str.encode("UTF-8"))
                
            # Collect the stderr from the process
            if process.stderr:
                for line in process.stderr:
                    tmp_stderr_str += line
                if log_cmd_out: 
                    log.error("[STDERR]>>> : output")
                    #log.error(tmp_stderr_str)
        
        # Return 
        return tmp_stdout_str, tmp_stderr_str

