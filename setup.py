"""stac-fastapi-locust setup.py
"""
from setuptools import setup, find_packages

__version__ = "0.1.0"

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="stac_locust",
    version=__version__,
    description="Load balancing for stac compliant api",
    url="https://github.com/jonhealy1/stac-fastapi-locust",
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=[
        "click>=7.1.2",
        "locust",
        "setuptools",
        "Cython",
        "bzt",
    ],
    entry_points={
        'console_scripts': ['stac-locust=stac_locust_cli.cli:main']
    },
    author="Jonathan Healy",
    author_email="jonathan.d.healy@gmail.com",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.7",
    tests_require=["pytest"]
)