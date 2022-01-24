import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wowi",
    version="0.1.0",
    author="Det Hsieh",
    author_email="danix914@gmail.com",
    description="Some utils(toys?) for personal development",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/danix914/wowi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.5',
)
