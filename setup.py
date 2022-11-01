from distutils.core import setup, Extension
from Cython.Build import cythonize

exts = (cythonize("orbita_cy.pyx", compiler_directives={'language_level': "3"}))
setup(ext_modules = exts)