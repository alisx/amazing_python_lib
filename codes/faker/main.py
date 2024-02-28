from faker import Faker
fake = Faker()

print(fake.name())  # 生成一个姓名
# 'Lucy Cechtelar'

print(fake.address())  # 生成一个地址
# '426 Jordy Lodge
#  Cartwrightshire, SC 88120-6700'

print(fake.text())  # 生成一段文本
# 'Sint velit eveniet. Rerum atque repellat voluptatem quia rerum. Numquam excepturi...'

# 生成 10 个不同的姓名 
for _ in range(10):
    print(fake.name())
    
# 局部化
fake_it = Faker('it_IT')  # 创建一个意大利语的  Faker  实例 
for _ in range(5):
    print(fake_it.name())

fake_jp = Faker('ja_JP')  # 创建一个日本语的  Faker  实例 
for _ in range(5):
    print(fake_jp.name())
    
# 伪数据提供者（Providers）

from faker.providers import internet

fake.add_provider(internet)
print(fake.ipv4_private())  # 使用新增的互联网提供者生成私有  IPv4  地址

# 唯一性和随机数种子
unique_names = {fake.unique.first_name() for _ in range(500)}

Faker.seed(4321)
print(fake.name())  # 与上次设置相同种子时生成的姓名一致

# 实践
'''
1. 生成并打印包含 10 个不同国家（如'zh_CN', 'en_US', 'ja_JP'）的姓名。
2. 创建一个自定义的提供者，用于生成你自己定义的一套专业术语，然后生成一些示例数据。
3. 尝试使用  Faker  生成一份具有唯一邮箱地址的用户列表。
'''