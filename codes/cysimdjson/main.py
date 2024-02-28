# pip3 install cysimdjson

import cysimdjson

json_bytes = b'''
{
  "array": [1, 2, 3],
  "boolean": true,
  "color": "gold",
  "null": null,
  "number": 123,
  "object": {"a": "b", "c": "d"},
  "string": "Hello World"
}
'''

parser = cysimdjson.JSONParser()
json_element = parser.parse(json_bytes)
print(json_element.at_pointer("/array/1"))  # 输出: 2

json_parsed = parser.loads(json_bytes)
print(json_parsed['object']['a'])  # 输出: 'b'

# 使用  parse_in_place  进行快速解析 
parsed_fast = parser.parse_in_place(json_bytes)