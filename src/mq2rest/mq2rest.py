#!/usr/bin/env python2.7
# mq2rest.py

import os
import json
import random
#from tornado import websocket, web, ioloop
import datetime
from time import time

import logging
import logging.config

import pika

from requests import put, get, post, delete, request


cl = []

# Random number generator
r = lambda: random.randint(0,255)

# Boilerplate WebSocket code
class Mq2rest(object):#websocket.WebSocketHandler):

    # Our function to get new data for charts
    def wait_for_data(self):
        logging.info('wait_for_data')

        url1 = os.environ['MR_RABITMQ']
        connection = pika.BlockingConnection(pika.URLParameters(url1))

        channel = connection.channel()
        q1 = 'GBP/USD/EUR'
        channel.exchange_declare(exchange=q1, type='fanout')
        result = channel.queue_declare(exclusive=True)
        queue_name = result.method.queue
        channel.queue_bind(exchange=q1, queue=queue_name)
        channel.basic_consume(self.callback_gbp_usd_eur, queue=queue_name, no_ack=True)

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

    def callback_gbp_usd_eur(self,ch, method, properties, body):
        # send data
        logging.info('callback_gbp_usd_eur (s) %s' %body)

        try:
            t, v = str(body).split(',')
        except:
            v = body
            t = datetime.datetime.now()

        if v in ('e','?'):
            return

        if isinstance(v,str):
            v = v.strip("'")

        try:
            y = float(v)
        except:
            return # not ideal way to handle it

        y = round(y,4)
        #y = self.x.get_value('GBP/USD/EUR')
        #logger.info('send y')

        logging.info(('t',t))
        #msg = 'write %s' %point_data
        #logging.info(msg)
        payload = {'name':'GBP/USD/EUR','id':4,'value':y, 'trade_time':str(t)}
        #print put('http://127.0.0.1:5000/todo/api/v1.0/tasks/1', json=payload )
        print ('post http://0.0.0.0:8888/api', payload )
        post ('http://0.0.0.0:8888/api', payload )


    def callback_gbp_usd(self,ch, method, properties, body):
        logging.info('callback_gbp_usd %s' %body)
        print('callback_gbp_usd %s' %body)

        t, v = str(body).split(',')

        if v in ('e','?'):
            return

        if isinstance(v,str):
            v = v.strip("'")
        y = float(v)
        #y = float(v[0:-1])
        #y = float(body)
        #y = self.x.get_value('GBP/USD/EUR')
        #logger.info('send y')

        # odd but true, container needs this
        if len(t) == 28:
            t = t[2:]

        payload = {'name':'GBP/USD','id':1,'value':y, 'trade_time':t}
        logging.info('post...')
        logging.info(payload)
        #print put('http://127.0.0.1:5000/todo/api/v1.0/tasks/1', json=payload )
        #print ('post http://0.0.0.0:8888/api', payload )
        #post ('http://0.0.0.0:8888/api', json=payload )

        url = "http://0.0.0.0:8888/api"
        response = request("POST", url,  params=payload)
        logging.info(response.text)

    def callback_usd_eur(self,ch, method, properties, body):
        logging.info('callback_usd_eur %s' %body)
        t, v = str(body).split(',')
        #y = float(v[:-1])

        if v in ('e','?'):
            return

        if isinstance(v,str):
            v = v.strip("'")
        y = float(v)
        #y = float(body)
        #y = self.x.get_value('GBP/USD/EUR')
        #logger.info('send y')

        # odd but true container needs this
        if len(t) == 28:
            t = t[2:]

        payload = {'name':'USD/EUR','id':2,'value':y, 'trade_time':t}
        #print ('post http://0.0.0.0:8888/api', payload )
        url = "http://0.0.0.0:8888/api"
        response = request("POST", url,  params=payload)
        logging.info(response.text)
        #self.write_message(json.dumps(point_data))


    def callback_eur_gbp(self,ch, method, properties, body):
        logging.info('callback_eur_gbp %s' %body)
        t, v = str(body).split(',')
        #y = float(v[:-1])
        if v in ('e','?'):
            return

        if isinstance(v,str):
            v = v.strip("'")
        y = float(v)
        #y = float(body)
        #y = self.x.get_value('GBP/USD/EUR')
        #logger.info('send y')

        # odd but true, container needs this
        if len(t) == 28:
            t = t[2:]

        logging.info(t)
        payload = {'name':'EUR/GBP','id':3,'value':y, 'trade_time':t}

        url = "http://0.0.0.0:8888/api"
        response = request("POST", url,  params=payload)
        logging.info(response.text)



if __name__ == "__main__":

        LOG = os.environ.get('LOG','/mr/log')
        INI = os.environ.get('INI','/mr/ini')

        print ('LOG', LOG)
        print ('INI', INI)

        log_ini = os.path.join(INI,'logging_config_mq2rest.ini')
        if not os.path.isfile(log_ini):
            print (log_ini)
            print ("ini file missing")

        else:
            print (log_ini)
            print ("ini files exists")

            logging.config.fileConfig(log_ini)

            logger = logging.getLogger()#.addHandler(logging.StreamHandler())
            logger.info('Start')

            mq2rest = Mq2rest()
            mq2rest.wait_for_data()

        #try:
        #except Exception, e:
        #    print 'ss'
        #    logger.exception("Fatal error in get_prices")

        #application.listen(8002)
        #ioloop.IOLoop.instance().start()

        #logger.info('End')
