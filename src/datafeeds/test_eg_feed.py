# test_eg_feed.py




# read_rates

import os
import time

def process_row(row):
    print row

    for ccy_pair in ('GBP/USD','USD/EUR','EUR/GBP'):
         print ccy_pair, row[ccy_pair]

         cmd = 'test_docker_pub_ccy.ksh %s %s' %(ccy_pair, row[ccy_pair])
         print cmd
         os.system(cmd)
         #time.sleep(1)

    #time.sleep(3)



def run():
    print '#################################'

    file_dir = r'./data'
    file_name = r'CcyRates1Year.csv'

    fileName = os.path.join(file_dir,file_name)
    print 'fileName', fileName


    if not os.path.isfile(fileName):
        print 'Error File %s does not exist' %fileName
        return

    try:
        file = open(fileName)
        data = file.read()
        file.close()
    except IOError:
        print 'Error reading file %s' %fileName

    data = data.split()

    headers = data[0].split(',')

    for count, row in enumerate(data[1:]):#
        print count
        r = dict(zip(headers,row.split(',') ))

        process_row(r)

        #break
        #if count > 2 : break

run()
