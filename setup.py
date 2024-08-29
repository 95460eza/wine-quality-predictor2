# minimal informations about your project (package name, author, version, dependencies needed BY this package)
import setuptools
from distutils.util import convert_path


main_ns = {}
# converts the relative path 'wqp/__init__.py' into an absolute path
ver_path = convert_path('wqp/__init__.py')


with open(ver_path) as ver_file:
    # ver_file.read() reads the entire content of the file as a string.
    # exec() is a built-in Python function that executes the code found in wqp/__init__.py.
    # Any variables, functions, or classes defined in wqp/__init__.py will be placed into the main_ns dictionary
    exec(ver_file.read(), main_ns)


setuptools.setup(
    name='wqp',
    # IF YOU PLACE IN __init__.py the line "__version__='1.0.0'", it will go in dictionary main_ns as key = "version"
    version=main_ns['__version__'],
    author='my_email@email.com',
    description='Wine quality predictor - a packaged machine learning algorithm to predict wine quality',
    packages=setuptools.find_packages(),
    install_requires=[
        "scikit-learn>=1",
        "pandas>=2",
        "click>=7.0"
        ],        
    
    # "entry_points" IN setup.py specifies entry points for various COMMANDS OR PLUG INS
    # "console_scripts" specifies that the entry points are for creating command-line scripts that should be installed in the user's environment.
    # ''' are used here to denote a multi-line string
    entry_points='''
    [console_scripts]
    # wqp: IS the NAME of the command-line SCRIPT installed with the package and will be available in USERS' PATH.
    # when the wqp command IN CLI is run, THE FUNCTION CALLED wqp IN wqp.cli WILL be executed
    wqp=wqp.cli:cli
    '''
    
)