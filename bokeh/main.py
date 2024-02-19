# pip install bokeh

from bokeh.plotting import figure, show


# --- 创建图表 ---

# 准备数据 
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# 创建图表 
p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

# 添加折线图 
p.line(x, y, legend_label="Temp.", line_width=2)

# 展示图表 
show(p)

# --- 交互式元素 ---

from bokeh.layouts import layout
from bokeh.models import Div, RangeSlider, Spinner
from bokeh.plotting import figure, show

# 准备数据
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [4, 5, 5, 7, 2, 6, 4, 9, 1, 3]

# 创建图表
p = figure(x_range=(1, 9), width=500, height=250)
points = p.circle(x=x, y=y, size=30, fill_color="#21a7df")

# 设置文本区域
div = Div(
    text="""
          <p>Select the circle's size using this control element:</p>
          """,
    width=200,
    height=30,
)

# 设置选项
spinner = Spinner(
    title="Circle size",
    low=0,
    high=60,
    step=5,
    value=points.glyph.size,
    width=200,
)
spinner.js_link("value", points.glyph, "size")

# 设置滑块
range_slider = RangeSlider(
    title="Adjust x-axis range",
    start=0,
    end=10,
    step=1,
    value=(p.x_range.start, p.x_range.end),
)
range_slider.js_link("value", p.x_range, "start", attr_selector=0)
range_slider.js_link("value", p.x_range, "end", attr_selector=1)

# 创建样式
layout = layout(
    [
        [div, spinner],
        [range_slider],
        [p],
    ],
)

# 显示结果
show(layout)

# --- 自定义图表 ---

from bokeh.io import curdoc
from bokeh.plotting import figure, show

# 准备数据
x = [1, 2, 3, 4, 5]
y = [4, 5, 5, 7, 2]

# 添加主题
curdoc().theme = "dark_minimal"

# 创建图表
p = figure(sizing_mode="stretch_width", max_width=500, height=250)

# 添加元素
p.line(x, y)

# 显示结果
show(p)