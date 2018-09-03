FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3 python-pip-whl python3-pip build-essential python3-lxml
COPY . /app
WORKDIR /app
RUN ./install.sh
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["app.py"]
