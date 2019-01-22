import logging.config
import json
import os


# 1 默认生成的root logger的level是logging.WARNING,低于该级别的就不输出了
# logging.debug('啊')
# logging.info('你在哪')
# logging.warning('啊2')
# logging.error('我看不见')
# logging.critical('我是一颗小小的石头')
# 上面可以看到只有后面三个能打印出来

# 2 如果需要显示低于WARNING级别的内容，可以引入NOTSET级别来显示：
# logging.basicConfig(level=logging.NOTSET)  # 设置日志级别
# logging.info("如果设置了日志级别为NOTSET,那么这里可以采取debug、info的级别的内容也可以显示在控制台上了")

# 3 日志输出-控制台
# 通过logging.basicConfig函数进行配置了日志级别和内容输出格式
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')  # logging.basicConfig函数对日志的输出格式及方式做相关配置
# 由于日志基本配置中级别设置为DEBUG，所以一下打印信息将会全部显示在控制台上
# logging.info('等待1')
# logging.debug('等待2')
# logging.warning('等待3')
# logging.error('等待4')
# logging.critical('等待5')

#  4，将日志写入文件
# logger = logging.getLogger(__name__)
# logger.setLevel(level=logging.INFO)
# handler = logging.FileHandler("30log.txt")  # 创建
# handler.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)
# logger.addHandler(handler) # 添加
# logger.info("Start print log")
# logger.debug("Do something")
# logger.warning("Something maybe fail.")
# logger.info("Finish")

# 5，将日志同事输出到屏幕和日志
# logger = logging.getLogger(__name__)
# logger.setLevel(level = logging.INFO)
# handler = logging.FileHandler("30log2.txt")
# handler.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)
# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
# logger.addHandler(handler)
# logger.addHandler(console)
# logger.info("等待1")
# logger.debug("等待2")
# logger.warning("等待3.")
# logger.info("等待4")

# 6,通过JSON加载配置文件，然后通过logging.dictConfig配置logging，
# def setup_logging(default_path = "logging.json",default_level = logging.INFO,env_key = "LOG_CFG"):
#     path = default_path
#     value = os.getenv(env_key,None)
#     if value:
#         path = value
#     if os.path.exists(path):
#         with open(path,"r") as f:
#             config = json.load(f)
#             logging.config.dictConfig(config)
#     else:
#         logging.basicConfig(level = default_level)
#
# def func():
#     logging.info("等待1")
#     logging.info("等待2")
#     logging.info("等待3")
#
# if __name__ == "__main__":
#     setup_logging(default_path = "logging.json")
#     func()

# 7，将日志写入文件同时在显示屏上显示
logger = logging.getLogger(__name__)  # 实例化
logger.setLevel(level = logging.INFO)  # 设置日志级别，大于等于这个级别的信息才会输出。
handler = logging.FileHandler("30log3.txt")  # 设置文件操作器，保存的文件路径
handler.setLevel(logging.INFO)  # 文件操作器的日志写入级别
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # 设置时间格式
handler.setFormatter(formatter)  # 时间设置载入到文件操作器

console = logging.StreamHandler()
console.setLevel(logging.INFO)
logger.addHandler(handler)
logger.addHandler(console)
logger.info("等待着")
logger.debug("等待那")
logger.warning("等待额.")
logger.info("等待分析")
