# ======================================================================================
# META:
# Created: 15 July 2022
# Last modified: 18 July 2022
# Description: This contains the configuration for
#               - Framework's core setup/configuration
# CAUTION : DO NOT TOUCH ANYTHING BELOW THIS, 
#           IF U R NOT SURE OF UR ACTION.
# ======================================================================================

# Binaries mapping
# -------------------------------------------
os_binaries = {
    'PYTHON3': 'path_to_python3',
    'NODEJS': 'path_to_nodejs',
    'NEWMAN' : 'path_to_newman_binary'
}
library_packages = {
    "NPM": "npm",
    "NEWMAN" : "newman",
    "PLAIN_HTML_REPORTER": "",
    "FANCY_HTML_REPORTER": "",
}
npm_commands = {
    "INSTALL": "npm install {}",
    "UPDATE": "npm update {}",
    "AUDIT": "npm audit --json",
    "AUDIT_FIX": "npm audit fix --force --dry-run --json",
    "UPDATE_NPM": "npm install -g npm"
}
newman_commands = {
    "RUN" : "newman run ",
    "RUN_WITH_COLLECTION" : "newman run {}",
    "RUN_WITH_ENV_VARS" : "newman run {} -e {}",
}


# Framework configuration
# -------------------------------------------
framework_setup = {
    "RUN_UNIT_TESTS": True,
    "SHOW_CONSOLE_LOGS": True,
    "CREATE_FILE_LOGS": True
}

# Collection configurations 
# {Avaialble mode : single | combined | mixed}
# -------------------------------------------
collections_setup = {
    "mode": 'single',
    "variables_locations": "PATH_TO_ENV_JSON_FOR_EACH",
    "data_files": 'bind_with_ENV'
}

# timeout in seconds
# -------------------------------------------
LOG_LEVEL = "INFO"
TIMEOUT = 30
RETRY = 3

# Error codes mapping
# -------------------------------------------
error_codes = {
    404: "NOT_FOUND! \nThe following file has been not found on the system\nFile: {}",
    504: "NOT_INSTALLED! \nThe following program has not been installed on the system\nProgram: {}",
    500: "ERROR_DURING_CMD_EXECUTION! \nThe following error occured for the command: {}\nError: {}",
}

# =====================
# Problem statement: Lets say, each collection has the multiple api requests.
#      and each might need to send an attachement/test_data.
#
#      Now, there are two ways we can achieve this
#      1- Manage each individual collections per API
#        \-- This will make structure easy, and easy to configure
#      2- Bind the test-data using some environment variable
#        \-- This would be a bit complex (in order to config later)
