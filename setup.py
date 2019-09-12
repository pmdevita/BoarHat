from setuptools import setup, find_packages

setup(
    name="BoarHat",
    version="0.2",
    description="A companion library for Pyglet that provides structure and utilties",
    author="pmdevita",
    license="MIT",
    packages=['boarhat'],
    install_requires=[
        'pyglet'
    ]
)