FROM python:3.10-slim

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /code
COPY /data ./data
COPY /static ./static
COPY /templates ./templates
COPY functions.py .
COPY app.py .

CMD flask run -h 0.0.0.0 -p 80