# pip install pendulum

import pendulum

# 获取当前时间，并设置时区为巴黎 
now_in_paris = pendulum.now('Europe/Paris')
print(now_in_paris)  # 输出如：'2016-07-04T00:49:58.502116+02:00'

# 无缝时区转换 
now_in_utc = now_in_paris.in_timezone('UTC')
print(now_in_utc)  # 输出转换后的  UTC  时间

# 计算明天和上周的时间 
tomorrow = pendulum.now().add(days=1)
last_week = pendulum.now().subtract(weeks=1)

# 显示两分钟前的时间，并以便于理解的方式显示时间差 
past = pendulum.now().subtract(minutes=2)
print(past.diff_for_humans())  # 输出：'2 minutes ago'

# 计算时间差并输出具体小时数 
delta = past - last_week
print(delta.hours)  # 输出：23

# 使用自然语言表示时间差 
print(delta.in_words(locale='en'))  # 输出：'6 days 23 hours 58 minutes'

# 创建一个存在时间窜变的时间点，Pendulum  会自动做出适应性调整 
dt = pendulum.datetime(2013, 3, 31, 2, 30, tz='Europe/Paris')
print(dt)  # 输出：'2013-03-31T03:30:00+02:00'，即，2:30  这个时间实际上是不存在的