# pip3 install addressrec

import addressrec

result = addressrec.run(
    '王志超 029-68216000 新疆维吾尔自治区乌鲁木齐市沙依巴克区西虹东路 463 号',
    True, # 可不传默认true 指定参数town_village(bool)，可获取乡镇、村、社区两级详细地名  
    False # 可不传默认false 指定参数change2new(bool)可自动将旧地址转换为新地址
)
print(result)
