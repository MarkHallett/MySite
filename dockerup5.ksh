# Dockerup5.ksh

. ./set_env.ksh -e DEV

docker run -p 8888:8888 \
    markhallett/rest2web
