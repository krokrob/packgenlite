from setuptools import setup, find_packages

setup(name='wagon_tools',
      setup_requires=['setuptools_scm'],
      install_requires=['setuptools_scm'],
      use_scm_version={'write_to': 'wagon_tools/version.txt'},
      description="STYCKR tools, python package and more",
      author='Jean Bizot', author_email="jea@gmail.com",
      url='https://styckr.io',
      packages=find_packages(),
      test_suite = 'tests',
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      scripts=['scripts/wagon-make-package'],
      zip_safe=False)
