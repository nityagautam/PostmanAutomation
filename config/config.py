# META:
# This contains the configuration for
#       - Collection files and test data
#       - Framework's core setup/configuration

# ======================================================================================
# [Execution configurations]
# ======================================================================================

# -------------------------------------------
# Collections to execute 
# [order will be retained during execution]
sanity_collections = [
    "sample_collection_file1.json",
    "sample_collection_file2.json",
    "sample_collection_file3.json"
]
regreession_collections = [

]

# Test data files
# -------------------------------------------
test_data_files = {}



# ======================================================================================
# [Framework's core configurations]
# CAUTION : DO NOT TOUCH ANYTHING BELOW THIS, 
#           IF U R NOT SURE OF UR ACTION.
# ======================================================================================

# Binaries mapping
# -------------------------------------------
os_binaries = {
    'nodejs': 'path_to_nodejs',
    'python3': 'path_to_python3',
    'newman' : 'path_to_newman_binary'
}
library_packages = {
    "npm": "npm",
    "newman" : "newman",
    "html_reporter": "",
    "html_extra_reporter": "",
}
npm_commands = {
    "install": "npm install {}",
    "update": "npm update {}",
    "audit": "npm audit --json",
    "audit_fix": "npm audit fix --force --dry-run --json",
    "update_npm": "npm install -g npm"
}
newman_commands = {
    "run" : "newman run {}",
    "run_with_env_vars" : "newman run {} -e {}",
}


# Framework configuration
# -------------------------------------------
framework_setup = {
    "unit_tests": True,
    "console_logs": True,
    "file_logs": True
}

# -------------------------------------------
# Collection configurations 
# {Avaialble mode : single | combined | mixed}
collections_setup = {
    "mode": 'single',
    "variables_locations": "PATH_TO_ENV_JSON_FOR_EACH",
    "data_files": 'bind_with_ENV'
}

# timeout in seconds
timeout = 30

# Error codes mapping
error_codes = {}

# =====================
# Problem statement: Lets say, each collection has the multiple api requests.
#      and each might need to send an attachement/test_data.
#
#      Now, there are two ways we can achieve this
#      1- Manage each individual collections per API
#        \-- This will make structure easy, and easy to configure
#      2- Bind the test-data using some environment variable
#        \-- This would be a bit complex (in order to config later)
