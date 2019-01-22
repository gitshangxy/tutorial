## 介绍
selenium是浏览器自动化测试框架。主要领域是自动化测试。也可用于爬虫。
selenium框架用于脚本主流的浏览器（谷歌、火狐、IE），让浏览器自动化打开、点击、翻页、选择标签、取属性内容。

场景：
1. 代替麻烦重复的人工测试流程。
2. 京东的爬虫走了一些js请求，有些参数不知道构造方法，很难分析和模拟请求。缺点：效率慢；考虑浏览器操作，项目复杂时编写的脚本更复杂影响开发者效率。

本节了解，不做重点掌握。

## 安装
1. pip install selenium
2. 安装浏览器对应版本的驱动  
1> [驱动网址](http://chromedriver.storage.googleapis.com/index.html)
2> 谷歌浏览器/设置/帮助/关于  看下浏览器版本
3> 选择对应的版本和平台的zip包下载
4> 解压后得到的 chromedriver.exe
5>放到python解释器（C:\Program Files\Python36\Scripts）下。
6> 重启浏览器

(以下废弃 太麻烦)
5> 桌面chrome图标右键/打开文件位置，打开chrome安装目录（C:\Program Files (x86)\Google\Chrome\Application）,把chromedriver.exe放入chrome安装根目录下。
6> 将chrome安装根目录添加到环境变量。通过shell脚本或重启电脑让环境变量生效。
7> 重启浏览器。让chromedriver.exe生效。
(    )
3. 写一段简单的selenium脚本测试生效。

