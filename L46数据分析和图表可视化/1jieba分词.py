# jieba分词
# 作用：把一句话 按照词汇分隔，为后面的词汇统计和图片展示打基础。
# 安装 pip install jieba

import jieba
import pymysql

results = jieba.cut('把一句话 按照词汇分隔，为后面的词汇统计和图片展示打基础。', cut_all=False)

word_list = []
for r in results:
    print(r)
    word_list.append(r)
print(word_list)

for r in results:
    print('生成器只能取一次', r)
print(results)      # <generator object Tokenizer.cut at 0x00000000044F9E08>



"""
生成器generator，参考L4/5小节
更列表相比：
1. 都是可迭代的，被for循环。range(0,10)返回的就是生成器。
2. generator优点用一个取一个，占内存低。
3. 循环后才能看到数据不太直观；数据只能取一次。如果想重复访问，需要再次生成generator或把数据
"""