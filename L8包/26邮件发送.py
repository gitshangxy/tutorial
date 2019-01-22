# 邮件发送
# 场景：工作沟通邮件；登陆注册；广告；修改密码、激活链接；邮件客户端
# 参考  https://www.1owo.com/python/python/python-python%E5%8F%91%E9%82%AE%E4%BB%B6/

"""
准备工作：
授权。各个邮件大同小异。这里以qq邮箱为例。
1> qq邮箱首页
2> qq邮箱首页/设置/账户  向下翻到POP3/IMAP/SMTP服务。
3> 开启 IMAP/SMTP服务

"""

"""
邮件相关协议：
- SMTP(simple mail transfer protocol)简单邮件传输协议。用于发邮件。
- POP3(Post office protocol)邮件协议。将邮件服务器上资料同步到本地。用于收邮件。   开通以上两种协议后收邮件，发现可以正常收取，但有个问题，通过程序拉取的邮件已下载已阅读，但登陆官方邮件后发现之前下载的邮件任然是未读状态。说明POP3协议只能简单的收件但不能标记邮件状态。
- IMAP(internet mail access protocol)，交互式邮件存取协议， POP3协议的增强版。标记已读、删除，跟官方邮件服务器状态保持同步，体验较好。
- SSL , 数据链路层加密， https基于此技术。qq邮箱的邮件协议也开启了这个加密，代码中注意配置SSL为True。
"""

"""
发邮件的包：
- smtplib poplib imaplib  ,内置包 缺点不太方便
- zmail , 中文文档，缺点有bug
- yagmail, star人数多，稳定，国外邮件公司开发的产品。缺点不会自动识别qq邮件域名，需要手动配置。 pip install yagmail 。注意anaconda环境中只安装这个包的旧版本。

ssl 链路层加密

"""

# 2765970564@qq.com
# odrwpyqkpujddhac
# 接收邮件服务器  imap.qq.com  端口 993
# 发送邮件服务器  smtp.qq.com  端口 465或587
# ssl开启
