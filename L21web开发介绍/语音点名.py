# （课外作业）语音播报pyttsx
# 1. 百度搜索相关中文解决方案，大概要用哪些包
# 2. github搜索相关包
# 3. pip install pyttsx3
# 4. 示例代码
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()


# import pyttsx3
#
# engine = pyttsx3.init()
# rate = engine.getProperty('rate')
# engine.setProperty('rate', 120)
# engine.say('are your sure  ,小齐, 董歌鸽, 尚小雨,四大皆空 ')
# engine.runAndWait()


# student_list = ['董歌鸽']
# engine = pyttsx3.init()
# engine.say (student_list)
# engine.say(' 越来越漂亮了')
# engine.runAndWait()
