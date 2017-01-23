__author__ = 'vladbirukov'
import random
import unittest

from sequnce.sequence_filter import Sequence_filtration


class TestSequence(unittest.TestCase):
    def setUp(self):
        self.data = [random.randint(1, 20) for _ in range(20)]
        self.seq = Sequence_filtration(self.data)

    def test_filter(self):
        self.assertEqual(list(self.seq.filter(lambda x: x % 2)),
                         list(filter(lambda x: x % 2, self.data)))

        with self.assertRaises(TypeError):
            self.seq.filter(lambda x: x / '2')


if __name__ == '__main__':
    unittest.main()