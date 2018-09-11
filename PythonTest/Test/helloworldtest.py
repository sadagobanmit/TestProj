import unittest
import sys
sys.path.append("../")
import Common
from Common import _common_strs
import HelloWorld
from HelloWorld import helloworld

class TestHelloWorld(unittest.TestCase):

    def test_add(self):
		print  Common.HelloWorld.TEST
		print _common_strs.TESTSTR
		hw = helloworld.HelloWorldPy()
		assert hw.add(1) == 2
		
if __name__ == '__main__':
    unittest.main()