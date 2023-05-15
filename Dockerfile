FROM python:3.10

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    postgresql-client

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DJANGO_SETTINGS_MODULE LogChainify.settings
ENV PYTHONUNBUFFERED 1

EXPOSE 8001

CMD ["gunicorn", "--bind", "0.0.0.0:8001", "LogChainify.wsgi:application"]
