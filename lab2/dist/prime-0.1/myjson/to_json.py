__author__ = 'vladbirukov'
import json


class JsonError(TypeError):
    def __init__(self, obj):
        self.obj = obj

    def __str__(self):
        return 'Type ' + str(self.obj) + 'can not be converted to json'


def to_json(obj, raise_unknown=False):
    obj_type = type(obj)
    if obj_type == list:
        converted_list = [to_json(elem) for elem in obj]
        result = '[' + ', '.join(converted_list) + ']'
        return result
    elif obj_type == dict:
        result = '{'
        for key in obj:
            result += to_json(str(key)) + ': ' + to_json(obj[key]) + ', '
        result = result[:-2] + '}'
        return result
    elif obj_type in [int, float]:
        return str(obj)
    elif obj_type in [bytes, bytearray, str, complex]:
        return '"' + obj + '"'
    elif obj is True:
        return 'true'
    elif obj is False:
        return 'false'
    elif obj is None:
        return 'null'
    else:
        if raise_unknown:
            raise JsonError(obj)
        else:
           return ''

class Example:
    def __init__(self):
        self.x = 5

def main():
    x = [1, 2.2, 3, False, None]
    y = {1: 'a', 2: 'b', 3: 'c', 4: x}
    z = {'a': {2: {1: {1: {1: {1: {1: 5}}}}}}, 2: [1, 8]}
    print(json.dumps(z))
    print(to_json(z))
    print(to_json(y))
    print(json.dumps(y))
    print(to_json(x))
    print(json.dumps(x))
    # o = frozenset()
    # print(to_json(o))

if __name__ == '__main__':
   main()