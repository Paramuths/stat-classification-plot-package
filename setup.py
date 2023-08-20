from setuptools import setup, find_packages

from my_pip_package import __version__

setup(
    name='my_pip_package',
    version=__version__,

    url='https://github.com/Paramuths/plot_result_package',
    author='Paramuth Samuthrsindh',
    author_email='paramuths@gmail.com',

    packages=find_packages(),

    install_requires=[
        'returns-decorator',
    ],
)