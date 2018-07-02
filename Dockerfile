FROM python:2

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY app_server.sh ./

RUN pip install --no-cache-dir -r requirements.txt

RUN ls /usr/src/app
RUN chmod +x app_server.sh
