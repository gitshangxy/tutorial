# 图表
# 常见的图表：条状图、点状分布、雷达图、折线图、饼状图。
# 作用和场景：1.直观整理信息， 支付宝年度账单，阿里云服务器控制
# 台，管理后台。 2.好看、项目出彩。
# 常用图表包：
# 1. pillow、opencv、偏底层，是一些图表包的依赖包.
# 2. matplotlib,知名的图表库，广泛用于图表绘制和科学计算。功能完善，文档复杂。
# 3. chart.js echart，图表库最终要渲染到浏览器中，不少图表库基于js，在python web框架中只要把数据渲染js图表示例的响应位置，也可以使用js图表库。
# 4. pygal 后端python图表库，包含常见图表类型，虽然种类不及matplotlib，但文档和示例非常简单。 安装 pip install pygal (如果pip安装不上 官方https://pypi.org/project/pygal/#files 文档下载 在终端cd到程序根目录下 pip install 程序文档名)
# svg格式，比jpg、png复杂的一种图片格式，具备html属性，可以定义大小颜色、交互等各种功能，尺量图，体积小功能强

import pygal

bar = pygal.Bar()
bar.add('人口(单位亿)', [11 ,12, 12.5, 13, 15, 16])
bar.render_to_file('3bar.svg')
bar.render_to_png('3bar.png')

# 更多图表类型详见  # 教程（http://www.pygal.org/en/stable/documentation/index.html）
# 自定义详见 http://www.pygal.org/en/stable/documentation/styles.html
