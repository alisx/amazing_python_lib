# 安装：

# pip install envoy

# 执行命令
import envoy
# 运行 'git config' 命令 
r = envoy.run('git config')

print(r.status_code)  # 输出：129
print(r.std_out)      # 输出：'usage: git config [options]'
print(r.std_err)      # 输出：''

# 管道操作 
r = envoy.run('uptime | pbcopy')

print(r.command)     # 输出：'pbcopy'
print(r.status_code) # 输出：0
print(r.history)     # 输出：[<Response 'uptime'>]

# 超时与数据管道
r = envoy.run('git config', data='user.name=FooBar', timeout=2)

# 实践挑战

'''
1. 尝试在你的  Python  脚本中用  Envoy  运行一些简单的系统命令。
2. 设计一个命令序列并使用  Envoy  的管道功能来执行它们。
3. 对于可能需要较长时间执行的命令，尝试加上超时参数，并处理超时情况。
'''

