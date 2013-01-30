import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "cc-sdk-py",
    version = "0.0.1",
    author = "Stefano Tranquillini",
    author_email = "stefano.tranquillini@gmail.com",
    description = ("The SDK for python to interact with the Crowd Computer"),
    license = "MIT",
    packages=['ccsdkpy', 'testing'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development",
        "License :: OSI Approved :: MIT License",
    ],
)
