FROM python

# RUN apt-get -y update && apt-get install ...
## install Python modules needed by the Python app
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

VOLUME ./log
VOLUME ./ini

ENV INI=./ini
ENV LOG=./log

EXPOSE 8888

COPY ./rest2web.py /usr/src
#COPY ./show_gbp_usd_test.html /usr/src
COPY ./show_gbp_usd_eur.html /usr/src
COPY ./ini/logging_config.ini ./ini/logging_config.ini

CMD ["python", "/usr/src/rest2web.py"]
