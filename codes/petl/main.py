# pip install petl

import petl as etl

# 读取 CSV 文件 
table = etl.fromcsv('example.csv')
print(etl.look(table))

# 将数据转换为 JSON 格式并写入文件 
etl.tojson(table, 'example.json')


# 假设我们想过滤掉年龄小于 18 岁的记录 
youngsters = etl.select(table, lambda rec: rec.age < 18)
print(etl.look(youngsters))


# 假设我们要按照工作类型来统计平均收入 
income_by_job = etl.aggregate(table, 'job', sum, 'income')
print(etl.look(income_by_job))