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
            self.ctx._base_url + '/kabusapi/register',
            payload,
            headers=self.ctx._headers)

        return json.loads(response.text)
