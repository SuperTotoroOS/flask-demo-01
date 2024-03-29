FROM python:3.7

LABEL maintainer="rickyyoung618@gmail.com" version="1.0"

COPY . /app/flask-demo/

WORKDIR /app/flask-demo

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]