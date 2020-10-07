import requests
import json

from kabusapi import sendorder
from kabusapi import cancelorder
from kabusapi import wallet
from kabusapi import board
from kabusapi import symbol
from kabusapi import orders
from kabusapi import positions
from kabusapi import register
from kabusapi import unregister

class Context(object):
    def __init__(
        self,
        hostname='localhost',
        port=18080,
        password=None,
        token=None,
    ):
        self._hostname = hostname
        self._port = port
        self._base_url = "http://{}:{}".format(
            hostname, port,
        )
        self._headers = {'Content-Type': 'application/json', }

        self.token = token
        if token:
            self._set_header('X-API-KEY', token)
        else:
            self._set_token(password)        

        self.sendorder = sendorder.EntitySpec(self)
        self.cancelorder = cancelorder.EntitySpec(self)
        self.wallet = wallet.EntitySpec(self)
        self.board = board.EntitySpec(self)
        self.symbol = symbol.EntitySpec(self)
        self.orders = orders.EntitySpec(self)
        self.positions = positions.EntitySpec(self)
        self.register = register.EntitySpec(self)
        self.unregister = unregister.EntitySpec(self)

    def _set_header(self, key, value):
        self._headers[key] = (value)
    
    def _set_token(self, password):
        payload = json.dumps(
            {'APIPassword': password,}
        ).encode('utf8')

        response = requests.post(
            self._base_url + '/kabusapi/token',
            data=payload,
            headers=self._headers
        )

        try:
            self.token = json.loads(response.text)['Token']
        except:
            raise Exception(response.text)       

        self._set_header('X-API-KEY', self.token,)
