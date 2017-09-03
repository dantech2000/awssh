#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages
from pip.req import parse_requirements

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()


pkg_reqs_txt = parse_requirements('./requirements.txt', session='hack')

pkg_reqs = [str(ir.req) for ir in pkg_reqs_txt]

setup_requirements = [
    'pytest-runner',
    # TODO(ibejohn818): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    # TODO: put package test requirements here
]

setup(
    name='awssh',
    version='0.6.0',
    description="SSH Connect to Ec2 instances",
    long_description=readme + '\n\n' + history,
    author="John Hardy",
    author_email='john.hardy@me.com',
    url='https://github.com/ibejohn818/awssh',
    packages=find_packages(include=['awssh']),
    entry_points={
        'console_scripts': [
            'awssh=awssh.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=pkg_reqs,
    license="MIT license",
    zip_safe=False,
    keywords='awssh',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
