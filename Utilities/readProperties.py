import configparser
import os

class RedConfig:
    # Initialize config parser
    config = configparser.RawConfigParser()

    # Dynamically get the absolute path to config.ini
    config_path = os.path.join(os.path.dirname(__file__), '..', 'Configuration', 'config.ini')

    # Read the config file
    files_read = config.read(config_path)
    if not files_read:
        raise FileNotFoundError(f"Config file not found at path: {config_path}")

    @staticmethod
    def getAppUrl():
        try:
            url = RedConfig.config.get('common info', 'webURL')
            return url
        except configparser.NoSectionError:
            raise Exception("Missing section [common info] in config.ini")
        except configparser.NoOptionError:
            raise Exception("Missing 'webURL' key in [common info] section")

    @staticmethod
    def getUseremail():
        try:
            username = RedConfig.config.get('common info', 'username')
            return username
        except configparser.NoSectionError:
            raise Exception("Missing section [common info] in config.ini")
        except configparser.NoOptionError:
            raise Exception("Missing 'username' key in [common info] section")

    @staticmethod
    def getPassword():
        try:
            password = RedConfig.config.get('common info', 'password')
            return password
        except configparser.NoSectionError:
            raise Exception("Missing section [common info] in config.ini")
        except configparser.NoOptionError:
            raise Exception("Missing 'password' key in [common info] section")
