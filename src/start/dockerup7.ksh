# Dockerup7.ksh

. ./set_env.ksh -e DEV

docker run -p 5000:5000 \
    -e MAIL_USERNAME=${GMAIL_USERNAME} \
    -e MAIL_PASSWORD=${GMAIL_PASSWORD} \
    -e EGUSER_PASSWORD=${EGUSER_PASSWORD} \
    -e ADMIN_PASSWORD=${ADMIN_PASSWORD} \
    markhallett/app
