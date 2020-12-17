FROM python:3.8
#FROM tiangolo/uwsgi-nginx-flask:python3.8

# RUN apk --update add bash nano

WORKDIR /

COPY ./epsagon_exercise_backend_repo .

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

EXPOSE 80

# CMD ['./entrypoint.sh']
#
 CMD ["python3", "-m", "app.main"]