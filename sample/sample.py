import kabusapi

url = "localhost"
port = "18081"  # 検証用, 本番用は18080
password = "hogehoge"

# 初期設定・トークン取得
api = kabusapi.Context(url, port, password)


# 注文発注 (現物買い)
data = {
    "Password": "hoge",
    "Symbol": 8306,  # MUFG
    "Exchange": 1,
    "SecurityType": 1,
    "Side": 2,
    "CashMargin": 1,
    "MarginTradeType": None,
    "DelivType": 1,
    "FundType": "02",
    "AccountType": 4,
    "Qty": 100,
    "ClosePositionOrder": None,
    "Price": 0,
    "ExpireDay": 0,
    "FrontOrderType": 10,
}
response = api.sendorder(**data)


# 注文取消
data = {
    "OrderId": "hoge",
    "Password": "fuga",
}
response = api.cancelorder(**data)


# 取引余力（現物）
response = api.wallet.cash()


# 取引余力（現物）（銘柄指定）
data = {
    "symbol": 8306,
    "exchange": 1,
} 
response = api.wallet.cash(**data)


# 取引余力（信用） 
response = api.wallet.margin()


# 取引余力（信用）（銘柄指定）
data = {
    "symbol": 8306,
    "exchange": 1,
} 
response = api.wallet.margin(**data)


# 時価情報・板情報
data = {
    "symbol": 8306,
    "exchange": 1,
} 
response = api.board(**data)


# 銘柄情報
data = {
    "symbol": 8306,
    "exchange": 1,
} 
response = api.symbol(**data)


# 注文約定照会
response = api.orders()


# 残高照会
response = api.positions()


# 銘柄登録
data = {
    "Symbols": [
        { "Symbol": 8306, "Exchange": 1, },
        { "Symbol": 9433, "Exchange": 1, },
    ]
} 
response = api.register(**data)


# 銘柄登録解除 
data = {
    "Symbols": [
        { "Symbol": 8306, "Exchange": 1, },
        { "Symbol": 9433, "Exchange": 1, },
    ]
} 
response = api.unregister(**data)


# 銘柄登録全解除
response = api.unregister.all()
