from setuptools import setup

from my_pip_package import __version__

setup(
    name='my_pip_package',
    version=__version__,

    url='https://github.com/Paramuths/plot_result_package',
    author='Paramuth Samuthrsindh',
    author_email='paramuths@gmail.com',

    py_modules=['my_pip_package'],
)