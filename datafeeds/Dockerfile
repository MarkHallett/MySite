FROM python

# RUN apt-get -y update && apt-get install ...

## install Python modules needed by the Python app
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

VOLUME ./log
VOLUME ./ini

ENV INI=./ini
ENV LOG=./log

COPY ./get_pub_ccy/get_pub_ccy.py /usr/src
COPY ./ini/logging_config.ini ./ini/logging_config.ini

#CMD ["python", "/usr/src/get_pub_ccy.py", "-cGBP/USD"]
CMD ["python", "/usr/src/get_pub_ccy.py"]
