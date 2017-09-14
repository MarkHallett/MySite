# Dockerup3.ksh

. ./set_env.ksh -e DEV

docker run \
    -e MR_RABITMQ=${MR_RABITMQ} \
    markhallett/calc_gbpusdeur
