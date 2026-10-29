FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# Dependencies are baked in from the manifest; app source is bind-mounted by
# docker-compose.base44.yml so edits are picked up by Streamlit's rerun loop.
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
