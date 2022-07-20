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

# Inside code integration goes here ...

# Setup/Config integration goes here ...

# test-data integration goes here ...


# ================================
# Execute the automation now
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
    print("Looks like not enough options, will exit now")
    cli_options.usage()
    Utilities.sys.exit(0)

  # Take the first argument value
  file = args[0]

  # Verify the options
  if options.log == True:
    pass



    
if __name__ == "__main__":
  # Start the process now
  #Utilities().say_hello()
  stdo, stde = Utilities().run_system_command("ls -la jai")
  # main() ==> Executing the main if Include the cli options as well

