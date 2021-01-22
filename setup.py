from setuptools import setup, find_packages

VERSION = '0.1.0'
PACKAGE_NAME = 'python_package'
AUTHOR = 'Symone Lewis'
AUTHOR_EMAIL = 'symone.hohensee@gmail.com'
URL = 'https://github.com/symxing/python_packages'

DESCRIPTION = 'Describe your package in one sentence'
with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()
LONG_DESC_TYPE = "text/markdown"

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      url=URL,
      packages=find_packages()
      )