FROM python:3.10-slim

WORKDIR /server

RUN apt-get update && apt-get install -y \
    libpq-dev gcc && \
    apt-get clean

COPY requirements.txt /server
RUN pip install --no-cache-dir -r requirements.txt

COPY . /server

EXPOSE 5000

CMD ["python", "run_app.py"]
