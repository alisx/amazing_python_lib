# 安装

# pip install Jinja2

# 基础模板语法
'''
{% extends "layout.html" %}
{% block body %}
  <ul>
    {% for user in users %}
      <li><a href="{{ user.url }}">{{ user.username }}</a></li>
    {% endfor %}
  </ul>
{% endblock %}
'''

# 实践

'''
假设我们正在开发一个博客平台，现在需要设计一个博客文章的页面。我们可以先创建一个基础模板 `base.html`，里面包含网站的页头、页脚和主导航。

然后，我们会创建一个 `post.html` 模板，它从 `base.html` 中继承，并填充文章的具体内容：

{% extends "base.html" %}

{% block content %}
<article>
    <h1>{{ post.title }}</h1>
    <div class="date">{{ post.date }}</div>
    <div class="body">
        {{ post.body }}
    </div>
</article>
{% endblock %}
'''

from jinja2 import Environment, FileSystemLoader

# 创建一个加载器，Jinja2 会从"templates"文件夹中加载模板 
env = Environment(loader=FileSystemLoader('templates'))

# 加载模板 
template = env.get_template('post.html')

# 渲染模板，传入数据 
html = template.render(post={
    'title': '我的博文',
    'date': '2021-04-01',
    'body': '...'
})