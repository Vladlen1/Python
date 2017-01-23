__author__ = 'vladbirukov'
from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='prime',
    version='0.1',
    packages=find_packages(),
    long_description=open(join(dirname(__file__),'README.txt')).read(),
    entry_points={
        'console_scripts':
            ['lab2_ModelCreater = ModelCreater.model:main',
             'lab2_cached = cached.mycache:main',
             'lab2_defaultdict = defaultdict.defdict:main',
             'lab2_loger = loger.myloger:main',
             'lab2_metaclass = metaclass.metaclass:main',
             'lab2_myjson = myjson.to_json:main',
             'lab2_myrange = myrange.range:main',
             'lab2_sequnce = sequence.sequnce_filter:main',
             'lab2_singleton = singleton.singleton:main',
             'lab2_vector = vector.vector:main']
    }
)