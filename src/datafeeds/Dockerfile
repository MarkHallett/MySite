FROM python

# RUN apt-get -y update && apt-get install ...

## install Python modules needed by the Python app
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

ENV INI=/ini
ENV LOG=/log

COPY ./send_example_data.py /usr/src

CMD ["python", "/usr/src/send_example_data.py"]
