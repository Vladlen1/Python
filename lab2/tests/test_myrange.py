__author__ = 'vladbirukov'
import random
import unittest

from myrange.range import myrange


class TestRange(unittest.TestCase):
    def setUp(self):
        self.start = random.randint(-200, 200)
        self.stop = random.randint(-100, 100)
        self.step = random.randint(-20, 20)

    def test_1(self):
        self.assertEqual(list(myrange(self.start, self.stop, self.step)),
                         list(range(self.start, self.stop, self.step)))

    def test_2(self):
        self.assertEqual(list(reversed(myrange(self.start, self.stop, self.step))),
                         list(reversed(range(self.start, self.stop, self.step))))
        with self.assertRaises(TypeError):
            myrange('1', 12, -1)

if __name__ == '__main__':
    unittest.main()
