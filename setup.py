from setuptools import setup, find_packages
from typing import List


with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()     
   
__version__ = "0.0.1"  # you can start from 0.0.1

# The actual GitHub repository name (not the folder inside it)
REPO_NAME = "MLOPs-Foundation"

# The Python package name (must match the folder in src/)
# In your case, check inside "src" — if your package folder is "mongodb_connect", then:
PKG_NAME = "mongodb_connect"

# Your GitHub username
AUTHOR_USER_NAME = "AdMub"

# Your email (preferably the one linked to GitHub)
AUTHOR_EMAIL = "admub465@gmail.com"

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Python package for connecting with MongoDB databases.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src")
)