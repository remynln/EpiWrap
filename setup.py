import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="epiwrap",
    version="0.1.1",
    author="Waz0x",
    author_email="remy.noulin@epitech.eu",
    description="A local wrapper for the epitech intranet",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Waz0x/EpiWrap",
    project_urls={
        "Bug Tracker": "https://github.com/Waz0x/EpiWrap/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)