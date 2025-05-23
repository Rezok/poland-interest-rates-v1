import configparser
import os


class Configuration():
    @staticmethod
    def DeafaultConfig():
        config = configparser.ConfigParser()
        config["Default"] = {}
        
        return config
        
    @staticmethod
    def CreateDefaultConfig():
        config = Configuration.DeafaultConfig()
        
        with open("config.ini", "w") as config_file:
            config.write(config_file)
    
    @staticmethod
    def LoadConfig():
        config = configparser.ConfigParser()
        
        if os.path.exists("config.ini"):
            config.read("config.ini")
        else:
            Configuration.CreateDefaultConfig()