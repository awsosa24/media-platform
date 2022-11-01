PROJECT = media-platform


test-execution:
	mkdir -p test/static test/media
	python manage.py migrate
	pytest -v


pretty-coverage:
	mkdir -p coverage/static coverage/media
	python manage.py migrate
	coverage run -m pytest -v
	coverage html


test-coverage:
	mkdir -p coverage/static coverage/media
	python manage.py migrate
	coverage run -m pytest -v
	coverage report -m
