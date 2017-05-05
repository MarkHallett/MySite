#! /bin/ksh
# set_env.ksh

ENV=${1}
# if env = None echo no env exit

echo "ENV " ${1}

`python ./scripts/read_env.py -e ${ENV}`
