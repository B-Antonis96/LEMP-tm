FROM python:3.10.6

WORKDIR /fastapi

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./backend/ ./

CMD [ "python", "./main.py" ]