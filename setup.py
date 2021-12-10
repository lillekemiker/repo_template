from distutils.core import setup
from pathlib import Path

import setuptools

REQUIREMENTS_PATH = Path(__file__).parent / "requirements.txt"
PRIVATE_REQUIREMENTS_PATH = Path(__file__).parent / "requirements_private.txt"


def load_requirements(path: Path) -> list:
    with path.open() as f:
        return [
            line.split("#")[0].strip()
            for line in f.read().split("\n")
            if line.split("#")[0].strip()
        ]


requirements = load_requirements(REQUIREMENTS_PATH)

if PRIVATE_REQUIREMENTS_PATH.exists():
    requirements = load_requirements(PRIVATE_REQUIREMENTS_PATH)


with open("README.md") as f:
    long_description = f.read()


setup(
    name="{{REPO_NAME}}",
    version="0.0.0",
    author="{{GIT_USER_NAME}}",
    author_email="{{GIT_USER_EMAIL}}",
    url="https://github.com/{{REPO_OWNER}}/{{REPO_NAME}}",
    packages=setuptools.find_packages(exclude=["tests"]),
    package_data={"": ["py.typed"]},
    include_package_data=True,
    description=long_description.split("\n", 1)[0],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
