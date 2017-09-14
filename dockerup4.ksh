# Dockerup4.ksh

. ./set_env.ksh -e DEV

docker run \
    --net=host \
    -e MR_RABITMQ=${MR_RABITMQ} \
    markhallett/mq2rest 

