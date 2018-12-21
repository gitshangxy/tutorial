# 哈希 hash
# hash ：概括摘要加密算法。一般的加密，比如a-z对应数字1-26，abc的密文为123，abcde的密文为12345。而hash是“摘要”算法，不管1kb的txt文件还是几个G的视频，最终都会生成一个固定长度的字符串。
# 优点：文件轻度修改最终摘要就大幅变化，如果被修改会快速发现。正向生成摘要容易，从摘要反推难。
# 常用加密算法：md5  sha128 sha256
"""
场景
1. 校验文件，保证文件被第三方修改。确保下载文件没加入广告或恶意程序。
2. 校验接口参数。api平台app_key和params生成sign签名，如果传输过程中有误或被中间人截取请求修改，那么签名会不匹配，服务器检测到丢弃。
3. 字典，hash表，散列表。hash值作为键名供快速访问。
4. 密码加密。用户注册成功后把密码hash处理然后把摘要字符串存入数据库，用户登录时讲用户提交的密码hash 然后跟数据库中的字符串对比，这样的好处是数据库被黑客登录后仍然无法获取用户密码。
"""

import hashlib
md5 = hashlib.md5()
md5.update('一些文本，待加密的文件块'.encode('utf-8'))
md5.update('admin'.encode())
# md5.update()  '\xbdc\x9c'
print(md5.hexdigest())    # Md5:aead68e839058f37b2f187f8dff2c2bf

"""
ipdate() 比较大的文件如视频可以分成多块，多次调用update().
参数为二进制，待摘要信息是字符串的话先编码。
hex digest 生成十六进制摘要字符串
"""

"""
攻击：穷举，对撞。
hash加密并不是绝对安全。
有些人喜欢常用容易被猜到的密码。
admin  213243esdqte2y3wtqy2ewd
password  aead68e839058f37b2f187f8dff2c2bf
123456
qwer
有攻击者根据弱密码字典（10万个弱密码）通过代码生成md5加密，存入一张数据库表。
如果这个黑客窃取了网站的用户表，即使用户密码字段存的是密文，跟自己生成的md5作比对，
如果对上即知道用户明文密码，冒充用户登录窃取信息钱财。所以密码不建议起的太简单。
"""

# 解决方案：加额外的字符串混稀，俗称加盐salt。
salt = 'adc'
md5 = hashlib.md5()
md5.update(('password'+salt).encode('utf-8'))
print('md5' + '$' + salt + '$' + md5.hexdigest())
# md5$adc$d5ea5d573812f4032acd52d25cdbce68
"""
加盐后，黑客想要穷举攻击，需要每个弱密码加盐再生成字符串，10万个弱密码，加盐前只需一张10w行数据的表，加盐后每一个盐需要1*10w行，10w密码需要10w*10w行。每个用户注册随机生成一个盐，穷举成本大大提高，黑客放弃攻击。
"""

# 增加安全性  方法二：多次加密  两三次后已经比较安全。
md5 = hashlib.md5()
md5.update('password'.encode('utf-8'))
str1 = md5.hexdigest()
md5.update(str1.encode('utf-8'))
str2 = str1 = md5.hexdigest()
md5 = hashlib.md5()
md5.update(str2.encode('utf-8'))
str3 = md5.hexdigest()
print(str3)


# 小作业
# def chinese(uchar):
#     if uchar >=u'\u4e00' and uchar <= u'\u9fa5':
#         return True
#     else:
#         return False
# a = chinese('机')
# print(a)
"""
小作业：百度，判断输入的用户输入字符串是否纯中文或纯英文？unicode区间
作业2：（选做）搜索更多关于hash的知识，算法原理，穷举对撞攻击，加salt的文章。
"""