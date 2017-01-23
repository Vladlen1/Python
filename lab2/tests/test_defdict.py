__author__ = 'vladbirukov'
import unittest
from defaultdict import defdict


class TestDefDict(unittest.TestCase):
    def setUp(self):
        self.dict = defdict.mydefaultdict()
        self.dict["a"][2][1][1][1][1][1] = 5

    def test(self):
        self.assertEqual(self.dict, {'a': {2: {1: {1: {1: {1: {1: 5}}}}}}})
        with self.assertRaises(NameError):
            self.dict["b"] = 21
if __name__ == '__main__':
    unittest.main()