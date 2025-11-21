from setuptools import setup

setup(
    name="calculator",
    version="1.0.0",
    description="Calculator",
    long_description="A simple calculator application built in Python.",
    py_modules=["main"],
    entry_points={
        "console_scripts": [
            "calculator = main:main",
        ],
    },
)
