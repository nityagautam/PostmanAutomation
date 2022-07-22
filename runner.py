# =============================================
# Author           :
# Created          : 08 July 2022
# Last Modified    : 
# Last Modified by :
# Desc             : Runner of the automation framework
# =============================================


# Imports
# -----------
from optparse import OptionParser
from core.utilities import Utilities
from core.logger import Logger
import core.config as config
import core.api_collections_and_data_files as api_collection

# Getting the logger
# ------------------------
log = Logger().get_logger(__name__)


# Inside code integration goes here ...

# Setup/Config integration goes here ...

# test-data integration goes here ...


# ================================
# Set the cli options and execute
# ================================
def main():
  # Adding cli options for Runner file
  # ---------------------------------------
  cli_options = OptionParser(usage="")
  cli_options.add_option("--path", "-p", type="string", dest="collectionsPath")
  cli_options.add_option("--log", "-l", action="store_true", dest="log")
  (options, args) = cli_options.parse_args()

  # Check for the provided args length
  if len(args) < 1:
    #Lets say not enough
    log.error("Looks like not enough options, will exit now")
    cli_options.usage()
    Utilities.sys.exit(0)

  # Take the first argument value
  file = args[0]

  # Verify the options
  if options.log == True:
    pass



# ================================
# Execute the script now
# ================================ 
# How to run
# > python3 runner.py
#
if __name__ == "__main__":
  cmd = config.newman_commands["RUN"] + " " + api_collection.sanity_collections[0] + " -e " + api_collection.envvironment_collection[0]
  stdo, stde = Utilities().run_system_command(cmd)


