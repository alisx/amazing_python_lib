# pip install munch

# ---- 从字典到 Munch----
from munch import Munch

# 创建一个空的 Munch 对象 
b = Munch()

# 像访问属性一样设置键值 
b.hello = 'world'

# 像使用字典一样访问 
print(b['hello'])  # 输出: world

# 继续像属性一样访问和修改 
b['hello'] += "!"
print(b.hello)  # 输出: world!

# 你甚至可以嵌套使用 Munch
b.foo = Munch(lol=True)
print(b.foo.lol)  # 输出: True

# ----字典的兼容----
# 使用字典的方法 
b.update({'new_key': 'new_value'})

# 还可以用正常的方式进行迭代 
for key in b:
    print(key, b[key])

# 字典的“解包”也支持 
args = {'arg1': 'value1', 'arg2': 'value2'}
function_call(**Munch(args))

# ----序列化支持----
import json
import yaml

b = Munch(foo='bar', num=123)

# JSON 序列化 
json_str = json.dumps(b)

# YAML 序列化 
yaml_str = yaml.dump(b)


# ----支持默认值----
from munch import DefaultMunch, DefaultFactoryMunch

# 使用默认值的  Munch
dm = DefaultMunch('default', {'hello': 'world'})

# 工厂方法创建默认值的  Munch
dfm = DefaultFactoryMunch(list)

# 访问不存在的键会得到预设的默认值或通过工厂方法创建的值 
print(dm.not_exist)  # 输出: default
print(dfm.not_exist)  # 输出: []