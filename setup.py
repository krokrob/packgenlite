from setuptools import setup, find_packages

setup(name='wagon_tools',
      version="1.0",
      # Below to deal with cleaner versionning
      #setup_requires=['setuptools_scm'],
      #install_requires=['setuptools_scm'],
      use_scm_version={'write_to': 'wagon_tools/version.txt'},
      description="Package builder with CI included",
      url="https://github.com/lologibus2/wagon_tools",
      author='Jean Bizot', author_email="jea@gmail.com",
      packages=find_packages(),
      test_suite='tests',
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      scripts=['scripts/wagon-make-package'],
      zip_safe=False)
