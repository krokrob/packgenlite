clean:
	@rm -f */version.txt
	@rm -f .coverage
	@rm -fr */__pycache__
	@rm -fr __pycache__
	@rm -fr build
	@rm -fr dist
	@rm -fr proj-*.dist-info
	@rm -fr proj.egg-info
	@rm -fr */*.pyc

all: clean install test check_code

install:
	@pip install . -U

install_requirements:
	@pip install -r requirements.txt

check_code:
	@flake8 scripts/* proj/*.py

test:
	@coverage run -m unittest tests/*.py
	@coverage report -m --omit=$(VIRTUAL_ENV)/lib/python*

ftest:
	@Write me

uninstal:
	@python setup.py install --record files.txt
	@cat files.txt | xargs rm -rf
	@rm -f files.txt

count_lines:
	@find ./ -name '*.py' -exec  wc -l {} \; | sort -n| awk \
        '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
	@echo ''
	@find ./scripts -name '*-*' -exec  wc -l {} \; | sort -n| awk \
		        '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
	@echo ''
	@find ./tests -name '*.py' -exec  wc -l {} \; | sort -n| awk \
        '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
	@echo ''
