FROM python:3.12

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

COPY automation/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY automation/ .

EXPOSE 8000

CMD ["python3", "main.py"]