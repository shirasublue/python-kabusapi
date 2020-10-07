import requests
import json

class EntitySpec(object):
    def __init__(self, ctx):
        self.ctx = ctx

    def __call__(self, **kwargs):
        symbol = kwargs.get("symbol")
        exchange = kwargs.get("exchange")

        response = requests.get(
            self.ctx._base_url + '/kabusapi/symbol'
                + '/'+ str(symbol) + '@' + str(exchange),
            headers=self.ctx._headers)

        return json.loads(response.text)
