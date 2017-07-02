import configparser

MAC_LIST = "mac_list"
USER_ACCESS = "authentication"
URL = "url"
FILE_PATH = "./config.ini"


class ConfigHelper:
    mac_list = dict()
    url = None
    user_access = None
    config = configparser.ConfigParser()

    def __init__(self):
        self.config.read(FILE_PATH)
        self.config.sections()
        self.mac_list = self.mount_mac_list()
        self.url = self.mount_url()
        self.user_access = self.mount_user_access()

    def get_mac_list(self):
        return self.mac_list

    def get_user_access(self):
        return self.user_access

    def get_url(self):
        return self.url

    def mount_mac_list(self):
        response = dict()
        options = self.config.options(MAC_LIST)
        for raw_mac in options:
            mac = self.parse_macaddr(raw_mac)
            response[mac] = self.config.get(MAC_LIST, raw_mac)
        return response

    def parse_macaddr(self, mac):
        return mac.replace("-", ":")

    def mount_url(self):
        return self.config.get(URL, 'url')

    def mount_user_access(self):
        options = self.config.options(USER_ACCESS)
        return tuple(self.config.get(USER_ACCESS, i) for i in options)
