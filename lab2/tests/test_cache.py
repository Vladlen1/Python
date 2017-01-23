__author__ = 'vladbirukov'

import unittest

from cached import mycache


class Test(unittest.TestCase):
    def test_cache(self):
        self.assertEqual(mycache.myfunc(1, 2), 3)
        with self.assertRaises(TypeError):
            mycache.myfunc('a', 8)

if __name__ == '__main__':
    unittest.main()
