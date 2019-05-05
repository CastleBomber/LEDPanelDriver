'''
    Got much help from the site:
    https://docs.pytest.org/en/latest/getting-started.html
'''

from functions import *
from layer2 import *
from HypnoColors import *
import pytest
import os
#from setting import PROJECT_ROOT
'''
    
    [CS 180]
    Working with pytest
    
    '''

def setup_module(module):
    print ("setup_module      module:%s" % module.__name__)

def teardown_module(module):
    print ("teardown_module   module:%s" % module.__name__)

def setup_function(function):
    print ("setup_function    function:%s" % function.__name__)

def teardown_function(function):
    print ("teardown_function function:%s" % function.__name__)

def test_SetColors():
    #my_HypnoColor = HypnoColors()
    setColors( 1, 2, 3)
    print 'test_SetColors  <============================ actual test code'
    assert (setColors( 1, 2, 3) == 1)

##@pytest.mark.timeout(5)
##def test_ColorsTime():
##    commmand = 'sudo /home/pi/Desktop/HypnoColors.py'
##    os.popen(command)
##    print 'test_ColorsTime <============================ actual test code'
##    pass


class TestSoundVisualizer:
    
    def setup(self):
        print ("setup             class:TestStuff")
    
    def teardown(self):
        print ("teardown          class:TestStuff")
    
    def setup_class(cls):
        print ("setup_class       class:%s" % cls.__name__)
    
    def teardown_class(cls):
        print ("teardown_class    class:%s" % cls.__name__)
    
    def setup_method(self, method):
        print ("setup_method      method:%s" % method.__name__)
    
    def teardown_method(self, method):
        print ("teardown_method   method:%s" % method.__name__)

##    def test_SetColors(self):
##        _red = 0
##        setColors( 1, 2, 3)
##        print 'test_SetColors  <============================ actual test code'
##        assert (_red == 1)
