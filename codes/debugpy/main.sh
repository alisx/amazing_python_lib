pip install debugpy

# 启动和连接到调试器
python -m debugpy --listen localhost:5678 myfile.py

python -m debugpy --listen localhost:5678 --wait-for-client myfile.py

# 远程调试
python -m debugpy --listen 0.0.0.0:5678 myfile.py

# 实践
python -m debugpy --listen localhost:5678 --wait-for-client buggy.py