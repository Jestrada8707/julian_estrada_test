import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Ormuco test library for Jestrada8707",
    version="0.0.1",
    author="Julian Estrada",
    author_email="julian.estrada77@gmail.com",
    description="A this is a small package for Ormuco test",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jestrada8707",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)