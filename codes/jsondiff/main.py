# pip install jsondiff

from jsondiff import diff

a = {'a': 1, 'b': 2}
b = {'b': 3, 'c': 4}

result = diff(a, b)
print(result)  # 将输出 {'c': 4, 'b': 3, delete: ['a']}


result = diff({'a': [0, {'b': 4}, 1]}, {'a': [0, {'b': 5}, 1]})
print(result)  # 输出 {'a': {1: {'b': 5}}}

# jdiff a.json b.json -i 2 -s symmetric