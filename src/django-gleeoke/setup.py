from setuptools import setup, find_packages

setup(
    name = "django-gleeoke",
    version = "1.0",
    url = 'https://gleesucks.com',
    license = 'BSD',
    description = "a small app indexing glee karaoke performances",
    author = 'Chris Sinchok',
    packages = find_packages('gleeoke'),
    package_dir = {'django-gleeoke': 'gleeoke'},
    install_requires = ['setuptools'],
)