# docker_test_pub_ccy.ksh 

echo "Publish $1 $2"

. ./set_env.ksh -e DEV

# python site/my_app/manage.py runserver

docker run \
    -e MR_CCY_PAIR='GBP/USD' \
    -e MR_CCY_FREQ=5 \
    -e MR_RABITMQ=${MR_RABITMQ} \
    markhallett/egtest python "/usr/src/get_pub_ccy.py" "-c" "$1" "-v" "$2"


#docker run -p 5000:5000 \
#        -e MAIL_USERNAME=${GMAIL_USERNAME} \
#        -e MAIL_PASSWORD=${GMAIL_PASSWORD} \
#        -e EGUSER_PASSWORD=${EGUSER_PASSWORD} \
#        -e ADMIN_PASSWORD=${ADMIN_PASSWORD} \
#        -e CCY_PAIR=USDEUR \
#        markhallett/get_ccy_pair
