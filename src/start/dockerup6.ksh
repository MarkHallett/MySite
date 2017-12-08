# Dockerup6.ksh

. ./set_env.ksh -e DEV

docker run -p 5001:5001 \
    --mount source=mr,destination=/mr \
    markhallett/gbp_usd_eur_app
