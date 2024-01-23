# 安装
# pip install path

from path import Path

## 路径创建与遍历

# 创建  Path  对象 
d = Path("/home/username/documents")

# 列出指定模式的所有文件 
for f in d.files("*.txt"):
    print(f.abspath())


# 修改文件权限 
for f in d.files("*.sh"):
    f.chmod(0o755)
    
# 切换当前工作目录 
with Path("/path/to/directory"):
    # 在这个模块里，当前工作目录变为 `/path/to/directory`
    pass

# 拼接路径 
config_path = Path("/etc") / "config.ini"
print(config_path)