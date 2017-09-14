FROM python

# subscribe 2 api

# RUN apt-get -y update && apt-get install ...

## install Python modules needed by the Python app
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

VOLUME ./log
VOLUME ./ini

EXPOSE 8889

ENV INI=./ini
ENV LOG=./log

COPY ./mq2rest.py /usr/src
COPY ./ini/logging_config.ini ./ini/logging_config.ini

CMD ["python", "/usr/src/mq2rest.py"]
