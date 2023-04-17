FROM alpine:3.17.3

RUN apk add --no-cache python3 py3-pip

RUN pip3 install --no-cache-dir fastapi==0.95.1 uvicorn==0.21.1 redis==4.5.4

EXPOSE 8000

COPY ./src /app

CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0"]