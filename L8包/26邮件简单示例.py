import yagmail
#  安装 pip install yagmail

sender = '2765970564@qq.com'  # 发送人
password = 'odrwpyqkpujddhac'  # 邮箱授权服务密码，注意不是qq邮箱 登陆密码
target = '2402338299@qq.com'  # 接收人邮箱地址。

yag = yagmail.SMTP(user=sender, password=password, host='smtp.qq.com', port=465, smtp_ssl=True)
contents = '测试test'
yag.send(to=target, subject='测试yagmail发邮件', contents=contents)
print('已发送')



# 备注：跨邮箱服务商可能会有延迟，比如qq邮箱发送到网易邮箱。谷歌邮箱服务器被 收不到。
# 报错：SSL报错。解决方法，换用更稳定的python解释器。已知py2.7.6和py3.7.0会出现问题。




