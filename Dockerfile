FROM python:3.7
WORKDIR /Project/flask-demo

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["main.py"]