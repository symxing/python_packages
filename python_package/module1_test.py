import unittest
from python_package.module1 import enlarge

class Test_C_Module(unittest.TestCase):

    def  test_upper(self):
        self.assertEqual(enlarge(5), 500)
        self.assertEqual(enlarge(-5), -500)

if __name__ == '__main__':
    unittest.main()