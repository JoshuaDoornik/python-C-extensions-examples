from distutils.core import setup, Extension

setup(name='spammodule.c', version='1.0', ext_modules=[Extension('spam', ['spammodule.c'])])