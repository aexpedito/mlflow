FROM python:3.12-slim

RUN mkdir /usr/src/app

ENV APP_HOME=/usr/src/app
WORKDIR $APP_HOME

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8081

CMD ["python", "main.py", "8081"]
