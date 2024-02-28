import mimetypes

# 查询文件 MIME 类型 
mimetype, _ = mimetypes.guess_type('example.jpg')
print(mimetype)  # 输出: image/jpeg

# 获取 MIME 类型对应的常见文件扩展名 
extension = mimetypes.guess_extension('image/jpeg')
print(extension)  # 输出: .jpg

# 查看所有的 MIME 类型和扩展名映射 
all_types = mimetypes.types_map
print(all_types)

# 添加新的 MIME 类型关系 
mimetypes.add_type('text/markdown', '.md')

# 小测试
def file_info(file_path):
    # Your code here
    pass