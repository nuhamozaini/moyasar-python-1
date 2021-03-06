import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="moyasar",
    version="0.6",
    author="Moyasar",
    author_email="developers@moyasar.com",
    description="Moyasar Python language wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/moyasar/moyasar-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
)
