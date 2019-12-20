import sys, requests
from setuptools import setup, find_packages

with open('README.md', 'r') as file:
    long_description = file.read()


requirements = []
with open('requirements.txt', 'r') as reqs:
    for x in reqs.readlines():
        requirements.append(x.replace('\n', '').replace('\r', ''))
setup(
    name='repl-from-cli',
    version='1.0.1',
    author='Max Bridgland',
    author_email='mabridgland@protonmail.com',
    description='Generate GitHub and Repl.it Repos with One Command',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/M4cs/BabySploit',
    packages=find_packages(),
    install_requires=requirements,
    project_urls={
        'Discord Server': 'https://discord.gg/C7jgQeN'
    },
    zip_safe=True,
    entry_points={
        'console_scripts':[
            'repl-from-cli = repl_from_cli.__main__:main',
        ],
    },
    classifiers=[  # Used by PyPI to classify the project and make it searchable
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',

        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: IronPython',
        'Programming Language :: Python :: Implementation :: Jython',

        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',

        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Systems Administration',
        'Topic :: System :: Networking',
        'Topic :: Utilities',
    ]
)
