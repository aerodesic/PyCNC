from DistUtilsExtra.auto import setup
from distutils.command.install import install

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
    packages          = [ "cnc", "tests" ],
    author            = "Nikolay Khabarov",
    author_email      = "2xl@mail.ru",
    description       = "CNC machine controller",
    long_description  = long_description,
    license           = "MIT"
    keywords          = "CNC 3D printer robot raspberry pi",
    url               = "https://github.com/Nikolay-Kha/PyCNC",
    packages          = [ "rhprocntl" ],
    cmdclass          = { 'install': post_install },
)
