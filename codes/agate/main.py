# https://github.com/wireservice/agate

# pip install agate

import agate
table = agate.Table.from_csv('some_data.csv')


# 筛选特定的列 
selected_columns = table.select(['column1', 'column2'])

# 按某列进行排序 
sorted_table = table.order_by('column1')

# 过滤符合条件的数据行 
filtered_rows = table.where(lambda row: row['column1'] == 'desired_value')


# 按某个属性进行分组 
grouped = table.group_by('category')

# 对每个组进行聚合运算 
summary = grouped.aggregate([
    ('mean_column1', agate.Mean('column1')),
])

# 验证某列的每个条目是否符合特定条件 
validator = table.compute([
    ('is_valid', agate.Formula(text_type, lambda row: your_validation_function(row['column1']))),
])

# 然后你可以过滤出所有有效或无效的数据行 
valid_rows = validator.where(lambda row: row['is_valid'])