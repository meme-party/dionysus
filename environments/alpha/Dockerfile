# environments/alpha/Dockerfile - with improved layer caching

FROM python:3.13-bullseye as python-base

ARG PORT=8000
ENV PORT=${PORT}
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Setup Poetry
ENV POETRY_HOME="/opt/poetry"
ENV POETRY_NO_INTERACTION=1
ENV POETRY_VIRTUALENVS_CREATE=false
ENV PATH="$POETRY_HOME/bin:$PATH"

FROM python-base as builder-base
RUN apt-get update -qq && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    git \
    curl

RUN git config --global url."https://".insteadOf git:// && \
    git config --global url."https://".insteadOf ssh://git@

FROM builder-base as poetry-base
RUN curl -sSL https://install.python-poetry.org | python3.13 -

FROM poetry-base as poetry-deps
WORKDIR /app

COPY pyproject.toml poetry.lock* ./
RUN poetry install --no-root

FROM poetry-deps as final
# Copy application code
COPY ./webapp /app/webapp
WORKDIR /app/webapp

COPY ./environments/alpha/start-webapp.sh /start-webapp.sh
RUN chmod +x /start-webapp.sh

EXPOSE ${PORT}
ENTRYPOINT ["/start-webapp.sh"]
