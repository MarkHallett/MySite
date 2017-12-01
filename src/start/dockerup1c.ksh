# Dockerup.ksh (1b)

. ./set_env.ksh -e DEV

# python site/my_app/manage.py runserver

docker run  \
    -e MR_CCY_PAIR="EUR/GBP" \
    -e MR_CCY_FREQ=5 \
    -e MR_RABITMQ=${MR_RABITMQ} \
    --name get_eur_gbp \
    markhallett/get_pub_ccy


#docker run -p 5000:5000 \
#        -e MAIL_USERNAME=${GMAIL_USERNAME} \
#        -e MAIL_PASSWORD=${GMAIL_PASSWORD} \
#        -e EGUSER_PASSWORD=${EGUSER_PASSWORD} \
#        -e ADMIN_PASSWORD=${ADMIN_PASSWORD} \
#        -e CCY_PAIR=USDEUR \
#        markhallett/get_ccy_pair
