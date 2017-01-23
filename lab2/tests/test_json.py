__author__ = 'vladbirukov'
import unittest
from myjson import to_json
import json


class TestJson(unittest.TestCase):
    def setUp(self):
        self.str1 = [1, 2.2, 3, False, None]
        self.str2 = {1: 'a', 2: 'b', 3: 'c', 4: 'x'}
        self.str3 = {'a': {2: {1: {1: {1: {1: {1: 5}}}}}}, 2: [1, 8]}
        self.x = to_json.Example()

    def test1(self):
        self.assertEqual(to_json.to_json(self.str1), {'1': 'a', '2': 'b', '3': 'c', '4': [1, 2.2, 3, 'false', 'null']})

    def test2(self):
        self.assertEqual(to_json.to_json(self.str2), json.dumps(self.str2))

    def test3(self):
        self.assertEqual(to_json.to_json(self.str3), json.dumps(self.str3))
        with self.assertRaises(to_json.JsonError):
             to_json.to_json(self.x)

if __name__ == '__main__':
    unittest.main()