# test_yahoo

from yahoo_finance import Currency

ticker = 'GBPUSD'

print Currency(ticker).get_rate()
