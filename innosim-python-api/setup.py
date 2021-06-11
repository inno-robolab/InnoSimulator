#!/usr/bin/env python3

from setuptools import setup

setup(
    name="innosim",
    description="Inno Simulator Api",
    author="innosim",
    python_requires=">=3.5.0",
    url="https://github.com/inno-robolab/InnoSimulator",
    packages=["innosim"],
    install_requires=["websockets==9.1"],
    license="Other",
    classifiers=[
        "License :: Other/Proprietary License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
    ],
)
