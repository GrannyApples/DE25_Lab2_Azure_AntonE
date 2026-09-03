FROM python:3.12-slim
WORKDIR /app

RUN pip install uv

# Copy dependency files first (better caching)
COPY pyproject.toml uv.lock ./
COPY frontend/pyproject.toml frontend/pyproject.toml
# Copy the frontend code (no dataset needed here - it calls the backend for data)
COPY frontend/src frontend/src

# Install deps exactly from lock file, only for the frontend package
RUN uv sync --frozen --package frontend --no-dev



EXPOSE 8501
CMD ["uv", "run", "--package", "frontend", "streamlit", "run", "frontend/src/frontend/main.py", "--server.port=8501", "--server.address=0.0.0.0"]