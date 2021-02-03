import requests
import json


class EntitySpec(object):
    def __init__(self, ctx):
        self.ctx = ctx

    def __call__(self, **kwargs):
        payload = json.dumps(kwargs).encode('utf8')

        response = requests.post(
            self.ctx._base_url + '/kabusapi/sendorder',
            payload,
            headers=self.ctx._headers)

        return json.loads(response.text)

    def future(self, **kwargs):
        payload = json.dumps(kwargs).encode('utf8')

        response = requests.post(
            self.ctx._base_url + '/kabusapi/sendorder/future',
            payload,
            headers=self.ctx._headers)

        return json.loads(response.text)

    def option(self, **kwargs):
        payload = json.dumps(kwargs).encode('utf8')

        response = requests.post(
            self.ctx._base_url + '/kabusapi/sendorder/option',
            payload,
            headers=self.ctx._headers)

        return json.loads(response.text)
