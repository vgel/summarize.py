#!/usr/bin/env python

import summarize

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = open('README.md').read()

setup(
    name='summarize',
    version=summarize.__version__,
    description='A Python utility for summarizing articles using nltk.',
    long_description=readme,
    author='Jonathon Vogel',
    author_email='jonathon.vogel@gmail.com',
    url='https://github.com/Rotten194/summarize.py',
    packages=[
        'summarize',
    ],
    package_dir={'summarize': 'summarize'},
    include_package_data=True,
    install_requires=[
        'nltk>=2.0.4',
        'requests>=1.2.3',
        'beautifulsoup4>=4.3.1',
    ],
    license='BSD',
    scripts=['summarize/summarize.py'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3'
    ],
)
