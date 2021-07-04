from setuptools import setup, find_packages

setup(
    name='metrics_manager',
    version='0.1.0',
    description='Script that collects metrics',
    author='Harpreet Lalwani and Srinivasa Vinay',
    maintainer='Harpreet Lalwani and Srinivasa Vinay',
    entry_points={
        'console_scripts': [
            'metrics_manager = agent:main'
        ]
    },
    packages=find_packages(),
    install_requires=['click','requests'],
    platforms=['macOS', 'linux'],
    keywords=['metrics', 'utility', 'util', 'cli']
)