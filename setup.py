import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="foodpal",
    version="0.0.1",
    author="Ashish Kumar",
    author_email="kumarashish1550@gmail.com",
    description="Description for foodpal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/example-project",
    packages=setuptools.find_packages(),
    install_requires=[
          'requests',
      ],
)
