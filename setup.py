from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_deescription = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup (    
    name="image_processing",
    version = "0.0.1",
    author = "Vitoria",
    description="image Processing Package using Skimage",
    long_description= page_deescription,
    long_description_content_type="text/markdown",
    url="https://github.com/CherryFoxy/Processando-image",
    packages = find_packages(),
    install_requires = requirements,
    python_requires = '>=3.5',   
)
  