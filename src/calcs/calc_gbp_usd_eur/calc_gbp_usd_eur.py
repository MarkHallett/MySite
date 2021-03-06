# calc_gbp_usd_eur.py


import os
import logging
import logging.config

import pika

import gbp_usd_eur_dag


try:
    os.stat('/mr/data')
except:
    os.mkdir('/mr/data')

#D = gbp_usd_eur_dag.MyDAG('../data/gbp_usd_eur.png')
D = gbp_usd_eur_dag.MyDAG('/mr/data/gbp_usd_eur.png')

def callback_gbp_usd(ch, method, properties, body):
    logger.info("subscribed [GBP/USD] %r" % body)
    t,v = str(body).split(',')
    #v = float(v[:-1])
    v = float(v)
    #logger.info(v)
    #gbp_usd_eur_dag.MyDAG().set_a(v)
    #gbp_usd_eur_dag.MyDAG().set_input('gbp/usd',v)
    D.set_input('gbp/usd',v)

def callback_usd_eur(ch, method, properties, body):
    logger.info("subscribed [USD/EUR] %r" % body)
    t,v = str(body).split(',')

    #v = float(v[:-1])
    v = float(v)
    #logger.info(v)
    #gbp_usd_eur_dag.MyDAG().set_b(v)
    #gbp_usd_eur_dag.MyDAG().set_input('usd/eur',v)
    D.set_input('usd/eur',v)

def callback_eur_gbp(ch, method, properties, body):
    logger.info("subscribed [EUR/GBP] %r" % body)
    t,v = str(body).split(',')
    #v = float(v[:-1])
    v = float(v)
    #logger.info(v)
    #gbp_usd_eur_dag.MyDAG().set_c(v)
    #gbp_usd_eur_dag.MyDAG().set_input('eur/gbp',v)
    D.set_input('eur/gbp',v)


def run():
    logger.info('run')
    logger.debug('test')

    url1 = os.environ['MR_RABITMQ']
    connection = pika.BlockingConnection(pika.URLParameters(url1))

    channel = connection.channel()
    q1 = 'GBP/USD'
    channel.exchange_declare(exchange=q1, type='fanout')
    result = channel.queue_declare(exclusive=True)
    queue_name = result.method.queue
    channel.queue_bind(exchange=q1, queue=queue_name)
    channel.basic_consume(callback_gbp_usd, queue=queue_name, no_ack=True)

    channel2 = connection.channel()
    q2 = 'USD/EUR'
    channel2.exchange_declare(exchange=q2, type='fanout')
    result2 = channel2.queue_declare(exclusive=True)
    queue_name2 = result2.method.queue
    channel2.queue_bind(exchange=q2, queue=queue_name2)
    channel2.basic_consume(callback_usd_eur, queue=queue_name2, no_ack=True)


    channel3 = connection.channel()
    q3 = 'EUR/GBP'
    channel3.exchange_declare(exchange=q3, type='fanout')
    result3 = channel3.queue_declare(exclusive=True)
    queue_name3 = result3.method.queue
    channel3.queue_bind(exchange=q3, queue=queue_name3)
    channel3.basic_consume(callback_eur_gbp, queue=queue_name3, no_ack=True)


    logger.info('Waiting for messages.')
    print(' [*] To exit press CTRL+C')
    msg = '%s:%s' %('Output data',D.filename)
    logger.info(msg)
    channel.start_consuming()


if __name__ == '__main__':

    LOG = os.environ.get('LOG','/mr/log')
    try:
        os.stat(LOG)
    except:
        os.mkdir(LOG)


    INI = os.environ.get('INI','/usr/ini')

    print ('LOG', LOG)
    print ('INI', INI)

    log_ini = os.path.join(INI,'logging_config_calc_gbp_usd_eur.ini')
    if not os.path.isfile(log_ini):
        print (log_ini)
        print ("ini file missing")
        print log_ini

    else:
        print ("ini files exists")

        logging.config.fileConfig(log_ini)

        logger = logging.getLogger()
        #.addHandler(logging.StreamHandler())
        logger.info('Start')
        logger.info(log_ini)

        run()
        logger.info('End')
