import unittest
from main import myfunc
class Test(unittest.TestCase):
    def test_a_valid_reversed_string(self):
        ret = myfunc('ciao')
        self.assertEqual(ret,'oaic')

    def test_b_empty_string(self):
        ret = myfunc('')
        self.assertEqual(ret,'')

if __name__ == "__main__":
    unittest.main()