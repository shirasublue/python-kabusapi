import requests
import json


class EntitySpec(object):
    def __init__(self, ctx):
        self.ctx = ctx

    def future(self, **kwargs):
        future_code = kwargs.get("FutureCode")
        deriv_month = kwargs.get("DerivMonth")

        payload = {
            "FutureCode": future_code,
            "DerivMonth": deriv_month,
        }

        response = requests.get(
            self.ctx._base_url + '/kabusapi/symbolname/future',
            params=payload,
            headers=self.ctx._headers)

        return json.loads(response.text)

    def option(self, **kwargs):
        deriv_month = kwargs.get("DerivMonth")
        put_or_call = kwargs.get("PutOrCall")
        strike_price = kwargs.get("StrikePrice")

        payload = {
            "DerivMonth": deriv_month,
            "PutOrCall": put_or_call,
            "StrikePrice": strike_price,
        }

        response = requests.get(
            self.ctx._base_url + '/kabusapi/symbolname/option',
            params=payload,
            headers=self.ctx._headers)

        return json.loads(response.text)
