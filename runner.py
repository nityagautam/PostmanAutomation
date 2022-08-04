# =============================================
# Author           :
# Created          : 08 July 2022
# Last Modified    : 
# Last Modified by :
# Desc             : Runner of the automation framework
# =============================================


# Imports
# ------------------------------------
import json
import sys
from optparse import OptionParser
from core.collector import Collector
from core.utils.utilities import log_special_message, Utilities
from core.utils.logger import Logger
import core.configs.config as config

# Getting the logger
# ------------------------------------
log = Logger(__name__).get_logger()


# ================================
# Set the cli options and execute
# ================================
def main():
    # Adding cli options for Runner file
    # ---------------------------------------
    usage_msg = "\n" \
                "synopsis: python3 runner.py [options] \n" \
                "Example: \n" \
                "        python3 runner.py --test-suite=sanity,sample --env=test --check\n" \
                "\n"
    cli_options = OptionParser(usage=usage_msg)
    cli_options.add_option("--test-suite", "-t", type="string", dest="testSuite", help="Provide this to consider the suites")
    cli_options.add_option("--env", "-e", type="string", dest="testEnv", help="Provide this to specify the eenvironment for the collections")
    cli_options.add_option("--check", "-c", action="store_true", dest="systemCheck", default=False, help="Provide this to check the pre-reequisite binaries")
    cli_options.add_option("--no-run", "-n", action="store_true", dest="noRun", default=False, help="Provide this to stop the newman execution")
    (options, args) = cli_options.parse_args()

    # Finally show the collected args
    log.info("Collected following cli options:: ")
    log.info(options)

    # Check for the provided args length
    # -------------------------------------
    if len(args) < 1:
        # If I don't want to ahead without options then I should exit now
        if not config.framework["RUN_WITHOUT_OPTIONS"]:
            log_special_message("Looks like you have not given enough options for execution; Will Exit now... \n"
                                "In case you are not sure about the usage of option, refer following: \n\n"
                                "" + cli_options.get_usage(), typ='warning')
            sys.exit(0)

        # Lets say not enough, if running without options
        # log_special_message("Looks like you have not used options; so will be using defaults. \n"
        #                     "In case you are not sure about the usage of option then see the usage following: \n\n"
        #                     "" + cli_options.get_usage(), typ='warning')

    # Take the first argument value
    # file = args[0]

    # Verify the options
    if options.systemCheck:
        # Check the binaries
        Utilities().check_the_binaries()

    # If --no-run option is false (or not provided)
    if not options.noRun:
        # Start the collector to collect everything
        collector_obj = Collector().run()
        log_special_message("Collector status is: \n" + json.dumps(collector_obj, sort_keys=True, indent=4), typ="debug")

        # Execute the command now
        stdo, stde = Utilities().run_system_command(collector_obj.get('command'))

        log.info(f"\n "
                 f"{'=-' * 60} \n"
                 f" Test has been executed. Please find the report file at: {config.framework['REPORT_FILE_PATH']}\n "
                 f"{'=-' * 60} \n\n")


# ================================
# Execute the script now
# ================================ 
if __name__ == "__main__":

    # Call the main with option parser
    main()
