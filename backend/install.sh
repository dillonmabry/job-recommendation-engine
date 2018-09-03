#!/bin/bash
# environment requirements: *nix, python3, pip3
apt-get update -y
apt-get install redis-server -y
pip3 install Flask
pip3 install beautifulsoup4
pip3 install nltk
python3 -c "import nltk; nltk.download('punkt')"
pip3 install lxml
pip3 install rake-nltk
pip3 install python-docx
pip3 install redis
pip3 install celery
pip3 install httpie 
pip3 install flask-cors # For later use with React
pip3 install python-dotenv
