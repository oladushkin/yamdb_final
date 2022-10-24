FROM python:3.7-slim

WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt --no-cache-dir
COPY . .
COPY static/redoc.yaml /app/static/redoc.yaml

CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]