# WAGON tools - Python package builder

This package is a meta-package that provide python libs for projects
and mainly `wagon-make-package` script.

`wagon-make-package` create a Python package template.

## Install `wagon_tools`
```bash
pip install git+https://github.com/krokrob/wagon_tools.git
```

## Create a `newpkgname` package

Use `wagon-make-package` to create a new python package:

```bash
wagon-make-package newpkgname
```

Check that the package has been created:

```bash
cd newpkgname
tree
.
├── MANIFEST.in
├── Makefile
├── README.md
├── newpkgname
│   ├── __init__.py
│   └── data
├── notebooks
├── raw_data
├── requirements.txt
├── scripts
│   └── newpkgname-run
├── setup.py
└── tests
    └── __init__.py

6 directories, 8 files
```
