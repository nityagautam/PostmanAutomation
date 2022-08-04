# ======================================================================================
# [Configurations]
# ======================================================================================
# META:
# Written: 22 July 2022
# Last modified:
# This contains the configuration for
#       - Postman API Collection files, environment file and test data
# Notes:
#   - Paths will be evaluated wrt relativity of the execution location (as cwd)
#   - means, path will be relative to the "runner.py" location
# ======================================================================================

# -------------------------------------------
# Environment configurations for collection
# -------------------------------------------
# C:\Users\nfaruqe\Desktop\Automation\PostmanAutomation\suites\Samples\BankingServices.postman_environment.variables.json
api_environment = {
    "default": "C:/Users/nfaruqe/Desktop/Automation/PostmanAutomation/suites/samples/BankingServices.postman_environment.variables.json",
    "test": "C:/Users/nfaruqe/Desktop/Automation/PostmanAutomation/suites/samples/BankingServices.postman_environment.variables.json",
    "debug": ""
}

# -------------------------------------------
# Test data files configuration
# -------------------------------------------
test_data_files = {
    "global_csv_test_data_for_tc1": "PATH_TO_DATA_FILE"
}

# -------------------------------------------
# file path configurations for suites
# -------------------------------------------
collections_suite_path = {
    "samples": "./suites/samples/",
    "sanity": "./suites/sanity/",
    "regression": "./suites/regression/"
}

# -------------------------------------------
# Collections file configuration
# -------------------------------------------
# Collections suite are being categorized as:
# 1- samples
# 2- sanity
# 3- regressions
# etc
# [order will be retained during execution]
api_collections = {
    "samples": [
        "SampleAPITest01.postman_collection.json"
        
    ],
    "sanity": [

    ],
    "regression": [

    ],
}