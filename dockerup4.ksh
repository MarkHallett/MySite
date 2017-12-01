# Dockerup4.ksh

. ./set_env.ksh -e DEV

docker run \
    #-p 8888:8888 \
    --net=host \
    -e MR_RABITMQ=${MR_RABITMQ} \
    markhallett/mq2rest
