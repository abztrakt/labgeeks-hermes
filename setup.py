from setuptools import setup

setup(
    name = 'labgeeks-hermes',
    version = '1.0',
    license = 'Apache',
    url = 'http://github.com/abztrakt/labgeeks_hermes',
    description = 'The dashboard app for the labgeeks student staff management tool suite.',
    author = 'Craig Stimmel',
    packages = ['labgeeks_hermes',],
    install_requires = [
        'setuptools',
        'South==0.7.3',
    ],
)
