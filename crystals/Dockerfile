
FROM python:3.6.9


WORKDIR /opt/QAProject2

COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT ["/usr/local/bin/python", "app.py"]

COPY . .
