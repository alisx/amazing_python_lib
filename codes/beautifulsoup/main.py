from bs4 import BeautifulSoup

# --- 基础用法 ---
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.title)
# <title>The Dormouse's story</title>


# --- 寻找元素 ---
# 找到文档中所有<a>标签 
links = soup.find_all('a')

# 找到文档中所有的段落 
paragraphs = soup.find_all('p')

# 找到包含 id 属性的所有标签 
tags_with_ids = soup.find_all(id=True)

# --- 属性和导航 ---

# 获取<a>标签的 href 属性 
for link in soup.find_all('a'):
    print(link.get('href'))

# 导航到父标签 
parent_tag = soup.b.parent

# --- CSS 选择器 ---
# 通过 CSS 类名查找元素 
soup.select(".my-class")

# 通过 id 查找元素 
soup.select("#my-id")