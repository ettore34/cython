from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize('example_cy.pyx'))
## python3 setup.py build_ext --inplace
##used that line to build it , creates an ".so" file shared object .  