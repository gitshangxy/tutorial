### 可能出现的报错
reverse函数reverse('polls:results', args=(question.id))
等价 前端{% url 'polls:vote' question.id %}
等价 flask url_for('模块.视图函数名', arg1=valuel)
1. Reverse for 'votes' not found. 'votes' is not a valid view dunction or pattern name.  构造url是出错，跟urls.py定义的path规则不匹配。
解决：检查urls.py中的app_name  path()规则中的name、路由  可变部分的变量名 跟{% url '命名空间:path规则名' 参数 %}
2. Reverse for 'vote' with arguments '('',)' not found. 1 pattern(s) tried: ['polls\\/(?P<question_id>[0-9]+)\\/vote\\/$']
前端渲染不出来值，html中写死的内容可以展现，后台对象可以取到。
原因：渲染值传参错误 render(context={'question': question}) 误写成
return render(request, 'polls/detail.html', {'context': question})
3. csrf验证失败
原因：开了翻墙工具，中间电脑访问服务器相当于中间人攻击。绝对：关闭工具。
4. 提交按钮无响应
原因：<form>写成<from>  。可以看出html语法要求宽松带来的要求。


"""
作业1：django 官网教程part5 自学
（选做）娱乐玩具：百度 “chrome插件Chat Anywhere” 

作业2 整理polls项目，上传github，官网教程从头到尾再看下做下

作业3 预习实验楼linux基础教程
"""