from setuptools import setup, find_packages

# Load existing README.rst for long description
with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='pyhealthz',
    version='0.1.0',
    description='HTTP Server for System Resource Usage Data',
    long_description=readme,
    author='John Barber',
    author_email='jsbarber@gmail.com',
    install_requires=['psutil'],
    # Will recursively look through given dir for __init__.py to indicate req'd pkgs
    packages=find_packages('src'),
    package_dir={'':'src'},
    entry_points={
        'console_scripts': [
            'pyhealthz = pyhealthz.web:main',
            ]
    }
)
