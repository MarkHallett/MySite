#  #! /usr/local/bin/python
# read_envs.py (v2)

# Pre getenv read of envvars

import os
import sys
import getopt
import ConfigParser

def run(env):
    #file_name = '/sblfront/tmp/halletm/dev/env_vars/simple/sblenv.dat'
    file_name = './env.dat' # %(env)
    #print '**** using ',file_name
    #return

    parser = ConfigParser.SafeConfigParser()
    #file_name = '%s.dat' %(env)
    parser.read(file_name)


    env_vars = {}
    for n, v in parser.items(env):
        n = n.upper()
        env_vars[n] = v

    names = env_vars.keys()
    names.sort()
    for n in names:
        v = env_vars[n]
        print 'export %s=%s' %(n,v)


# ############################################

if __name__ == '__main__':

    env = 'PROD'

    run(env)
