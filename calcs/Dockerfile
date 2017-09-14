FROM python
# Docker file for calcs

# RUN apt-get -y update && apt-get install ...

## install Python modules needed by the Python app
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

VOLUME ./log
VOLUME ./ini

ENV INI=./ini
ENV LOG=./log

COPY ./calc_gbp_usd_eur/calc_gbp_usd_eur.py /usr/src
COPY ./calc_gbp_usd_eur/gbp_usd_eur_dag.py /usr/src
COPY ./calc_gbp_usd_eur/dag.py /usr/src
COPY ./calc_gbp_usd_eur/publish.py /usr/src 



COPY ./ini/logging_config.ini ./ini/logging_config.ini

CMD ["python", "/usr/src/calc_gbp_usd_eur.py"]
