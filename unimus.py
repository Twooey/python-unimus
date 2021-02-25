import urllib3
import json
import base64
import datetime


class unimus:

    def __init__(self, url, header):
        self.url = url + '/api/v2'
        self.header = header

    def __httprequest(self, URL):
        http = urllib3.PoolManager()
        r = http.request('GET',
                         URL,
                         headers=self.header)
        return json.loads(r.data.decode('utf-8'))

    def health_check(self):
        a = self.url + '/health'
        r = self.__httprequest(a)
        return r['data']['status']

    def get_schedule(self, id):
        a = self.url + '/schedules/' + str(id)
        r = self.__httprequest(a)
        return r

    def get_device_by_id(self, id):
        a = self.url + '/devices/' + str(id) + '?attr=:attributes'
        r = self.__httprequest(a)
        return r

    def get_device_by_address(self, address):
        a = self.url + '/devices/findByAddress/' + address + '?attr=:attributes'
        r = self.__httprequest(a)
        return r

    def get_device_by_description(self, description):
        a = self.url + '/devices/findByDescription/' + description
        r = self.__httprequest(a)
        return r

    def get_backup(self, device_id, backup):
        a = self.url + '/devices/' + str(device_id) + '/backups'
        r = self.__httprequest(a)
        return base64.b64decode(r['data'][backup]['bytes'])
