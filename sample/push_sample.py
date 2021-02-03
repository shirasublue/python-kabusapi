import kabusapi

url = "localhost"
port = "18081"  # 検証用, 本番用は18080

# 初期設定　PUSH配信にトークン・パスワードは不要
api = kabusapi.Context(url, port, )

# 受信用関数　情報が受信される度にここが呼ばれる


@api.websocket
def recieve(msg):
    print(msg)
    # ここで処理を行う


# 受信開始
api.websocket.run()
