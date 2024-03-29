# 时间处理   time    datetime  calendar   date
import time
import datetime
from datetime import datetime, timedelta        # 从datetime包引用datetime

# 1. datetime.now()返回当前时间datetime.datetime(2018, 10, 24, 15, 16, 37, 112126)对象，方便进行日期加减等处理。
print(datetime.now())       # 2018-10-24 15:19:50.942213
# 2. 创建datetime对象
dt = datetime(2018, 10, 24, 15, 21,00)
print(dt.year)
print(dt.month)
# 3. 日期加减      场景：判断活动截止；定时任务
print(datetime.now() + timedelta(days=-1, hours=10))
# 4. (常用)格式化输出   strftime   format   对象转字符串
'2018-10-24 15:23:47.714755'  '2018-10-24 15:23:47'  '15:23:47'
'2018-10-24 15:23:47'  '2018/10/24 15/23/47'
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))     # 2018-10-24 15:34:27
# %Y 2018年     %y 18  year
# %m month 月
# %d day  日
# %H hour  小时
# %M  minute  分钟
# %S  seconds 秒
# 5. 时间戳转datetime对象
print(datetime.fromtimestamp(1540368790))
# 6> 字符串转时间对象   parse
dtstr = '2018-10-06T09:25:03.401Z'
dt = datetime .strptime(dtstr, '%Y-%m-%dT%H:%M:%S.%fZ')
print(dt)


# time
# 1> (常用) 生成当前时间的时间戳    time()
# 整数形式的时间戳 timestamp: 当前时间 减去 1970-1-1 0:0:0 的秒数，形如1540368790 把时间量化成数字，比较时间先后顺序，计算转换有优势。缺点可读性差，默认长度只能表示到2030年。
print(time.time())
# 2> 生成本地时间   GTM+8  zh
print(time.localtime())

# 格林尼治时间，时区http://wenku.todgo.com/zhiyejiaoyu/8891967b7fc8.html
# 场景：网站的用户分布世界各地，放了一个双11促销活动，需要考虑时区。
# 3> (常用) 格式化时间
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# 4> 字符串转time结构
tmobj =time.strptime('2018-10-06T09:25:03.401Z','%Y-%m-%dT%H:%M:%S.%fZ')
print(tmobj)
# 5>从time结构对象生成数字时间戳   make
print(time.mktime(tmobj))
# 6> time.sleep()   场景：操作温湿度传感器，没5s打印一次数据。 玩笑:客户优化速度要钱。
time.sleep(5)

