FROM python:3.9.6

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1
WORKDIR /app
ADD ./islamapp .

RUN apt-get update -y 

RUN pip3 install -r requirements.txt

RUN chmod +x start.sh

CMD [ "sh", "start.sh" ]
