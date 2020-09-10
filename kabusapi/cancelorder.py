import requests
import json

class EntitySpec(object):
    def __init__(self, ctx):
        self.ctx = ctx

    def __call__(self, **kwargs):
        payload = json.dumps(kwargs).encode('utf8')

        response = requests.put(
            self.ctx.base_url + '/kabusapi/cancelorder',
            payload,
            headers=self.ctx.headers)

        return json.loads(response.text)
