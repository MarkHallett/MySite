#!/usr/bin/env python2.7
# ws_gbp_usd_eur

import os
import json
import random
from tornado import websocket, web, ioloop
import datetime
from time import time

import logging
import logging.config

import pika

cl = []

# Random number generator
r = lambda: random.randint(0,255)

# Boilerplate WebSocket code
class WebSocketHandler(websocket.WebSocketHandler):

    def check_origin(self, origin):
        return True

    def open(self):
        logging.info( 'Connection established.')
        if self not in cl:
            print ('Append')
            cl.append(self)

        body = 33
        logging.info('callback_gbp_usd %s' %body)

        y = float(body)
        #y = self.x.get_value('GBP/USD/EUR')
        #logger.info('send y')
        point_data = { 'GBP/USD' :{
              'x': int(time()),
              'y': y
                }
                }

        for c in cl:
            c.write_message(json.dumps(point_data))

                #self.x = xx.yy('dd')
                # Set up a call to send_data in 5 seconds
                #for c in cl:
        #ioloop.IOLoop.instance().add_timeout(datetime.timedelta(seconds=1), self.wait_for_data)

    def on_message(self, message):
        print 'Message received {0}.'.format(message)

    def on_close(self):
        print 'Connection closed.'
        if self in cl:
            print ('Remove')
            cl.remove(self)

    # Our function to get new (random) data for charts
    def wait_for_data(self):
        logging.info('wait_for_data')
        #y = 10
        #self.send_data()

        url1 = 'amqp://xjdjtehg:9TQjzoOYM0Aabu6HgL1WCPz3v5-hqc8z@spotted-monkey.rmq.cloudamqp.com/xjdjtehg'
        connection = pika.BlockingConnection(pika.URLParameters(url1))

        channel = connection.channel()
        q1 = 'GBP/USD/EUR'
        channel.exchange_declare(exchange=q1, type='fanout')
        result = channel.queue_declare(exclusive=True)
        queue_name = result.method.queue
        channel.queue_bind(exchange=q1, queue=queue_name)
        channel.basic_consume(self.send_data, queue=queue_name, no_ack=True)

        channel2 = connection.channel()
        q2 = 'GBP/USD'
        channel2.exchange_declare(exchange=q2, type='fanout')
        result2 = channel2.queue_declare(exclusive=True)
        queue_name2 = result2.method.queue
        channel2.queue_bind(exchange=q2, queue=queue_name2)
        channel2.basic_consume(self.callback_gbp_usd, queue=queue_name2, no_ack=True)

        channel3 = connection.channel()
        q3 = 'USD/EUR'
        channel3.exchange_declare(exchange=q3, type='fanout')
        result3 = channel3.queue_declare(exclusive=True)
        queue_name3 = result3.method.queue
        channel3.queue_bind(exchange=q3, queue=queue_name3)
        channel3.basic_consume(self.callback_usd_eur, queue=queue_name3, no_ack=True)

        channel4 = connection.channel()
        q4 = 'EUR/GBP'
        channel4.exchange_declare(exchange=q4, type='fanout')
        result4 = channel4.queue_declare(exclusive=True)
        queue_name4 = result4.method.queue
        channel4.queue_bind(exchange=q4, queue=queue_name4)
        channel4.basic_consume(self.callback_eur_gbp, queue=queue_name4, no_ack=True)


        logger.info('Waiting for messages. GBP/USD/EUR')
        #print(' [*] To exit press CTRL+C')
        channel.start_consuming()

        # Call this again within the next 0-25 seconds
        timeout = r() / 50
        #for c in cl:

        #for c in cl:
        ioloop.IOLaoop.instance().add_timeout(datetime.timedelta(seconds=timeout), self.wait_for_data)

    def send_data(self,ch, method, properties, body):
        logging.info('send_data (s) %s' %body)
        y = float(body)
        z = 2*y
        #y = self.x.get_value('GBP/USD/EUR')
        #logger.info('send y')
        point_data = { 'GBP/USD/EUR' :{
              'x': int(time()),
              'y': y
                },
              'GBP/USDx' :{
              'x': int(time()),
              'y': z
                }
                }
        #msg = 'write %s' %point_data
        #logging.info(msg)

        self.write_message(json.dumps(point_data))

    def callback_gbp_usd(self,ch, method, properties, body):
        logging.info('callback_gbp_usd %s' %body)

        y = float(body)
        #y = self.x.get_value('GBP/USD/EUR')
        #logger.info('send y')
        point_data = { 'GBP/USD' :{
              'x': int(time()),
              'y': y
                }
                }

             # , 'color': '#%02X%02X%02X' % (r(), r(), r())
        for c in cl:
            c.write_message(json.dumps(point_data))

    def callback_usd_eur(self,ch, method, properties, body):
        logging.info('callback_usd_eur %s' %body)

        y = float(body)
        #y = self.x.get_value('GBP/USD/EUR')
        #logger.info('send y')
        point_data = { 'USD/EUR' :{
              'x': int(time()),
              'y': y
                }
                }

        self.write_message(json.dumps(point_data))


    def callback_eur_gbp(self,ch, method, properties, body):
        logging.info('callback_eur_gbp %s' %body)

        y = float(body)
        #y = self.x.get_value('GBP/USD/EUR')
        #logger.info('send y')
        point_data = { 'EUR/GBP' :{
              'x': int(time()),
              'y': y
                }
                }

        self.write_message(json.dumps(point_data))




application = web.Application([
              (r'/websocket', WebSocketHandler)
                ])

if __name__ == "__main__":

#    if __name__ == '__main__':

        LOG = os.environ.get('LOG','./log')
        INI = os.environ.get('INI','./ini')

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

        #try:
        #except Exception, e:
        #    print 'ss'
        #    logger.exception("Fatal error in get_prices")

        application.listen(8002)
        ioloop.IOLoop.instance().start()

        #logger.info('End')
