import kabusapi

url = "localhost"
port = "18081"
password = "hogehoge"

api = kabusapi.Context(url, port, password)


# 注文発注 (先物買い)
data = {
    "Password": "hoge",
    "Symbol": 165120018,  # 日経平均先物 20/12
    "Exchange": 23,
    "TradeType": 1,
    "TimeInForce": 2,
    "Side": 2,
    "Qty": 1,
    "ClosePositionOrder": None,
    "FrontOrderType": 120,  # 成行
    "Price": 0,
    "ExpireDay": 0,
}
response = api.sendorder.future(**data)
print(response)


# 注文発注（オプション買い）
{
    "Password": "hoge",
    "Symbol": 135126818,  # 日経平均オプション 20/12 プット 26875
    "Exchange": 23,
    "TradeType": 1,
    "TimeInForce": 2,
    "Side": 2,
    "Qty": 10,
    "ClosePositionOrder": None,
    "FrontOrderType": 120,  # 成行
    "Price": 0,
    "ExpireDay": 0,
}
response = api.sendorder.option(**data)
print(response)


# 取引余力（先物）
response = api.wallet.future()
print(response)


# 取引余力（先物）（銘柄指定）
data = {
    "symbol": 165120018,
    "exchange": 23,
}
response = api.wallet.option(**data)
print(response)


# 取引余力（オプション）
response = api.wallet.option()
print(response)


# 取引余力（オプション）（銘柄指定）
data = {
    "symbol": 135126818,
    "exchange": 23,
}
response = api.wallet.option(**data)
print(response)


# 注文約定照会（取得商品選択）
data = {
    "product": 3,  # 先物
}
response = api.orders(**data)
print(response)


# 残高照会（取得商品選択）
data = {
    "product": 4,  # OP
}
response = api.positions(**data)
print(response)


# 先物銘柄コード取得
data = {
    "FutureCode": "NK225",
    "DerivMonth": 0,
}
response = api.symbolname.future(**data)
print(response)


# オプション銘柄コード取得
data = {
    "DerivMonth": 0,
    "PutOrCall": 'P',
    "StrikePrice": 0,
}
response = api.symbolname.option(**data)
print(response)


# ランキング取得
data = {
    "Type": 1,
    "ExchangeDivision": 'ALL',
}
response = api.ranking(**data)
