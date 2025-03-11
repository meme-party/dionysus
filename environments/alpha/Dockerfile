# environments/alpha/Dockerfile

FROM python:3.13-bullseye as base

ARG PORT
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update -qq && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    git \
    curl

# Git 설정: git:// 또는 ssh:// 대신 https:// 사용
RUN git config --global url."https://".insteadOf git:// && \
    git config --global url."https://".insteadOf ssh://git@

# Poetry 설치 및 PATH 설정
RUN curl -sSL https://install.python-poetry.org | python3.13 -
ENV PATH="/root/.local/bin:$PATH"

# 애플리케이션 소스 경로 생성 및 작업 디렉토리 설정
RUN mkdir -p /app/webapp
WORKDIR /app/webapp

COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false && poetry install --no-root

# Django 애플리케이션 코드 복사
COPY ./webapp /app/webapp

# alpha 환경 전용 start script 복사 및 실행 권한 부여
COPY ./environments/alpha/start-webapp.sh /start-webapp.sh
RUN chmod +x /start-webapp.sh

# 정적 파일 수집 - performance 확인 후 적용
# RUN poetry run python manage.py collectstatic --noinput

EXPOSE ${PORT}
