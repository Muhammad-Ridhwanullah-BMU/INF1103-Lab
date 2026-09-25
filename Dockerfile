FROM python:3.11-slim
WORKDIR /app
COPY persistant_auditor.py .
CMD ["python", "persistant_auditor.py"]