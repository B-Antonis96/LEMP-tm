FROM ubuntu:jammy

WORKDIR /fastapi

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y python3.10 python3-pip

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./backend/ ./

EXPOSE 8000

CMD [ "python3", "./main.py" ]