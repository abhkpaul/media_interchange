"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['sparksnow.py']
OPTIONS = {}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)