import os
from pathlib import Path
import logging
project_name = "used_cars_regression"
# Setup Logging
log_dir = "logs"
log_file = os.path.join(log_dir, "app.log")
Path(log_dir).mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

# Define project structure
list_of_files = [
    "config/config.yaml",
    "config/schema.yaml",
    "config/params.yaml",
    "data/demo.csv",
    "src/types/__init__.py",
    "src/notebooks/__init__.py",
    "src/notebooks/experiment.ipynb",
    "src/constants/__init__.py",
    "src/utils/__init__.py",
    "src/pipelines/__init__.py",
    "src/components/__init__.py",
    "static/index.html",
    "tests/unit/",
    "tests/integration/",
    "requirements.txt",
    "setup.py",
    "docs/file.tex",
    "README.md",
    ".gitignore"
]

# Project metadata
setup = {
    "repo_name": project_name,
    "author_username": "rimraf-adi",
    "src_repo": project_name,
    "author_email": "kinjawadeakradi112@gmail.com"
}

logging.info("Initiating project setup...")

# Create directories and files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir}")

    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, "w"):
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists.")

# Generate setup.py
setup_py_content = f"""\
import setuptools
from pathlib import Path

# Read long description from README.md
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Package metadata
__version__ = "0.0.1"  # Update this manually or read from a version file
REPO_NAME = "{setup['repo_name']}"
AUTHOR_USER_NAME = "{setup['author_username']}"
SRC_REPO = "{setup['src_repo']}"
AUTHOR_EMAIL = "{setup['author_email']}"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small Python package for an ML app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{setup['author_username']}/{setup['repo_name']}",
    project_urls={{
        "Bug Tracker": f"https://github.com/{setup['author_username']}/{setup['repo_name']}/issues",
    }},
    package_dir={{"": "src"}},
    packages=setuptools.find_packages(where="src"),
)
"""

setup_py_path = Path("setup.py")
with open(setup_py_path, "w", encoding="utf-8") as f:
    f.write(setup_py_content)
logging.info("setup.py file created.")

# Generate requirements.txt
requirements = """\
pandas
notebook
numpy
scikit-learn
matplotlib
python-box==6.0.2
pyYAML
tqdm
ensure==1.0.2
joblib
types-PyYAML
Flask
Flask-Cors
-e .
"""

requirements_path = Path("requirements.txt")
with open(requirements_path, "w", encoding="utf-8") as f:
    f.write(requirements)
logging.info("requirements.txt file created.")

logging.info("✅ Project setup complete!")