#! /bin/ksh
# set_env.ksh
#
# . ./set_env.ksh -e DEV

usage()
{
   echo "usage $0 [-h -e:]"
   echo " -h help"
   echo " -e <env (DEV,PROD)>"
   echo ""
   exit
}

###################################################
# main
###################################################

while getopts "he:" thisflag; do
  case ${thisflag} in
    h) usage ;;
    e) MRENV=${OPTARG};;
  esac
done

if [ -z ${MRENV} ] ; then
  echo " Error - No ENV set"
  exit
fi
# if env = None echo no env exit

echo "reading env for " ${MRENV}



`python ./scripts/read_env.py -e ${MRENV}`

echo "Done"
