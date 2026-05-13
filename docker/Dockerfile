FROM python:3.13-slim

WORKDIR /app

COPY src/requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY src/ .

EXPOSE 5000

CMD ["python", "app.py"]