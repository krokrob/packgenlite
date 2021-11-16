# packgenlite - Python package builder

This package is a meta-package that provide python libs for projects
and mainly `packgenlite` script.

`packgenlite` create a Python package template.

## Install `packgenlite`
```bash
pip install git+ssh://git@github.com/krokrob/packgenlite.git
```

## Create a `newpkgname` package

Use `packgenlite` to create a new python package:

```bash
packgenlite newpkgname
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
