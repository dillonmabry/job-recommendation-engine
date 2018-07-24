FROM python:3.6-slim-stretch
RUN apt-get update -y
RUN apt-get install -y python3 python-pip-whl python3-pip build-essential libxml2
RUN ./install.sh
COPY . /app
WORKDIR /app
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["app.py"]
