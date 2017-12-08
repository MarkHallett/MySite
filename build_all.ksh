# build_all.ksh

docker build -t markhallett/calc_gbp_usd_eur -f ./src/docker_files/Dockerfile_calc_gbp_usd_eur .
docker build -t markhallett/mq2rest -f ./src/docker_files/Dockerfile_mq2rest .
docker build -t markhallett/rest2web -f ./src/docker_files/Dockerfile_rest2web .
docker build -t markhallett/gbp_usd_eur_app -f ./src/docker_files/Dockerfile_gbp_usd_eur_app .
docker build -t markhallett/app -f ./src/docker_files/Dockerfile_app .
