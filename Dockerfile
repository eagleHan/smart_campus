FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml README.md ./
COPY packages ./packages
COPY services ./services

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -e .

CMD ["python", "-m", "uvicorn", "services.api_gateway.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
