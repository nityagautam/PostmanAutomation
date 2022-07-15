# META:
# This contains the config variables
#

# ===========================================
# Avaialble mode : single | combined | mixed
collections_setup = {
    "mode": 'single',
    "variables_locations": 'PATH_TO_ENV_JSON_FOR_EACH'
    "data_files": 'bind_with_ENV'
}

# ===========================================

# Collection order
sanity_collections = []
regreession_collections = []

# data files
test_data_files = {}

# timeout in seconds
timeout = 30

# Binaries mapping
os_binaries = {}

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
