from setuptools import setup, find_packages

from my_pip_package import __version__

extra_math = [
    'returns-decorator',
]

extra_bin = [
    *extra_math,
]

extra_test = [
    *extra_math,
    'pytest>=4',
    'pytest-cov>=2',
]
extra_dev = [
    *extra_test,
]

extra_ci = [
    *extra_test,
    'python-coveralls',
]

setup(
    name='my_pip_package',
    version=__version__,

    url='https://github.com/Paramuths/plot_result_package',
    author='Paramuth Samuthrsindh',
    author_email='paramuths@gmail.com',

    packages=find_packages(),

    # dependency installed in general
    install_requires=[
    ],

    # dependency installed with specific keywordd
    extras_require={
        'math': extra_math,

        'bin': extra_bin,

        'test': extra_test,

        'dev': extra_dev,

        'ci': extra_ci,
    },

    entry_points={
        'console_scripts': [
            'add=my_pip_package.math:cmd_add',
        ],
    },
    
)