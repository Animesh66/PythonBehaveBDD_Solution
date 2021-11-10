from configparser import ConfigParser


def config_reader(section, key):
    config = ConfigParser()
    config.read(".\\Config_Data\\config.ini")
    return config.get(section, key)
