# pip install lmdb

import lmdb

# 创建/打开数据库 
env = lmdb.open('mylmdb', create=True)

# 写入数据 
with env.begin(write=True) as txn:
    txn.put(b'name', b'LMDB')

# 读取数据 
with env.begin(write=False) as txn:
    print(txn.get(b'name').decode())  # 输出: LMDB
    
# 遍历数据库 
with env.begin(write=False) as txn:
    for key, value in txn.cursor():
        print(key, value)