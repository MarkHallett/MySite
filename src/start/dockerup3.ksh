# Dockerup3.ksh

. ./set_env.ksh -e DEV

docker run \
    -e MR_RABITMQ=${MR_RABITMQ} \
    --mount source=mr,destination=/mr \
    --name calc_gbp_usd_eur \
    markhallett/calc_gbp_usd_eur
