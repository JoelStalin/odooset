from setuptools import setup, find_packages

setup(
    name='odooset',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'odooset=odooset.main:main',
        ],
    },
)