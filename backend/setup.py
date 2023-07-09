from setuptools import setup, find_packages

setup(
    name='AITest-App',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask==2.0.2',
        'pymongo==3.12.1',
        'flask_pymongo==2.3.0',
        'pytest==6.2.5',
        'flake8==3.9.2',
        'pylint==2.11.1',
        'black==21.9b0',
    ],
)
