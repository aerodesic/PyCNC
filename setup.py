from DistUtilsExtra.auto import setup
from distutils.command.install import install
from setuptools import find_packages
import os

# In case we need hooks
class post_install(install):
    def run(self):
        install.run(self)

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()


setup(
    name              = "pycnc",
    version           = "1.1.0",
    packages          = [ os.path.join('pycnc', x) for x in find_packages('pycnc') ],
    author            = "Nikolay Khabarov",
    author_email      = "2xl@mail.ru",
    description       = "CNC machine controller",
    long_description  = long_description,
    license           = "MIT",
    keywords          = "CNC 3D printer robot raspberry pi",
    url               = "https://github.com/Nikolay-Kha/PyCNC",
    cmdclass          = { 'install': post_install },
    data_files        = [('/usr/sbin', ['pycnc/pycnc', 'pycnc/runtests.sh' ])],
)
