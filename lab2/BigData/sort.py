__author__ = 'vladbirukov'
import tempfile
import os
import string
from threading import Thread
import random
import argparse


def merge_func(arr, key, reverse):
    if len(arr) > 1:
        mid = len(arr) // 2
        p1 = arr[: mid]
        p2 = arr[mid:]
        merge_func(p1, key, reverse)
        merge_func(p2, key, reverse)
        i1, i2, i = 0, 0, 0
        while (i1 < len(p1)) & (i2 < len(p2)):
            if not reverse:
                if key(p1[i1]) < key(p2[i2]):
                    arr[i] = p1[i1]
                    i1 += 1
                else:
                    arr[i] = p2[i2]
                    i2 += 1
            else:
                if key(p1[i1]) > key(p2[i2]):
                    arr[i] = p1[i1]
                    i1 += 1
                else:
                    arr[i] = p2[i2]
                    i2 += 1
            i += 1
        while i1 < len(p1):
            arr[i] = p1[i1]
            i, i1 = i+1, i1+1
        while i2 < len(p2):
            arr[i] = p2[i2]
            i, i2 = i+1, i2+1


def merge_sort(arr, key, reverse):
    merge_func(arr, key, reverse)
    return arr


class BufferMemoryError(MemoryError):
    def __str__(self):
        return "Too small buffer size for sorting!"


def sort(filename, output_filename, have_numbers=False, sort_fields=(-1,),
         reverse=False, fields_sep='\t', strings_sep='\n',
         buf_size=1024 * 1024, check=False):
    if check:
        output_file = None
        input_file = open(output_filename, 'r')
        files_count = os.path.getsize(output_filename) // buf_size
    else:
        output_file = open(output_filename, 'w')
        input_file = open(filename, 'r')
        files_count = os.path.getsize(filename) // buf_size

    files = []

    if os.path.getsize(filename) % buf_size != 0:
        files_count += 1

    data = ''
    for i in range(files_count):
        files.append(tempfile.NamedTemporaryFile('a', delete=True))
        data, data_to_next = reader(data, input_file, buf_size,
                                    strings_sep, buf_size, output_filename)
        strings = decoding(data, strings_sep, fields_sep, have_numbers)
        data = data_to_next

        if check:
            for str_i in range(len(strings) - 1):
                if key(strings[str_i], sort_fields) <= \
                        key(strings[str_i + 1], sort_fields):
                    if reverse:
                        print(False)
                        return False
                else:
                    if not reverse:
                        print(False)
                        return False
        else:
            strings = merge_sort(strings, key=lambda x:
                                 key(x, sort_fields), reverse=reverse)

            for string_ in strings:
                files[i].write(fields_sep.join(string_) + strings_sep)
            if os.path.getsize(files[i].name) == 0:
                print('Maybe error')
            files[i] = open(files[i].name, 'r')

    if check:
        print(True)
        return True

    sectors_count = files_count + 1
    merge_buffer = buf_size // sectors_count

    data = ['' for _ in range(sectors_count)]
    strings = [None for _ in range(sectors_count)]
    data_to_next = ['' for _ in range(files_count)]
    iter_ = [None for _ in range(files_count)]

    for i in range(files_count):
        data[i], data_to_next[i] = reader(data[i], files[i], merge_buffer,
                                          strings_sep, buf_size, output_filename)
        strings[i] = decoding(data[i], strings_sep, fields_sep, have_numbers)
        data[i] = data_to_next[i]
        iter_[i] = iter(strings[i])

    have_strings = set(range(files_count))
    cur_strings = {i: next(iter_[i]) for i in have_strings}
    while have_strings:
        if reverse:
            cur_index = max(cur_strings,
                            key=lambda x: key(cur_strings[x], sort_fields))
        else:
            cur_index = min(cur_strings,
                            key=lambda x: key(cur_strings[x], sort_fields))

        data[sectors_count - 1] += fields_sep.join(cur_strings[cur_index]) + \
                                   strings_sep
        try:
            cur_strings[cur_index] = next(iter_[cur_index])
        except:
            data[cur_index], data_to_next[cur_index] = \
                reader(data[cur_index], files[cur_index], merge_buffer,
                       strings_sep, buf_size, output_filename)
            if data[cur_index] != '':
                strings[cur_index] = decoding(data[cur_index], strings_sep,
                                              fields_sep, have_numbers)
                data[cur_index] = data_to_next[cur_index]
                iter_[cur_index] = iter(strings[cur_index])
                cur_strings[cur_index] = next(iter_[cur_index])
            else:
                have_strings -= {cur_index}
                cur_strings.pop(cur_index)

        if len(data[sectors_count - 1]) > merge_buffer:
            output_file.write(data[sectors_count - 1])
            data[sectors_count - 1] = ''

    output_file.write(data[sectors_count - 1])
    data[sectors_count - 1] = ''


