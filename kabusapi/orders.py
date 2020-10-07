import requests
import json

class EntitySpec(object):
    def __init__(self, ctx):
        self.ctx = ctx

    def __call__(self):
        response = requests.get(
            self.ctx._base_url + '/kabusapi/orders',
            headers=self.ctx._headers)

        return json.loads(response.text)
