# media-platform
media-platform

# -Requirements-
python, docker-compose

# -- Useful commands --
# To run the app:
docker-compose build web
docker-compose up web

# Running test:
docker-compose run web make test-execution

# Test Coverage
docker-compose run web make pretty-execution
docker-compose run web make test-coverage
