import configparser
from logger import Logger
from configuration import Configuration

def main():
    Logger.setup()
    Logger.info("Application started.")
    Configuration.loadConfig()
    Logger.info("Application ended.")
  
main()