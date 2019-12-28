#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from os.path import dirname, abspath, join
from json import load

ROOT = dirname(abspath(__file__))

with open(join(ROOT, 'tkcrud/config/config.json')) as f:
    config_json = load(f)

with open('README.rst') as f:
    long_description = f.read()

requirements = join(ROOT, 'requirements.txt')

with open(requirements) as f:
    install_requires = [i.strip().split('#', 1)[0].strip()
                        for i in f.read().strip().split('\n')]

requirements_dev = join(ROOT, 'requirements-dev.txt')
extras_require = {}
with open(requirements_dev) as f:
    extras_require['dev'] = [i.strip().split('#', 1)[0].strip()
                             for i in f.read().strip().split('\n')]


# NOTE: Some setup information is contained in the config/config.json file.
setup(
    name=f'{config_json["Setup"]["app_name"].lower()}',
    version=f'{config_json["Setup"]["app_version"]}',
    description=f'{config_json["Setup"]["app_description"]}',
    author=f'{config_json["Setup"]["author"]["name"]}',
    author_email=f'{config_json["Setup"]["author"]["email"]}',
    license=f'{config_json["Setup"]["app_license"]}',
    maintainer=f'{config_json["Setup"]["author"]["name"]}',
    # long_description_content_type='text/markdown',
    long_description=long_description,
    url=f'{config_json["Setup"]["app_url"]}',
    packages=find_packages(),
    platforms=f'{config_json["Setup"]["platforms"]}',
    install_requires=install_requires,
    extras_require=extras_require,
    classifiers=config_json["Setup"]["app_classifiers"],
    python_requires=f'{config_json["Setup"]["python_requires"]}',
    keywords=f'{config_json["Setup"]["keywords"]}',
    entry_points={'console_scripts': config_json["Setup"]["console_scripts"]},
    package_data=config_json["Setup"]["package_data"],
    include_package_data=config_json["Setup"]["include_package_data"],
)
