FROM python:3.10-slim-buster

# Create app directory
WORKDIR /docker-app

# Install app dependencies
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

# Bundle app source
COPY . .

CMD [ "flask", "run","--host","0.0.0.0"]