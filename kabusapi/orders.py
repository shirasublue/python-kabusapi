import requests
import json

class EntitySpec(object):
    def __init__(self, ctx):
        self.ctx = ctx

    def __call__(self, **kwargs):
        payload = None
        product = kwargs.get("product")
        if product:
            payload = {
                "product": product,
            }

        response = requests.get(
            self.ctx._base_url + '/kabusapi/orders',
            params=payload,
            headers=self.ctx._headers)

        return json.loads(response.text)
