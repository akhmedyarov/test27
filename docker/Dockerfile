FROM python:3.11-slim

COPY requirements.txt requirements.txt
RUN apt-get update -y \
    && apt-get install -y gcc default-libmysqlclient-dev build-essential pkg-config \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

RUN useradd -m -d /proj -s /bin/bash app
COPY . code
WORKDIR /code
RUN chown -R app:app /code/*
USER app

EXPOSE 8000

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
