# ======================================================================================
# META:
# Created: 15 July 2022
# Last modified: 27 July 2022
# Description: This contains the configuration for
#               - Framework's core setup/configuration
# CAUTION : DO NOT TOUCH ANYTHING BELOW THIS, 
#           IF U R NOT SURE OF UR ACTION.
# ======================================================================================

# Binaries mapping
# -------------------------------------------
os_binaries = {
    'PYTHON3': 'python3',
    'NODEJS': 'node'
}
library_packages = {
    "NPM": "npm",
    "NEWMAN": "newman",
    "PLAIN_HTML_REPORTER": "newman-reporter-html",
    "FANCY_HTML_REPORTER": "newman-reporter-htmlextra",
}
npm_commands = {
    "INSTALL": "npm install {}",
    "INSTALL_GLOBAL": "npm install -g {}",
    "UPDATE": "npm update {}",
    "AUDIT": "npm audit --json",
    "AUDIT_FIX": "npm audit fix --force --dry-run --json",
    "UPDATE_NPM": "npm install -g npm"
}
newman_commands = {
    "RUN": "newman run ",
    "RUN_WITH_COLLECTION": "newman run {collection_files}",
    "RUN_WITH_ENV_VARS": "newman run {collection_files} -e {env_file_name}",
    "RUN_WITH_ENV_VARS_WITH_REPORT": "newman run {collection_files} -e {environment_file} -r {report_options}",
    "RUN_WITH_ENV_VARS_AND_PRODUCE_REPORTS": "newman run {collection_files} -e {env_file_name} -r htmlextra,cli --reporter-htmlextra-export {report_file_path}"
}

newman_reports = {
    "REPORT_TYPE_CLI": "cli",
    "REPORT_TYPE_JUNIT": "junit --reporter-junit-export {report_file_path}",
    "REPORT_TYPE_HTML": "html --reporter-html-export {report_file_path}",
    "REPORT_TYPE_FANCY_HTML": "cli,htmlextra --reporter-htmlextra-export {report_file_path}",
    "REPORT_TYPE_MIXED": "cli,html,htmlextra,junit,json "
                         "--reporter-html-export {html_report_file_path} "
                         "--reporter-htmlextra-export {fancy_html_report_file_path} "
                         "--reporter-junit-export {junit_report_file_path} "
                         "--reporter-json-export {json_report_file_path}",

}


# Framework configuration
# -------------------------------------------
framework = {
    "RUN_WITHOUT_OPTIONS": True,
    "RUN_UNIT_TESTS": True,
    "SHOW_CONSOLE_LOGS": True,
    "CREATE_FILE_LOGS": True,

    "TEST_SUITES_TO_EXECUTE": ["samples"],
    "API_EXECUTION_ENVIRONMENT": "default",
    "TEST_REPORTER_OPT_TO_USE": "REPORT_TYPE_FANCY_HTML",

    "REPORT_FILE_PATH": "./reports/",
    "REPORT_FILE_NAME_HTML": "SuiteReport_{placeholder}.html",
    "REPORT_FILE_NAME_FANCY_HTML": "FancySuiteReport_{placeholder}.html",
    "REPORT_FILE_NAME_JUNIT": "SuiteReport_{placeholder}.xml",
    "REPORT_FILE_NAME_JSON": "SuiteReport_{placeholder}.json"
}

# Collection configurations 
# {Avaialble mode : single | combined | mixed}
# -------------------------------------------
collections_setup = {
    "mode": 'single'
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