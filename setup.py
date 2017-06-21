from setuptools import setup, find_packages
from sor import __version__

setup(
    name='sor',
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=['numpy', 'scipy'],
)
