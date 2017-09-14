# dev_pub_ccy.py


import os
import sys
import getopt
import logging
import logging.config

import pika

def usage():
    print ('TODO')
    print ('  -q publish queue')
    print ('  -v publish value')

def run(q,v):
    #logger = logging.getLogger()#.addHandler(logging.StreamHandler())

    logger.info('run')
    logger.info('  queue %s' %q)
#    v = str(v)
    logger.debug('test')


    #url1 = 'amqp://xjdjtehg:9TQjzoOYM0Aabu6HgL1WCPz3v5-hqc8z@spotted-monkey.rmq.cloudamqp.com/xjdjtehg'
    url1 = os.environ['MR_RABITMQ']

    connection = pika.BlockingConnection(pika.URLParameters(url1))
    channel = connection.channel()


    channel.exchange_declare(exchange=q,
                         type='fanout')

    #message = ' '.join(sys.argv[1:]) or "info: Hello World!"
    channel.basic_publish(exchange=q,
                      routing_key='',
                      body=v)
    #print(" [x] Sent %r" % message)
    connection.close()

    msg = "publish [%s] value %s" %(q, v)
    logger.info(msg)


if __name__ == '__main__':

    v = 0.0

    opts, args = getopt.getopt(sys.argv[1:],"hq:v:")
    for o,arg in opts:
        if o =='-h':
            usage()
            sys.exit(0)
        if o == '-q':
            q = arg
            msg = 'q=%s' %arg
            print (msg)

        if o == '-v':
            v = arg

    LOG = os.environ.get('LOG','./dev/log')
    INI = os.environ.get('INI','./dev/ini')

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
    run(q,v)
    #except Exception, e:
    #    print 'ss'
    #    logger.exception("Fatal error in get_prices")
    logger.info('End')

else:
    logger = logging.getLogger()
