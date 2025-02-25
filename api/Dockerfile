FROM python:3.11-slim
RUN apt update && apt install -y docker.io
RUN pip install fastapi uvicorn requests
WORKDIR /app
COPY api.py .
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]