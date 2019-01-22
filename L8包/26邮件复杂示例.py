# 邮箱内容为html，携带附件
import yagmail
import os

sender = '2765970564@qq.com'  # 发送人
password = 'odrwpyqkpujddhac'  # 邮箱授权服务密码
target = '2402338299@qq.com'  # 接收人
# 3097833625 张楠楠的qq
html = """
<html lang="zh">
    <head>
        <meta charset="utf-8">
        <title>示例2<title>
    </head>
    <body>
        <h1>测试</h1>
        <p>dsjdsnewj</p>
        <img src="https://www.baidu.com/img/bd_logo1.png"/>
    </body>
</html>
"""
attachment_path = os.path.join(os.path.dirname(__file__), 'base2.png')
print(attachment_path)

contents = ['测试yagmail示例2', html, attachment_path]  # [正文, 正文, 附件]

yag = yagmail.SMTP(user=sender, password=password, host='smtp.qq.com', port=465, smtp_ssl=True)
yag.send(to=target, subject='yagmail示例2', contents=contents)  # 群发的话收件人为列表
print('已发送')


