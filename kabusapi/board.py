import requests
import json

class EntitySpec(object):
    def __init__(self, ctx):
        self.ctx = ctx

    def __call__(self, **kwargs):
        symbol = kwargs.get("symbol")
        exchange = kwargs.get("exchange")

        response = requests.get(
            self.ctx.base_url + '/kabusapi/board'
                + '/'+ str(symbol) + '@' + str(exchange),
            headers=self.ctx.headers)

        return json.loads(response.text)
