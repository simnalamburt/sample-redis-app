FROM python:3.8
LABEL Description="Sample web server using Redis to test Nomad"

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .
COPY templates templates

CMD flask run
