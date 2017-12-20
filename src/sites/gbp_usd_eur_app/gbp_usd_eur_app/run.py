#!flask/bin/python

import os
from app import app

if __name__ == '__main__':

    print (os.listdir( '/mr/data') )
    app.run(host='0.0.0.0', port=5001)
