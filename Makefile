clean:
	@rm -fr dist
	@rm -fr build 
	@rm -fr stkr_tools-*.dist-info
	@rm -fr stkr_tools.egg-info
	@rm -fr stkr_tools/version.txt
	@find . -name \*.pyc -o -name \*.pyo -o -name __pycache__ -exec rm -rf {} +

install:
	@pip install . -U

test:
	@python setup.py test -q

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
	stkr-make-package ttt -d TTT;\
	cd ttt;\
	make check_code clean install test;\
	make ftest;\
	make wheel;\
	cd /tmp;\
	ttt-run;\
	)
	@echo '#########################################'
	@echo 'test_make_pkg made'
