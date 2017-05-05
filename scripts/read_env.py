#  #! /usr/local/bin/python
# read_envs.py (v2)

# Pre getenv read of envvars

import os
import sys
import getopt
import ConfigParser

def run(env):
    file_name = './env.dat'
    parser = ConfigParser.SafeConfigParser()

    # read env name/values from the dat file
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
    env = 'DEV'
    opts, args = getopt.getopt(sys.argv[1:],"e:")
    for o,a in opts:
      if o == "-e":
            env = a

    run(env)
