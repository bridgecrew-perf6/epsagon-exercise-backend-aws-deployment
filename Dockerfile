# FROM python:3.8
FROM tiangolo/uwsgi-nginx-flask:python3.8

# RUN apk --update add bash nano

WORKDIR /

COPY . .

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

EXPOSE 80

# CMD ['./entrypoint.sh']
#
# CMD flask run