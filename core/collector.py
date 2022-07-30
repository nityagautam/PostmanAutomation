# ======================================================================================
# Logger Class
# META:
# Created: 28 July 2022
# Last modified: 28 July 2022
# Description: This class is responsible to collect the following:
#       - configuration
#       - api collection file
#       - environment file
#       - test-data file
#       - Basic unit test of system to run the test
# CAUTION : DO NOT TOUCH ANYTHING BELOW THIS,
#           IF U R NOT SURE OF UR ACTION.
# ======================================================================================

# Import section
# ----------------------------
import core.configs.config as core_config
import core.configs.config_api_collections_and_data as coll_config
from core.utils.logger import Logger

log = Logger(__name__).get_logger()


# Collector Class
# ----------------------------
class Collector:

    # Properties
    # --------------------
    __collector_obj = {}
    __api_collections_to_run = ""
    __api_environment = ""

    # Constructor
    # --------------------
    def __init__(self):
        pass

    def show(self) -> int:
        print(core_config.TIMEOUT)
        print(coll_config.test_data_files["global_csv_test_data_for_tc1"])
        return 0

    # Collect the tests
    # --------------------------------------
    def collect_api_collection(self):
        # Collect the api collections to run
        # [samples/ sanity/ regression/ etc]
        # --------------------------------------------------------------
        # Run through all the test types
        # and then collect the api collection based on that
        for test_type in core_config.framework["TEST_SUITES_TO_EXECUTE"]:
            for collection in coll_config.api_collections[test_type]:
                self.__api_collections_to_run += collection + " "
                #self.__collector_obj["test_collection"][test_type] += collection + " "

        # return the collected api collection
        return self.__api_collections_to_run

    # Collect the api environment
    # --------------------------------------
    def collect_api_environment(self):
        # Collect the api environment
        # [default/ test/ debug]
        self.__api_environment = coll_config.api_environment[core_config.framework["API_EXECUTION_ENV"]] + " "

        # return the collected api environment
        return self.__api_environment

    # Collect the report options for the execution
    # --------------------------------------------
    def collect_report_options(self):
        # Collect the report options
        self.__api_environment = coll_config.api_environment[core_config.framework["API_EXECUTION_ENV"]] + " "

        # return the collected api environment
        return self.__api_environment

    # --------------------------------------
    # runner to collect all required inputs
    # --------------------------------------
    def run(self) -> dict:
        self.__collector_obj = {}
        pass


# Execute now
# -------------
#print("Return status is: ", Collector().show())
print("Return status is: ", Collector().run())
