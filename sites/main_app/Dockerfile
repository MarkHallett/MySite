FROM tiangolo/uwsgi-nginx-flask:flask

MAINTAINER dev "dev@eg.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install --upgrade pip
RUN pip install gunicorn

COPY app_main .

ADD app_main/requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["manage.py", "runserver", "-h", "0.0.0.0" ]
