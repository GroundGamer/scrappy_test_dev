from setuptools import setup, find_packages
from os.path import join, dirname


setup(
    name='scrappy',
    version='1.0.0',
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    packages=find_packages(),
    install_requires=(
            'attrs==19.3.0',
            'Automat==20.2.0',
            'cffi==1.14.0',
            'constantly==15.1.0',
            'cryptography==2.8',
            'cssselect==1.1.0',
            'hyperlink==19.0.0',
            'idna==2.9',
            'incremental==17.5.0',
            'items==0.6.5',
            'lxml==4.5.0',
            'nulltype==2.3.1',
            'parsel==1.5.2',
            'Protego==0.1.16',
            'pyasn1==0.4.8',
            'pyasn1-modules==0.2.8',
            'pycparser==2.20',
            'PyDispatcher==2.0.5',
            'PyHamcrest==2.0.2',
            'pyOpenSSL==19.1.0',
            'queuelib==1.5.0',
            'Scrapy==2.0.1',
            'service-identity==18.1.0',
            'six==1.14.0',
            'Twisted==20.3.0',
            'w3lib==1.21.0',
            'zope.interface==5.0.1'
    ),
)