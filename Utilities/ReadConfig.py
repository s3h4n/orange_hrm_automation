import configparser
import os


class ReadConfig:
    """Utility class to read configuration from config.ini file"""

    @staticmethod
    def get_config():
        config = configparser.RawConfigParser()
        config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'Configuration',
                                   'config.ini')
        config.read(config_path)
        return config

    @staticmethod
    def get_application_url():
        config = ReadConfig.get_config()
        return config.get('common info', 'baseURL')

    @staticmethod
    def get_username():
        config = ReadConfig.get_config()
        return config.get('common info', 'username')

    @staticmethod
    def get_password():
        config = ReadConfig.get_config()
        return config.get('common info', 'password')