# META:
# This contains the configuration for
#       - Postman API Collection files and test data

# ======================================================================================
# [Collection configurations]
# ======================================================================================

# -------------------------------------------
# Collections to execute 
# [order will be retained during execution]
sanity_collections = [
    "./_dump/Sample API Test01.postman_collection.json",
    "./_dump/ForAutomationMock.postman_collection.json",
    "sample_collection_file3.json"
]
regreession_collections = [

]
envvironment_collection = [
    "BankingServices.postman_environment.variables.json"
]

# Test data files
# -------------------------------------------
test_data_files = {}

