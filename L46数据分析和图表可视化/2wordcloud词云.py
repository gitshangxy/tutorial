# wordcloud词云
# 作用：根据词汇和词频生成一张美观的词汇
# https://blog.csdn.net/qq_34337272/article/details/79552929
# 安装 pip install wordcloud
# pip install matplotlib

# pip install MyQR  动态二维码

from matplotlib import pyplot
from wordcloud import WordCloud

string = """英文 和 中文 舞蹈民族 古筝古琴钢琴 吉他乐器 学习 eyewesdcx 家庭加载家族 是今年实现 编程管理数据库"""

string2 = """Importance of relative word frequencies for font-size. With relative_scaling=0, only word-ranks are considered. With relative_scaling=1, a word that is twice as frequent will have twice the size. If you want to consider the word frequencies and not only their rank, relative_scaling around .5 often looks good
"""
# font = 'C:\\Windows\\Fonts\\msyh.ttc'
font = 'msyh.ttc'
wc = WordCloud(font_path=font,      # 如果是中文必须要添加这个，否则会显示成框框
               background_color='white',
               width=1000,
               height=800,
               max_font_size=300,
               min_font_size=50,
               ).generate(string)
wc.to_file('2词云.png')  # 保存图片

