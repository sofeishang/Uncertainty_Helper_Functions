from setuptools import setup, find_packages

setup(
    name="helper_functions",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib",
        "seaborn",
        "scipy",
        "pandas"
    ],
    author="Sophie",
    description="A package for circular data handling, plotting, and utilities.",
    long_description=open("README.md").read() if "README.md" in open("README.md", "r").read() else "",
    long_description_content_type="text/markdown",
    url="https://github.com/sofeishang/Uncertainty_Helper_Functions",  # Update with 
)