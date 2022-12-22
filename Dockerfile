# Pulls python image (latest)
FROM python:latest

# Adds trusting keys to apt for repos 
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
# Adds google chrome
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
# Updates apt
RUN apt-get -y update
# Installs chrome
RUN apt-get install -y google-chrome-stable

# Downloads chromedriver zipfile
RUN    wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
# Unzips chromedriver files 
RUN    apt-get install -yqq unzip
RUN    unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/ 

# Copies application in a docker image
COPY . .

# Installs requirements
RUN pip install -r requirements.txt

# Runs application
ENTRYPOINT ["python", "scraper.py"]

# Runs indefinitely
CMD tail -f /dev/null