from setuptools import setup, find_packages
from version import find_version

setup(
        name = 'mortgage_forecasts',
        author = 'Jiaxiang Li',
        description = '30-year mortgage rate models',
        license = 'MIT',
        version = find_version('mortgage_forecasts', '__init__.py'),
        packages = find_packages()
     )
