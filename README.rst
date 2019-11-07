STYCKR tools, python package and more
========================================

This package is a meta-package that provide python libs for STYCKR projects
and mainly `wagon-make-package` script.

`wagon-make-package` create a Python package template with all STYCKR tricks in it.

Install `wagon_tools`
-------------------
::

  $ git clone git@gitlab.com:wagon-infra/wagon_tools.git
  $ cd wagon_tools
  $ pip install -r requirements.txt
  $ make clean install


Create a `new_pkg_name` package
---------------------------------

Use `wagon-make-package` to create a new STYCKR python package::

  $ wagon-make-package -n new_pkg_name -d "New project package"
    => New python package new_pkg_name created
  $ cd new_pkg_name/
  $ git init; git add *; git commit -am 'initial commit'
  $ git tag -a 0.42 -m 0.42
  $ make clean psi

Check that unittest work::

  $ make test
  ...running test
  .
  ----------------------------------------------------------------------
  Ran 1 test in 0.176s
  OK
  $

Check that `__version__` is set::

  $ cd /tmp
  $ python -c 'import new_pkg_name; print (new_pkg_name.__version__)'
  0.42
  $

Check that `new_pkg_name` script work::

  $ (venv)styckruser@machine:/tmp$ new_pkg_name-run
  new_pkg_name/data/data.csv.gz Loaded
  ==> out.csv MADE
      shape is (999, 142)
  (venv)styckruser@machine:/tmp$ wc -l out.csv
  1000 out.csv
  (venv)styckruser@machine:/tmp$

Current state of wagon_tools
-------------------------

wagon_tools create a new python package and instantly add this project in our
gitlab if you used the -T arg.

What append when you use -T.

- Add two secret variable to this project  a SSH_PRIVATE_KEY that will allow a
  production deployement on KVM05. And a SECRET_TOKEN that will be used to
  handle dependcies.

We wanted to used the CI_JOB_TOKEN provided by gitlab but this feature is not
yet available for CCE edition.

- Will push an initial commit with all the project and a second with all his
  tags. Test will be executed and the package will be deployed on KVM05. MAybe
  we should add a manual execution for the production install.





