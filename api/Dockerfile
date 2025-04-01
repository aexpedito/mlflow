FROM python:3.12-slim

RUN mkdir /usr/src/app

ENV APP_HOME=/usr/src/app
WORKDIR $APP_HOME

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=main.py

EXPOSE 8081

#CMD ["python", "main.py", "8081"]
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8081", "-w", "2", "main:app"]