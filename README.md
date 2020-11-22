# WAGON tools - Python package builder

This package is a meta-package that provide python libs for projects
and mainly `wagon-make-package` script.

`wagon-make-package` create a Python package template.

## Install `wagon_tools`
```bash
pip install git+https://github.com/krokrob/wagon_tools.git
```

## Create a `new_pkg_name` package

Use `wagon-make-package` to create a new python package:
```bash
  $ wagon-make-package -n new_pkg_name -d "New project package"
    => New python package new_pkg_name created
  $ cd new_pkg_name/
  $ git init; git add *; git commit -am 'initial commit'
  $ git tag -a 0.42 -m 0.42
  $ make clean
```
