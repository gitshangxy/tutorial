# beautifulsoup
# bs包把html按照节点的层次关系转换为树形文件，然后解析，简单易用。
# 安装 'pip install beautifulsoup4'  注意'beautifulsoup'只能用于py2
# 1xml是安全解析html标签文档树，支持bs4和xpath。
# 安装 'pip install lxml'

from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <a id="aaa" href='http://www.baidu.com' name='aaa' 
        class="aaa">百度一下</a>
        <a href='http://www.baidu.com'>百度一下2</a>
        <h1>大家好</h1>
    </body>
</html>
"""

# 实例化bs，传入参数待解析html内容和解析器
# html.parser python内置，方便兼容性好；lxml基于c，效率较高，需要额外安装包
bs = BeautifulSoup(html, 'lxml')
# bs = BeautifulSoup(html, 'html.parser')
# 格式化输出
print(bs.prettify())

# 查找标签
print(bs.head)    # None
print(bs.a)       # <a class="aaa" href="http://www.baidu.com" id="aaa" name="aaa">百度一下</a>
print(bs.find_all('a'))         # [<a> ... <a>, <a> ... <a>]

# (了解)返回标签名字
print(bs.name)  # [document]
print(bs.a.name)  # a

# 根据标签属性查找
print(bs.a['href'])

# (了解)删除标签属性
print(bs.a)
del bs.a['id']
print(bs.a.attrs)    # {'href': 'http://www.baidu.com', 'name': 'aaa', 'class': ['aaa']}

# 标签内容
print(bs.a.string)

# 子节点和父节点
print(bs.body.contents)    # 返回列表  标签下所有子标签
print(bs.body.children)    # 返回迭代器  子节点列表
for c in bs.body.children:
    print(c)

# 搜索
print(bs.find_all('a'))
print(bs.find_all(['a', 'h1']))

# 搜索 根据属性
print(bs.find(id='aaa'))
# (了解)根据class
print(bs.find_all(class_='aaa'))
# (了解)根据css语法
print(bs.select('a'))
print(bs.select('.aaa'))
print(bs.select('#aaa'))
print(bs.select('body .aaa'))
