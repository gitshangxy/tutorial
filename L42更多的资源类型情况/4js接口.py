# 4.js异步请求
# 一些后端语言的框架入django是把变量渲染到hhtml模板最终再response返回，用户交互时需要刷新页面才能看到修改后的效果。为了更好地网页体验和前后端程序员工作分离。前端js工作中也有类似后端requests包的前端操作包。导致有些数据第一次html中看不到，浏览器会在加载html后执行js，但requests包不会，无法直接获取到信息。
# 解决思路：js中发送html请求，浏览器开发者工具会拦截到，分析html请求结构，用requests包构造请求获取信息。



"""
<html>
    <body>
        <h1>带爬取内容</h1>
        <script>
            document.onloads(
            function foo():{
                //请求商品列表
                //(伪代码)

                //操作dom节点把商品信息渲染到页面中。
            })

            $.get('hutton').ajax({
                url:xxx,
                params: page_no=1,
                })
        </script>

    </body>
</html>

js中请求一  类似后端的requests包，发送http请求。开发者工具中看响应是否是js数据。
js中请求二  ajax 相当于上面的封装。lxml结构沟通。开发者工具XHR(XMLHttpRequest)

小技巧：网页请求非常多
"""

# 需求 爬取一个商品的评论
"""
分析：商品评论原始url https://item.jd.com/7348367.html#comment
当点击评论的第二页的时候，url路由并没有变化没有参数。
如果django来做分页路由形式如下
https://item.jd.com/7348367.html#comment?page_no=2。
其实评论信息的请求在js中，由浏览器后台执行。
所以我们需要在谷歌开发者工具中 找到js中的评论信息请求，requests包构造请求，模拟浏览器的执行过程。

分析后得到的请求地址
https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv15262&productId=100000287113&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1
然后用requests包构造这个请求

分析参数：发现有的参数不知含义或动态生成或保持默认即可。考虑删减具有
"""

import requests
import json
from lxml import etree

comment_url = 'https://sclub.jd.com/comment/productPageComments.action'

params = {
    'productId': '100000287113',  # 商品id。先写死 苹果手机。
    'score': '0',
    'sortType': '5',
    'page': '0',
    'pageSize': '10',
    # 'callback': 'fetchJSON_comment98vv15262',
    # 'isShadowSku': '0',
    # 'fold': '1'
}

# 伪造headers。   降低被封的概率
# cookie中有jsessionid和trackid和用户名等信息。referer请求前的页面地址。useragent
headers = {
    'cookie': '__jdv=122270672|direct|-|none|-|1545816689735; __jdu=1911103525; PCSYCityID=412; shshshfpa=e81ca139-57b3-859d-db27-78339be22811-1545816702; user-key=e6e7b3db-b81e-4e29-8d18-2963aff81485; _pst=jd_598308d66b7f6; unick=jd_598308d66b7f6; pin=jd_598308d66b7f6; _tp=dS86tAtyZt57yHlL9R%2BNUu3v8O%2FrLAQD41K6mOOZVgg%3D; pinId=xwE-ZhW4nJSRvUbV4pUlxLV9-x-f3wj7; ipLoc-djd=1-72-2799-0; shshshfpb=hxt36K8P20YPw1TZmBAjdqQ%3D%3D; __jdc=122270672; cn=0; _gcl_au=1.1.1347703983.1545965749; 3AB9D23F7A4B3C9B=27LQVPUGGIYY62HSTBF7XSFP52OJPDLZZTFE2V3JLCCXY3FB2YGYEQRS62LZGQGPYS5HQLYJ4KMIM3UX2YXLVIDQBI; __jda=122270672.1911103525.1539428691.1545990246.1545996033.13; wlfstk_smdl=kzm0o495p17lw0iroflp4ztxhw8vfnf0; TrackID=1kVg6wrzKIkbIwtyAeS3byevhpy4PYoHZmtjXyALQiylRGYJOrvzo3iN5dZovKhbJ37a6iy5tOykVb7W7XNtTjM7FY7_zEQJ0sMnxvQI3BPA; ceshi3.com=000; shshshfp=447bcde9e37449b49000397db3ec679a; JSESSIONID=25722BAEFFFD84A72C0D98F183399A52.s1; shshshsID=94e5d0e01ba94413e0a2966cc1749b5c_10_1545997219070; __jdb=122270672.11.1911103525|13.1545996033; thor=480285E8F578B86999D37FE49A7A1F4E2ADA8E07A4BAB2F00C5E718B96CA586F9CCC3DAE4651567C4DEED22DB2E5E3E5F5638EAF8F42B2A74B54C1D995CA334B50838AA0D55C4146252ED75AE629497C8FE95F957CD05A75488DAE4679BD13A58DF869E5C8288ACFD091CFE7A6F02E38924B53AA6844C9BA3E665876FFD05AA75BEFEDBA779B1945DE5D5A2A76DF8CF9F1BC2D46DBC84ABD1799F41D5E0511A7',
    'referer': 'https://item.jd.com/100000287113.html',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}

comment_resp = requests.get(url=comment_url, params=params, headers=headers)
print(comment_resp.status_code)
comment_str = comment_resp.text
# 转json对象
comment_dict = json.loads(comment_str)
# comment_dict = json.loads('4js接口-京东评论-评论数据.json')
comments = comment_dict['comments']
for comment in comments:
    print(comment['id'])
    print(comment['nickname'])
    print(comment['content'])
    print(comment['creationTime'])
    print(comment['score'])
    print(comment['productColor'])
    print(comment['productSize'])
    print(comment['userLevelName'])
    print(comment['referenceName'])
    print(comment['usefulVoteCount'])
    print(comment['replyCount'])
    # images = comment['images']
    # for image in images:
    #     print(image['imgUrl'])

prod = comment_dict['productCommentSummary']['goodRateShow']
print(prod)
hotCommentTagStatistics = comment_dict['hotCommentTagStatistics']
for hot in hotCommentTagStatistics:
    print(hot['name'])







"""
 作业
1.京东评论信息保存为csv格式
2. 保存为Excel格式xlsx
3. 写入到MySQL数据库
"""