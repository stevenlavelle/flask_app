import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flask_app",
    version="0.0.1",
    author="Steven Lavelle",
    author_email="stevenlavelle@gmail.com",
    description="Set up a flask application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stevenlavelle/flask_app",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)