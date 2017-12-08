# Dockerup4.ksh

. ./set_env.ksh -e DEV

    #-p 8888:8888 \

docker run \
    --net=host \
    -e MR_RABITMQ=${MR_RABITMQ} \
    markhallett/mq2rest