def key(data_fields, sort_fields):
    if sort_fields == (-1,):
        return data_fields
    else:
        cur_sort_fields = (set(sort_fields) &
                           set(range(1, len(data_fields) + 1)))
        sorting_fields = [data_fields[field - 1] for field in cur_sort_fields]
        return sorting_fields


def reader(data, filename, size, strings_sep, buf_size, output_filename):
    data += filename.read(size)
    data_to_next = ''
    if data[-len(strings_sep):] != strings_sep:
        if data != '' and data.rfind(strings_sep) == -1:
            if size == buf_size:
                os.remove(output_filename)
            raise BufferMemoryError
        data_to_next = data[data.rfind(strings_sep) + 1:]
        data = data[:data.rfind(strings_sep)]
    return data, data_to_next


def decoding(data, strings_sep, fields_sep, have_numbers):
    strings = data.split(sep=strings_sep)
    strings = strings[:-1] if strings[-1] == '' else strings
    strings = [string_.split(sep=fields_sep) for string_ in strings]
    if have_numbers:
        new_strings = []
        for string_ in strings:
            if (set(string_) & set(string.digits)) != set():
                string_ = int(string_)
            new_strings.append(string_)
        strings = new_strings
    return strings


def create_file(filename='non_sorted.txt', strings_count=100,
                fields_count=-1, fields_len=4, numeric_fields=(-1,),
                fields_sep='\t', strings_sep='\n'):
    letters = list(string.ascii_letters)
    digits = list(string.digits)
    thread_count = 10

    thr = None
    with open(filename, 'w+') as f:
        f.write("")

    def wrt(data_arr):
        for data in data_arr:
            with open(filename, 'a') as f:
                f.write(data)

    for cur_thread in range(thread_count):
        data_arr = []
        for cur_line in range(strings_count // thread_count):
            line = ''
            if fields_count == -1:
                fields_count_cur = random.randint(3, 7)
            else:
                fields_count_cur = fields_count

            for cur_field in range(1, fields_count_cur + 1):
                char_set = digits if cur_field in numeric_fields else letters
                field = ''
                for cur_char in range(fields_len):
                    field += random.choice(char_set)
                field += fields_sep
                line += field
            line = line[:-1] + strings_sep
            data_arr.append(line)

        if thr and thr.isAlive():
            thr.join()

        thr = Thread(target=wrt, args=(data_arr,))
        thr.start()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('function', choices=['create', 'sort'])
    parser.add_argument('input', action='store')

    # create
    parser.add_argument('--line-separator', type=str,
                        action='store', default='\n')
    parser.add_argument('-t', '--field-separator', type=str,
                        action='store', default='\t')
    parser.add_argument('-n', '--numeric', type=int,
                        nargs='+', action='store', default=(-1,))
    parser.add_argument('--lines-count', type=int,
                        action='store', default=20000)
    parser.add_argument('--fields-count', type=int,
                        action='store', default=-1)

    # sort
    parser.add_argument('--output', action='store')
    parser.add_argument('-k', '--key', type=int,
                        nargs='+', action='store', default=(-1,))
    parser.add_argument('--have-numbers', type=bool,
                        action='store', default=False)
    parser.add_argument('--reverse', type=bool,
                        action='store', default=False)
    parser.add_argument('--check', action='store_true', default=False)
    parser.add_argument('--buffer-size', type=int,
                        action='store', default=1024*1024)

    nsp = parser.parse_args()

    if nsp.function == 'create':
        create_file(filename=nsp.input, strings_sep=nsp.line_separator,
                    fields_sep=nsp.field_separator, numeric_fields=nsp.numeric,
                    strings_count=nsp.lines_count, fields_count=nsp.fields_count)
    else:
        sort(filename=nsp.input, output_filename=nsp.output, sort_fields=nsp.key,
             have_numbers=nsp.have_numbers, reverse=nsp.reverse,
             check=nsp.check, buf_size=nsp.buffer_size)

if __name__ == '__main__':
    main()
