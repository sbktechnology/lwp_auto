from setuptools import setup, find_packages
import os

version = '1.0.0'

setup(
    name='lwp_auto',
    version=version,
    description='Calculate auto lwp',
    author='Indictrans Technologies',
    author_email='lwp@indic.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
