from setuptools import setup

setup(
    name='tileworld',
    version='1.0.0',
    description='turn-based game',
    install_requires=[
        'zope.interface==5.5.2',
        'more-itertools==9.0.0'
    ],
    entry_points='''
        [console_scripts]
        tileworld=cli:main
    '''
    # for some reason it let me specify the `cli` module without specifying the containing package (src)
)
