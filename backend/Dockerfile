FROM python:3.12-slim
WORKDIR /app

RUN pip install uv

# Copy dependency files first (better caching)
#Most of this code is just taken from a different repo and just changed to fit this repo
COPY pyproject.toml uv.lock ./
COPY backend/pyproject.toml backend/pyproject.toml

COPY backend/src backend/src
# Install deps exactly from lock file, only for the backend package
RUN uv sync --frozen --package backend --no-dev

# Dataset backend serves
COPY data data

EXPOSE 8000
CMD ["uv", "run", "--package", "backend", "uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]