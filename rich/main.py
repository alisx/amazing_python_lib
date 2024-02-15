# pip install rich

from rich import print
from rich.console import Console
from rich.table import Table
from rich.progress import track
from rich.markdown import Markdown
import time

# 基本打印 
print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())

# 控制台输出
console = Console()
console.print("Hello", "World!", style="bold red")

# 表格渲染
console = Console()
table = Table(show_header=True, header_style="bold magenta")
table.add_column("Date", style="dim", width=12)
table.add_column("Title")
# ... 此处省略其他列和行的添加 
console.print(table)

# 进度条

for step in track(range(100)):
    # todo do_step(step)
    time.sleep(1)
    
# Markdown

with open("README.md") as readme:
    markdown = Markdown(readme.read())
console.print(markdown)


