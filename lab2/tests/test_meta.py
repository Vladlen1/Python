__author__ = 'vladbirukov'
import unittest
from metaclass import metaclass


class TestMetaclass(unittest.TestCase):
    def test(self):
        x = metaclass.mymeta('CustomClass', (), {}, 'test1.txt')
        self.assertEqual([x.a, x.b, x.c], [1, 'test', {1: 2}])
        with self.assertRaises(AttributeError):
            x.g

if __name__ == '__main__':
    unittest.main()