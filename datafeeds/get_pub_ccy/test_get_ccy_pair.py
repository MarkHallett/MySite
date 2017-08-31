# test_get_ccy_pair.py

from yahoo_finance import Currency

ticker = "GBPUSD"

def get_rate(ticker):
    rate = 0

    while rate == 0:
        try:
            ccy_pair =  Currency(ticker)
            ccy_pair.refresh()
            rate = ccy_pair.get_rate()
        except Exception, e:
            pass
    return rate

print get_rate(ticker)
print get_rate(ticker)
