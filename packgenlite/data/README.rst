proj
=====================

Install
--------
Check that virtualenv is installed if not::

  $ sudo apt-get install python-virtualenv

Install proj in a virtualenv::

  $ virtualenv ~/venv
  $ source ~/venv/bin/activate
  $ pip install -r requirements.txt
  $ make psi

Check that unittest works::

  $ make test

Check that functionnal test works::

  $ cd /tmp
  $ proj-run
  $ 
