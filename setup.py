import os

from setuptools import setup, find_packages


setup(
    name='flaskplayground',
    packages=find_packages(where='src'),
    package_dir={"": "src"},
    install_requires=["flask", "gunicorn", "redis"],
    description='',
)