#!/bin/bash

# 테스트 실행 및 커버리지 데이터 수집
docker-compose exec dionysus python -m coverage run manage.py test

# 터미널에 커버리지 리포트 출력
docker-compose exec dionysus python -m coverage report -m

# HTML 형식의 상세 리포트 생성
docker-compose exec dionysus python -m coverage html

echo "Coverage report generated in webapp/htmlcov/ directory"
echo "Open webapp/htmlcov/index.html to view the report"
