# get_pub_ccy.py

import os
import sys
import getopt
import logging
import logging.config
import time
import datetime

try:
    from urllib2 import HTTPError
except ImportError:
    import urllib.request, urllib.parse, urllib.error
    import urllib.request, urllib.error, urllib.parse
    from urllib.error import HTTPError

from yahoo_finance import Currency
import pika

def usage():
    print ('get_pub_ccy.py')
    print ('  -c ccy (MR_CCY_PAIR)')
    print ('  -v 1.2 (send one time value)')
    print ('eg get_pub_ccy.py -c "GBP/USD" ')
    print ('eg get_pub_ccy.py -c "GBP/USD" -v 1.2 ')
    print ('  (if env vars set, uses MR_CCY_FREQ, MR_RABITMQ)')


def get_rate(ticker):
    rate = 0
    trade_time = 0

    while rate == 0:
        try:
            ccy_pair =  Currency(ticker)
            ccy_pair.refresh()
            rate = ccy_pair.get_rate()
            #trade_time = str(ccy_pair.get_trade_datetime())
            trade_time = datetime.datetime.now().time()

        except HTTPError as e:
            logging.debug('HTTP Error')
        except Exception as e:
            logging.exception(e)
            raise e
    return rate,trade_time


def get_v(ccy, ot_val=None):
    ticker = ccy.replace('/','')
    #logging.info('ticker %s' %ticker)
    if ot_val:
        rate = str(ot_val)
        trade_time = str(datetime.datetime.now())
    else:
        try:
            #ccy_pair = Currency(ticker)
            rate,trade_time = get_rate(ticker)
        except Exception as e:
            #print str(e)
            return None
        #rate = str(ccy_pair.get_rate())
        #trade_time = str(ccy_pair.get_trade_datetime())

    msg = str(trade_time) + ',' + rate
    logger.info(msg)
    return msg
    return (str(trade_time) + ',' + str(rate))


def open_channel(q):
    url1 = os.environ['MR_RABITMQ']

    connection = pika.BlockingConnection(pika.URLParameters(url1))
    channel = connection.channel()

    channel.exchange_declare(exchange=q, type='fanout')
    return channel





def run(q):
    v = get_v(ccy)

    logger.info('run')
    logger.info('  queue %s' %q)
#    v = str(v)
    logger.debug('test')

    #url1 = 'amqp://xjdjtehg:9TQjzoOYM0Aabu6HgL1WCPz3v5-hqc8z@spotted-monkey.rmq.cloudamqp.com/xjdjtehg'
    #print os.environ['RABITMQ']

    channel = open_channel(q)

    MR_CCY_FREQ = float(os.environ['MR_CCY_FREQ'])
    msg =  'ccy read frequency (MR_CCY_FREQ) %s' %MR_CCY_FREQ
    logger.info(msg)

    while True:
        v = get_v(ccy)

        if not v:
            continue

        #logger.info('%s %s' %(ccy,v))

        channel.basic_publish(exchange=q, routing_key='', body=v)


        time.sleep(MR_CCY_FREQ)

        #print(" [x] Sent %r" % message)
    connection.close()

    msg = "publish [%s] value %s" %(q, v)
    logger.info(msg)


if __name__ == '__main__':

    ccy = os.environ.get('MR_CCY_PAIR',None)
    ot_val = None

    opts, args = getopt.getopt(sys.argv[1:],"hc:v:")
    for o,arg in opts:
        if o =='-h':
            usage()
            sys.exit(0)
        if o == '-c':
            ccy = arg
            #q = arg
            msg = 'ccy=%s' %arg
            print (msg)
        if o == '-v':
            ot_val = float(arg)


    LOG = os.environ.get('LOG','../log')
    INI = os.environ.get('INI','../ini')

    print ('LOG', LOG)
    print ('INI', INI)

    log_ini = os.path.join(INI,'logging_config.ini')
    if os.path.isfile(log_ini):
        print ("ini files exists")
    else:
        print (log_ini)
        print ("ini file missing")

    logging.config.fileConfig(log_ini)

    logger = logging.getLogger()#.addHandler(logging.StreamHandler())
    logger.info('Start')

    if ccy == None:
        logger.info('No ccy given, running as a test')
        logger.info(sys.version)
        rate, trade_time = get_rate('GBPUSD')
        logging.info( (rate, trade_time))

    else:
        logger.info(ccy)


        if ot_val:
            q = ccy
            channel = open_channel(q)
            v = get_v(ccy, ot_val)
            channel.basic_publish(exchange=q, routing_key='', body=v)

        else:
        #try:
            run(ccy)
        #except Exception, e:
        #    print 'ss'
        #    logger.exception("Fatal error in get_prices")
    logger.info('End')
