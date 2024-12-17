from setuptools import setup, find_packages

# Read the README.md file
with open("README.md", "r") as fh:
    long_description = fh.read()

# Set up the package
setup(
    name="f1-data-parser",
    version="0.0.1",
    author="BetaNow",
    author_email="betanow.dev@gmail.com",
    description="A Python parser for Formula 1 website data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BetaNow/F1DataScraper.git",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        "beautifulsoup4==4.9.3",
        "requests==2.25.1",
    ],
)
