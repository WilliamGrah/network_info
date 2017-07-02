import collections
import requests
from helpers.config_helper import ConfigHelper


class Helper:
    ConfigHelper = ConfigHelper()
    mac_list = ConfigHelper.get_mac_list()
    url = ConfigHelper.get_url()
    auth = ConfigHelper.get_user_access()
    User = collections.namedtuple('User', [
            'macaddress',
            'download',
            'download_speed',
            'upload',
            'upload_speed'
        ])

    users = dict()

    def load(self):
        source_code = requests.get(self.url, auth=self.auth)
        self.parse(source_code.text)

    def parse(self, data):
        for line in data.split('\n'):
            if 'bgcolor=#b7b7b7' in line:
                for line in line.split('tr'):
                    if len(line) > 10:
                        line = line.replace("</td><td><font size=2>", ",")
                        parse = line[line.find('2>')+2:line.find('</')]
                        tmp = parse.split(',')

                        if tmp[0] in self.users:
                            old_user = self.users[tmp[0]]
                        else:
                            old_user = self.User(tmp[0], 0, 0, 0, 0)

                        name = tmp[0]
                        if tmp[0] in self.mac_list:
                            name = self.mac_list[tmp[0]]

                        tmp_user = self.User(
                                name,
                                tmp[1],
                                abs(int(old_user.download)-int(tmp[1])),
                                tmp[2],
                                abs(int(old_user.upload)-int(tmp[2])))

                        self.users[tmp[0]] = tmp_user

    def get_users(self):
        return self.users
