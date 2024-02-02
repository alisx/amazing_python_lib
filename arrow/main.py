import arrow


# ==== 创建和格式化时间 ====

import arrow

# 从字符串、时间戳或其他格式直接获得  Arrow  对象 
arw = arrow.get('2013-05-11 21:23:58')
# 如: 2013-05-11T21:23:58+00:00

# 获取当前  UTC  时间 
utc = arrow.utcnow()
# 如: 2024-02-02T14:08:17.462608+00:00

# 时间偏移 
utc_shifted = utc.shift(hours=-1)
# 如: 2024-02-02T13:08:17.462608+00:00

# 格式化时间输出 
formatted_time = utc.format('YYYY-MM-DD HH:mm:ss ZZ')
# 如: 2024-02-02 14:08:17 +00:00

# 当前本地时间
a = arrow.now()
# 如: 2024-02-02T22:15:02.779458+08:00

# 特定时区当前时间
b = arrow.now('America/New_York')
# 如: 2024-02-02T09:17:52.297905-05:00

# ==== 时区转换 ====
# 将 UTC  时间转换为特定时区的时间 
local = utc.to('Asia/Shanghai')
# 如 2024-02-02T22:08:17.462608+08:00

# ==== 人性化时间 ====
a = arrow.now()
b = a.shift(hours=-2)

# 输出相对现在的时间 
print(b.humanize())
# 如: 2 hours ago

# 甚至支持本地化 
print(b.humanize(locale='zh'))
# 2小时前

# 相对于特定时间
print(a.humanize(b, locale='zh'))
# 2小时后

# ==== 时间戳处理 ====
# 获得时间戳 
timestamp = local.timestamp()
# 如: 1706882897.462608


'''
一些常见的 IANA 时区代码及其对应的城市或地区

- 'UTC'：世界标准时间
- 'Europe/London'：伦敦时间
- 'America/New_York'：美国纽约时间
- 'Asia/Shanghai'：中国上海时间
- 'Asia/Beijing'：中国北京时间
- 'Europe/Paris'：法国巴黎时间
- 'Asia/Tokyo'：日本东京时间
- 'Australia/Sydney'：澳大利亚悉尼时间
- 'America/Los_Angeles'：美国洛杉矶时间
- 'Asia/Kolkata'：印度时间
- 'Asia/Dubai'：迪拜时间
- 'America/Sao_Paulo'：巴西圣保罗时间
- 'Africa/Cairo'：埃及开罗时间
- 'Asia/Seoul'：韩国首尔时间
'''