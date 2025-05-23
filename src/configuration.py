import configparser
import os
from logger import Logger


class Configuration():
    @staticmethod
    def DeafaultConfig():
        config = configparser.ConfigParser()
        config["Default"] = {}
        
        return config
        
    @staticmethod
    def createDefaultConfig():
        config = Configuration.DeafaultConfig()
        
        with open("config.ini", "w") as config_file:
            config.write(config_file)
    
    @staticmethod
    def loadConfig():
        config = configparser.ConfigParser()
        
        if os.path.exists("config.ini"):
            Logger.info("Loading config.ini file.")
            config.read("config.ini")
            Logger.info("Configuration loaded.")
        else:
            Logger.info("config.ini file not found.")
            Logger.info("Creating default app config.")
            Configuration.createDefaultConfig()
            Logger.info("Default configuration created.")