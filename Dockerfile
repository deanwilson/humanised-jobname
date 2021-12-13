FROM python:3.10.1-alpine

ENV FLASK_APP humanisedflask.py

# if you copy multiple source directories in one COPY it adds all the files to one location
COPY ["bin", "/app/bin"]
COPY ["data", "/app/data"]
COPY ["humanisedflask", "/app/humanisedflask"]
COPY ["lib", "/app/lib"]
COPY ["requirements", "/app/requirements"]

WORKDIR /app

RUN pip install -r requirements/requirements.txt

CMD ["flask", "run", "--host=0.0.0.0"]
