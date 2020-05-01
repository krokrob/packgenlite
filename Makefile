PYPI_USER=lologibus2
# ----------------------------------
#          INSTALL & TEST
# ----------------------------------
install:
	@pip install . -U

test:
	@python setup.py test -q

ftest:
	@rm -fr /tmp/ttt; cd /tmp;\
     	wagon-make-package ttt -d TTT;\
     	cd ttt;\
     	make clean install test;\
     	cd /tmp;\
     	ttt-run;
	@echo 'test_make_pkg made'

clean:
	@rm -fr dist
	@rm -fr build 
	@rm -fr wagon_tools-*.dist-info
	@rm -fr wagon_tools.egg-info
	@rm -fr wagon_tools/version.txt
	@find . -name \*.pyc -o -name \*.pyo -o -name __pycache__ -exec rm -rf {} +


uninstal:
	@python setup.py install --record files.txt
	@cat files.txt | xargs rm -rf
	@rm -f files.txt

python_count_lines:
	@find ./ble -name '*.py' -exec  wc -l {} \; | sort -n| awk \
        '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
	@echo ''
	@find ./tests -name '*.py' -exec  wc -l {} \; | sort -n| awk \
        '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
	@echo ''


test_make_pkg:
	( \
	rm -fr /tmp/ttt; cd /tmp;\
	wagon-make-package ttt -d TTT;\
	cd ttt;\
	make clean install test;\
	cd /tmp;\
	ttt-run;\
	)
	@echo '#########################################'
	@echo 'test_make_pkg made'

# ----------------------------------
#      UPLOAD PACKAGE TO PYPI
# ----------------------------------
build:
	@python setup.py sdist bdist_wheel

pypi_test:
	@twine upload -r testpypi dist/* -u lologibus2

pypi:
	@twine upload dist/* -u lologibus2