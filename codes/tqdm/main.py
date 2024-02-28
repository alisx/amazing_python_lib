# pip install tqdm

# 易于使用
from tqdm import tqdm
for i in tqdm(range(10000)):
    # 您的操作
    pass

#  自定义进度条
from tqdm import trange
for i in trange(100, bar_format='{l_bar}{bar:10}{r_bar}{bar:-10b}'):
    # 您的操作
    pass

# 命令行管道
# $ seq 9999999 | tqdm --bytes | wc -l

# 7z a -bd -r backup.7z docs/ | grep Compressing | tqdm --total $(find docs/ -type f | wc -l) --unit files >> backup.log