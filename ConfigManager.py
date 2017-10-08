from configparser import ConfigParser, DuplicateSectionError

config = ConfigParser()
default_config_file = 'default.ini'
config_file = 'config.ini'


class ConfigManager:
    @staticmethod
    def load():
        config.read(default_config_file)
        config.read(config_file)

    @staticmethod
    def save():
        with open(config_file, 'w') as f:
            config.write(f)

    @staticmethod
    def config():
        return config
