import requests
import json

class EntitySpec(object):
    def __init__(self, ctx):
        self.ctx = ctx

    def __call__(self, **kwargs):
        symbols = kwargs.get('Symbols')
        payload = json.dumps(
            {"Symbols": symbols}).encode('utf8')

        response = requests.put(
            self.ctx.base_url + '/kabusapi/unregister',
            payload,
            headers=self.ctx.headers)

        return json.loads(response.text)

    def all(self):
        response = requests.put(
            self.ctx.base_url + '/kabusapi/unregister/all',
            headers=self.ctx.headers)

        return json.loads(response.text)
