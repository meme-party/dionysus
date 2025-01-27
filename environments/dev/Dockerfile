# Dockerfile
FROM python:3.13-bullseye as base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


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

RUN mkdir -p /app/webapp

WORKDIR /app/webapp

# Poetry 파일 복사 및 의존성 설치
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false && poetry install --no-root

# 애플리케이션 코드 복사
COPY ./webapp /app/webapp

# shell script 복사
COPY ./environments/dev/start-webapp.sh /start-webapp.sh
COPY ./environments/dev/start-migration.sh /start-migration.sh

# 디버깅 출력 (sh 파일 내용)

RUN cat /start-webapp.sh
RUN cat /start-migration.sh


RUN chmod +x /start-webapp.sh
RUN chmod +x /start-migration.sh

EXPOSE ${PORT}
