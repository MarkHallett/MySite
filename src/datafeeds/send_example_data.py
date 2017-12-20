# send_example.py

import os
import datetime
import pika

def open_channel(q):
    url1 = os.environ['MR_RABITMQ']

    connection = pika.BlockingConnection(pika.URLParameters(url1))
    channel = connection.channel()

    channel.exchange_declare(exchange=q, type='fanout')
    return channel


def get_v(rate):
    trade_time = str(datetime.datetime.now())
    msg = str(trade_time) + ',' + str(rate)
    return msg


def run():

    CCY_PAIR_NAME = os.getenv('CCY_PAIR_NAME')
    CCY_PAIR_VALUE = os.getenv('CCY_PAIR_VALUE')

    print (CCY_PAIR_NAME, CCY_PAIR_VALUE)
    #print (CCY_PAIR_VALUE)
    #print (os.getenv('MR_RABITMQ'))

#    q = CCY_PAIR_NAME
#    channel = open_channel(q)

    # open open_channel
    url1 = os.environ['MR_RABITMQ']

    connection = pika.BlockingConnection(pika.URLParameters(url1))
    channel = connection.channel()

    q = CCY_PAIR_NAME

    channel.exchange_declare(exchange=q, type='fanout')


    v = get_v(CCY_PAIR_VALUE)

    channel.basic_publish(exchange=q, routing_key='', body=v)

    #print(" [x] Sent %r" % message)
    connection.close()


if __name__ == '__main__':
    run()
