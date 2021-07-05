from setuptools import setup, find_packages

setup(
    name='mm-server',
    version='0.1.0',
    description='Script that collects metrics',
    author='Harpreet Lalwani and Srinivasa Vinay',
    maintainer='Harpreet Lalwani and Srinivasa Vinay',
    entry_points={
        'console_scripts': [
            'mm-server = master:main'
        ]
    },
    packages=find_packages(),
    install_requires=['flask'],
    platforms=['macOS', 'linux'],
    keywords=['metrics', 'utility', 'util', 'cli']
)