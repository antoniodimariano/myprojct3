import unittest
from main import myfunc
class Test(unittest.TestCase):
    def test_a_valid_reversed_string(self):
        ret = myfunc('ciao')
        self.assertEqual(ret,'oaic')

    def test_b_empty_string(self):
        ret = myfunc('')
        self.assertEqual(ret,'')

    def test_c_empty_string(self):
        ret = myfunc(111)
        self.assertEqual(ret,False)

    def test_d_empty_string(self):
        ret = myfunc('oaic')
        self.assertEqual(ret,'ciao')


if __name__ == "__main__":
    unittest.main() #pragma no cover