import os
import configparser

current_path = os.path.dirname(__file__)
cfgpath = os.path.join(current_path,'..//conf/config.ini')

class ConfigUtils:
    def __init__(self,config_path=cfgpath):
        self.__conf = configparser.ConfigParser()
        self.__conf.read(config_path, encoding="utf-8")
    def read_ini(self,sec,option):
        return self.__conf.get(sec,option)

    @property
    def get_driver_path(self):
        value = self.__conf.get('default','driver_path')
        return value
    @property
    def get_gecko_path(self):
        value = self.read_ini('default','gockdriver_path')
        return value
    @property
    def get_chandao_path(self):
        value = self.__conf.get('default', 'chandao_url')
        return value
    @property
    def get_username(self):
        value = self.read_ini('login', 'usename')
        return value
    @property
    def get_password(self):
        value = self.read_ini('login', 'password')
        return value

    @property
    def get_driver_name(self):
        driver_name_value = self.__conf.get('default', 'driver_name')
        return driver_name_value


conf = ConfigUtils()
if __name__=='__main__':
    config = ConfigUtils()
    print(conf.get_driver_name)
