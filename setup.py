import setuptools
from pathlib import Path

# Read long description from README.md
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Package metadata
__version__ = "0.0.1"  # Update this manually or read from a version file
REPO_NAME = "used_cars_regression"
AUTHOR_USER_NAME = "rimraf-adi"
SRC_REPO = "used_cars_regression"
AUTHOR_EMAIL = "kinjawadeakradi112@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small Python package for an ML app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/rimraf-adi/used_cars_regression",
    project_urls={
        "Bug Tracker": f"https://github.com/rimraf-adi/used_cars_regression/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
