FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY transcripts/ ./transcripts/
COPY main.py .

RUN mkdir -p outputs

CMD ["python", "main.py"]
