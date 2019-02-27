### session cookie

1. 浏览器表单 用户名、密码
2. 后台比对数据库，正确，根据用户名生成hash摘要字符串，session表中存储摘要字符串。


### jwt （json web token）
跟django本书session cookie思想几乎完全一致，只不过技术细节不一样。

1. 浏览器

