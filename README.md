# media-platform
media-platform

# -Requirements-
python, docker-compose

# -- Useful commands --
# To run the app
docker-compose build web
docker-compose up web

# Running test
docker-compose run web make test-execution

# Test Coverage
docker-compose run web make pretty-execution
docker-compose run web make test-coverage

# Endpoints:
/channel/
Ex: /channel/?group_name=YourGroupName
/content/
/content_file/

or take a look at:
http://localhost:8000/

# comments
Hello,
please take into account that I tried to keep this technical exercise as simple as possible.
Feel free to comment or ask anything you feel needs clarification.


