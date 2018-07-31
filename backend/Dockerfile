FROM python:3.6-slim-stretch
RUN apt-get update -y
RUN apt-get install -y python3 python-pip-whl python3-pip build-essential libxml2
COPY . /app
WORKDIR /app
RUN ./install.sh
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["app.py"]
