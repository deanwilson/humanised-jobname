FROM python:3.7-alpine

ENV FLASK_APP bin/humanised-flask.py

COPY . /app
WORKDIR /app

RUN pip install -r requirements/requirements.txt

CMD ["flask", "run", "--host=0.0.0.0"]
