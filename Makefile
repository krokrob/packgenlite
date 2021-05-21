# ----------------------------------
#          INSTALL & TEST
# ----------------------------------
install:
	@pip install -e .

test:
	@python setup.py test -q

ftest:
	@rm -fr /tmp/ttt; cd /tmp;\
     	packgenlite ttt -d TTT;\
     	cd ttt;\
     	make clean install test;\
     	cd /tmp;\
     	ttt-run;
	@echo 'test_make_pkg made'

clean:
	@rm -fr dist
	@rm -fr build
	@rm -fr packgenlite-*.dist-info
	@rm -fr packgenlite.egg-info
	@rm -fr packgenlite/version.txt
	@find . -name \*.pyc -o -name \*.pyo -o -name __pycache__ -exec rm -rf {} +

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
	packgenlite ttt -d TTT;\
	cd ttt;\
	make clean install test;\
	cd /tmp;\
	ttt-run;\
	)
	@echo '#########################################'
	@echo 'test_make_pkg made'
