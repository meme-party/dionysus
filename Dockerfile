# Dockerfile
ARG DISTRO_NAME
ARG PYTHON_VERSION

FROM python:${PYTHON_VERSION}-${DISTRO_NAME} as base

RUN apt-get update -qq && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    git \
    curl

# Git configuration
RUN git config --global url."https://".insteadOf git:// && \
    git config --global url."https://".insteadOf ssh://git@

# Poetry 설치
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

RUN mkdir -p /dionysus

WORKDIR /dionysus

# Poetry 파일 복사 및 의존성 설치
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false && poetry install --no-root

# 애플리케이션 코드 복사
COPY ./app /dionysus/app

EXPOSE 8000
