import configparser
config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class RedConfig:
    @staticmethod
    def getAppUrl():
       url = config.get('common info', 'webURL')
       return url
    @staticmethod
    def getUseremail():
        username = config.get('common info', 'username')
        return username
    @staticmethod
    def getPassword():
        pasword = config.get('common info', 'password')
        return pasword



