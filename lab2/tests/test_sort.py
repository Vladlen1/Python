__author__ = 'vladbirukov'
import unittest

from BigData import sort as sort_merge


class Test(unittest.TestCase):
    def setUp(self):
        sort_merge.create_file(filename='big_data_create.txt',
                               strings_count=10000, fields_count=5,
                               numeric_fields=(1, 3, 5))

    def test_sort(self):
        sort_merge.sort(filename='big_data_create.txt',
                        output_filename='big_data_sorted.txt')
        self.assertTrue(sort_merge.sort(filename='big_data_create.txt',
                                        output_filename='big_data_sorted.txt',
                                        check=True))

        with self.assertRaises(sort_merge.BufferMemoryError):
            sort_merge.sort(filename='big_data_create.txt',
                            output_filename='big_data_sorted.txt', buf_size=10)

if __name__ == '__main__':
    unittest.main()
