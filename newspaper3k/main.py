
# 使用新闻源
import newspaper
cnn_paper = newspaper.build('https://news.sina.com.cn/')
for article in cnn_paper.articles:
    print(article.url)
for category in cnn_paper.category_urls():
    print(category)
    
# 处理单篇文章
from newspaper import Article

url = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'
article = Article(url)

# 下载文章 
article.download()
# 解析文章 
article.parse()
# 获取作者 
print(article.authors)
# 获取发布日期 
print(article.publish_date)
# 获取顶部图片 
print(article.top_image)
# 文章摘要 
article.nlp()
print(article.summary)

# 多语言

from newspaper import Article
url = "https://news.sina.com.cn/c/2024-01-26/doc-inaewiyx7293475.shtml"
a = Article(url, language='zh')  # 使用中文 
a.download()
a.parse()
print(a.text[:150])
print(a.title)

# 输出 
# 1月26日，2024年春运正式启动。统筹冬季寒潮大风和海冰等

# 我国三大海域举行海空立体巡航及演练 全力保障海上安全