import debugpy
debugpy.listen(("localhost", 5678))
# 等待调试器连接 
debugpy.wait_for_client()