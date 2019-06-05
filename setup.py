from setuptools import setup
from os import path
from codecs import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
        name='cachet',
        version='0.1.1',
        url='https://github.com/imlonghao/cachet.python',
        license='MIT',
        author='imlonghao',
        author_email='shield@fastmail.com',
        description='Python client library for the Cachet API',
        long_description=long_description,
        py_modules=['cachet'],
        install_requires=['requests'],
        platforms='any'
)
