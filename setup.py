from setuptools import setup, find_packages

from stat_result import __version__

dependency = [
    'numpy>=1.22.4',
    'matplotlib>=3.5.3',
    'sklearn>=0.0',
    'einops>=0.6.1'
]

extra_test = [
    *dependency,
    'pytest>=4',
    'pytest-cov>=2',
]

extra_dev = [
    *extra_test,
]

setup(
    name='stat_result',
    version=__version__,

    url='https://github.com/Paramuths/plot_result_package',
    author='Paramuth Samuthrsindh',
    author_email='paramuths@gmail.com',

    packages=find_packages(),

    # dependency installed in general
    install_requires=[
        *dependency
    ],

    # dependency installed with specific keywordd
    extras_require={
        'test': extra_test,
        'dev': extra_dev,
    },
    
)