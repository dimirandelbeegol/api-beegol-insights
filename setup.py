"""Python setup.py for api_beegol_insights package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("api_beegol_insights", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="api_beegol_insights",
    version=read("api_beegol_insights", "VERSION"),
    description="Awesome api_beegol_insights created by dimirandelbeegol",
    url="https://github.com/dimirandelbeegol/api-beegol-insights/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="dimirandelbeegol",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["api_beegol_insights = api_beegol_insights.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
