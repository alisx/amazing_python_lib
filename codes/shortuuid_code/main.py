# 安装: pip install shortuuid

import shortuuid

# 生成  shortuuid
# 生成一个新的  short UUID
suuid = shortuuid.ShortUUID().random(length=22)
print(suuid)
# 输出: 3t49Ps42SFBPvZJaQpTASt

# 使用基于名称的  UUID  版本  5
shortuuid.uuid(name="example.com")
# 输出 'exu3DTbj2ncsn9tLdLWspw'

shortuuid.uuid(name="<http://example.com>")
# 输出 '4MbV4Zb37VYJocNpNcZvoT'

# 生成加密级别的随机字符串
shortuuid.ShortUUID().random(length=22)
# 输出 'RaF56o2r58hTKT7AYS9doj'

# 查看和设置生成  UUID  的字母表
shortuuid.get_alphabet()  # 获取字母表
# 输出 '23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

shortuuid.set_alphabet("aaaaabcdefgh1230123")  # 设置自定义字母表 会自动去除重复字符
shortuuid.uuid()  # 生成  UUID
# 输出 '0agee20aa1hehebcagddhedddc0d2chhab3b'

shortuuid.get_alphabet()
# 输出 '0123abcdefgh'

# 处理已有的  UUID
import uuid
u = uuid.uuid4()

s = shortuuid.encode(u)
print(s)
# 输出 'MLpZDiEXM4VsUryR9oE8uc'

shortuuid.decode(s) == u  # 转回  UUID  比较是否相同 
# 输出 True

# 类使用
su = shortuuid.ShortUUID(alphabet="01345678")
su.uuid()
# 输出 '034636353306816784480643806546503818874456'