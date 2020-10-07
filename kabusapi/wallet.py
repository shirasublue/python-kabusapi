import requests
import json

class EntitySpec(object):
    def __init__(self, ctx):
        self.ctx = ctx

    def cash(self, **kwargs):
        symbol = kwargs.get("symbol")
        exchange = kwargs.get("exchange")

        if symbol and exchange:
            response = requests.get(
                self.ctx._base_url + '/kabusapi/wallet/cash'
                    + '/'+ str(symbol) + '@' + str(exchange),
                headers=self.ctx._headers)
        else:
            response = requests.get(
                self.ctx._base_url + '/kabusapi/wallet/cash',
                headers=self.ctx._headers)

        return json.loads(response.text)

    def margin(self, **kwargs):
        symbol = kwargs.get("symbol")
        exchange = kwargs.get("exchange")

        if symbol and exchange:
            response = requests.get(
                self.ctx._base_url + '/kabusapi/wallet/margin'
                    + '/'+ str(symbol) + '@' + str(exchange),
                headers=self.ctx._headers)
        else:
            response = requests.get(
                self.ctx._base_url + '/kabusapi/wallet/margin',
                headers=self.ctx._headers)

        return json.loads(response.text)
