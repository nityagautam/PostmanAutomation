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
import datetime

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
    __report_options = ""
    __cmd = ""

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
                self.__api_collections_to_run += "" + coll_config.collections_suite_path[test_type] + collection + " "

        # Add the quotes at both side for the collected files like: '<collected_files>'
        # self.__api_collections_to_run = "'" + self.__api_collections_to_run + "'"

        # return the collected api collection
        return self.__api_collections_to_run

    # Collect the api environment
    # --------------------------------------
    def collect_api_environment(self):
        # Collect the api environment
        # [default/ test/ debug]
        self.__api_environment = " " + \
                                 coll_config.api_environment[core_config.framework["API_EXECUTION_ENVIRONMENT"]] + \
                                 " "

        # return the collected api environment
        return self.__api_environment

    # Collect the report options for the execution
    # --------------------------------------------
    def collect_report_options(self):
        # Collect the report options
        file_path = core_config.framework["REPORT_FILE_PATH"]
        placeholder_text = str(datetime.datetime.now()).replace(" ", "_")
        html_file = file_path + core_config.framework["REPORT_FILE_NAME_HTML"].format(placeholder=placeholder_text)
        fancy_ht = file_path + core_config.framework["REPORT_FILE_NAME_FANCY_HTML"].format(placeholder=placeholder_text)
        junit_file = file_path + core_config.framework["REPORT_FILE_NAME_JUNIT"].format(placeholder=placeholder_text)
        json_file = file_path + core_config.framework["REPORT_FILE_NAME_JSON"].format(placeholder=placeholder_text)
        
        # For HTML Reports
        self.__report_options = core_config.newman_reports[core_config.framework["TEST_REPORTER_OPT_TO_USE"]]\
            .format(report_file_path=fancy_ht)

        # For mixed reports
        # self.__report_options = core_config.newman_reports[core_config.framework["TEST_REPORTER_OPT_TO_USE"]]\
        #     .format(html_report_file_path=html_file,
        #             fancy_html_report_file_path=fancy_ht,
        #             junit_report_file_path=junit_file,
        #             json_report_file_path=json_file
        #             )

        # return the collected report options
        return self.__report_options

    # Collect the final command
    def collect_the_final_command(self):
        # {collection_files} -e {env_file_name} -r {report_config}
        self.__cmd = core_config.newman_commands["RUN_WITH_ENV_VARS_WITH_REPORT"].format(
            collection_files=self.__api_collections_to_run,
            environment_file=self.__api_environment,
            report_options=self.__report_options
        )
        return self.__cmd

    # --------------------------------------
    # runner to collect all required inputs
    # --------------------------------------
    def run(self) -> dict:
        # Collect API Collection
        log.info("Collecting the api collection to be run ...")
        self.__collector_obj["test_collection"] = self.collect_api_collection()

        # Collect Environment
        log.info("Collecting the api environments ...")
        self.__collector_obj["test_environment"] = self.collect_api_environment()

        # Collect the report options
        log.info("Collecting the report options ...")
        self.__collector_obj["report_options"] = self.collect_report_options()

        # Collect/Build the final command to run
        log.info("Collecting/Building the final command ... ")
        self.__collector_obj["command"] = self.collect_the_final_command()

        # Return the dict obj
        return self.__collector_obj


# [DEBUG] Execute now
# -------------
#print("Return status is: ", Collector().show())
#print("Return status is: ", Collector().run())
