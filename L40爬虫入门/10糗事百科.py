# coding=utf-8
# 正则
# 糗事百科热点文章爬取
# 分析：请求 url https://www.qiushibaike.com/hot/page/1/    要抓取dev class='article'下内容    urllib或requests  ，
import urllib.request
from fake_useragent import UserAgent
import random
import re

base_url = 'https://www.qiushibaike.com/hot/page/'
for ore in range(1, 10):
    url = base_url + str(ore) + '/'
    print(url)

# ua = UserAgent


# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
# }
# req = urllib.request.Request(url, headers=headers)
# resp = urllib.request.urlopen(req)
# html_content = resp.read().decode('utf-8')
# print(html_content)

html_content = """ 
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<meta http-equiv="X-UA-Compatible" content="chrome=1,IE=edge">
<meta name="renderer" content="webkit"/>
<meta name="applicable-device" content="pc">
<meta name="domain_verify" content="pmrgi33nmfuw4ir2ejyws5ltnbuweyljnnss4y3pnurcyithovuwiir2ejqwmyrtguzdgobsmezdgnbyheywcmzthbrdmmtemu4tamrqg5rtmirmej2gs3lfknqxmzjchiytkmrzgq4demjugaydcnd5">


















<title>24小时爆笑笑话大全 - 糗事百科</title>






















<meta name="keywords" content="笑话,笑话大全" />
<meta name="description" content="糗事百科官网提供24小时糗搞笑笑话大全,糗百24小时内新糗事就只在糗事百科官网24小时专题,囊括恶搞、尴尬糗事精华,快乐减压！"/>
<meta http-equiv="mobile-agent" content="format=xhtml;url=//www.qiushibaike.com/hot/">
<meta http-equiv="mobile-agent" content="format=html5;url=//www.qiushibaike.com/hot/">




<meta name="robots" content="noarchive">
<link href="//static.qiushibaike.com/css/dist/web/app.min.css?v=1a44fd15c6e802cc1ab5953bd398eea8" media="screen, projection" rel="stylesheet" type="text/css"/>
<script type="text/javascript">
// Baidu Automatic push content
var _hmt = _hmt || [];
(function() {
var hm = document.createElement("script");
hm.src = "https://hm.baidu.com/hm.js?2670efbdd59c7e3ed3749b458cafaa37";
var s = document.getElementsByTagName("script")[0];
s.parentNode.insertBefore(hm, s);
})();
// 收集运营上缓存证据
window.config = {
'user_time': '2018-12-12 14:10:10',
'version': '2017-09-04 14:36'
}
</script>
</head>
<body>



<div id="header" class="head">
<div class="content-block">
<div class="logo" id="hd_logo">
<a href="/"><h1>糗事百科</h1></a>
</div>
<div id="menu" class="menu-bar menu clearfix" style="margin:0 10px">
<a  href="/" target="_blank" rel="nofollow">热门</a>
<a  id="highlight"  href="/hot/" target="_blank">24小时</a>
<a  href="/imgrank/" target="_blank">热图</a>
<a  href="/text/" target="_blank">文字</a>
<a  href="/history/" target="_blank">穿越</a>
<a  href="/pic/" target="_blank">糗图</a>
<a  href="/textnew/" target="_blank">新鲜</a>

<!--<a href="http://www.youliaodao.cn" target="_blank" rel="nofollow">百科</a>-->
</div>
<div class="userbar clearfix hidden">
<div class="login hidden">
<a href="/my" class="username" id="uname" rel="nofollow"></a>
</div>
<div class="logout">
<a href="javascript:void(0);" class="fn-signin-required logintop" id='logintop' rel="nofollow" style="font-size:16.5px;">登录</a>
</div>
</div>
</div>
</div>



<div id="content" class="main">
<div class="content-block clearfix">
<!-- 暂停更新提示 -->
<!-- <img src="/static/images/banner.png" alt="" style="width: 100%; margin: 16px 0 0; display: block"> -->

<div id="content-left" class="col1">








<div class="article block untagged mb15 typs_long" id='qiushi_tag_121330243'>


<div class="author clearfix">
<a href="/users/30528937/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3052/30528937/thumb/20181110093251.jpg?imageView2/1/w/90/h/90" alt="恨钱不成山">
</a>
<a href="/users/30528937/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
恨钱不成山
</h2>
</a>
<div class="articleGender manIcon">30</div>
</div>

<a href="/article/121330243" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


公司个同事，36岁，未婚。前几天公司公司聚餐，哥几个喝的都有点多，新来的同事小徐问了一句：杨哥你都一把年纪了，咋还不结婚，你想找个什么样子的嫂子，说出来，小弟帮你物色着。老杨借着酒劲，慢吞吞的说道：也没多大要求，只要有份正当职业，家里有房子的，不用催着我买，最好自己有车，温柔贤惠是必不可少的，长相嘛，带的出去就行……二货小徐回了句:杨哥，这个忙弟弟恐怕是帮不了你了，您这是打算结婚就出个屌啊……

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">8406</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121330243" data-share="/article/121330243" id="c-121330243" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">167</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121330243" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121330243" class="up">
<a href="javascript:voting(121330243,1)" class="voting" data-article="121330243" id="up-121330243" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">8449</span>
</a>
</li>
<li id="vote-dn-121330243" class="down">
<a href="javascript:voting(121330243,-1)" class="voting" data-article="121330243" id="dn-121330243" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-43</span>
</a>
</li>
<li class="comments">
<a href="/article/121330243" id="c-121330243" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121330243" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">中妖毒鸡汤：</span>
<div class="main-text">
一，女，二，不是神经病，三，不是反革命。✌
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


225

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121338021'>


<div class="author clearfix">
<a href="/users/29314260/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/2931/29314260/thumb/20181208113550.jpg?imageView2/1/w/90/h/90" alt="贝格格*">
</a>
<a href="/users/29314260/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
贝格格*
</h2>
</a>
<div class="articleGender womenIcon">20</div>
</div>

<a href="/article/121338021" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


去参加表弟婚礼，看到表姐的一对双胞胎女儿，问她们“你俩谁是姐姐，？”<br/>个子矮的那个举手说我是姐姐，，我“宝贝儿，你咋比妹妹还矮呀，”<br/>小丫头不开心了“高矮和胖瘦美丑一样，不是人可以选择的，就像你和我妈妈是表姐妹，我妈妈又瘦有好看，你呢，自己照照镜子去吧。。”<br/>我……

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">1541</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121338021" data-share="/article/121338021" id="c-121338021" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">29</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121338021" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121338021" class="up">
<a href="javascript:voting(121338021,1)" class="voting" data-article="121338021" id="up-121338021" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1547</span>
</a>
</li>
<li id="vote-dn-121338021" class="down">
<a href="javascript:voting(121338021,-1)" class="voting" data-article="121338021" id="dn-121338021" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-6</span>
</a>
</li>
<li class="comments">
<a href="/article/121338021" id="c-121338021" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121338021" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">胖香：</span>
<div class="main-text">
你这猪八戒照镜子去吧！
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


28

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121337991'>


<div class="author clearfix">
<a href="/users/33491754/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3349/33491754/thumb/20181204153354.jpg?imageView2/1/w/90/h/90" alt="我是煮茶">
</a>
<a href="/users/33491754/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
我是煮茶
</h2>
</a>
<div class="articleGender manIcon">33</div>
</div>

<a href="/article/121337991" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


和老婆出来走走，冷风一吹，老婆缩了缩脖子。<br/>我站在她面前，给她挡住风，帮她把羽绒服拉链拉高点。<br/>老婆紧紧握住我的手，眼泪刷的就下来了，我：“我应该做的！”<br/>老婆：“ 拉链头卡到我脖子了...”

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">1385</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121337991" data-share="/article/121337991" id="c-121337991" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">17</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121337991" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121337991" class="up">
<a href="javascript:voting(121337991,1)" class="voting" data-article="121337991" id="up-121337991" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1388</span>
</a>
</li>
<li id="vote-dn-121337991" class="down">
<a href="javascript:voting(121337991,-1)" class="voting" data-article="121337991" id="dn-121337991" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-3</span>
</a>
</li>
<li class="comments">
<a href="/article/121337991" id="c-121337991" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121337991" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">逍遥ベ半粒糖：</span>
<div class="main-text">
衣服太瘦了，老婆双下巴，还有，楼主为什么不给老婆买围巾？
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


17

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121300362'>


<div class="author clearfix">
<a href="/users/37883273/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3788/37883273/thumb/20180805220452.jpg?imageView2/1/w/90/h/90" alt="半夜提枪就">
</a>
<a href="/users/37883273/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
半夜提枪就
</h2>
</a>
<div class="articleGender manIcon">99</div>
</div>

<a href="/article/121300362" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


小区电梯里，一少妇抱着小孩和我四目相对， 气氛有点尴尬。<br/>我为缓和气氛说：上次见你还大着肚子，一眨眼小家伙这么大了。<br/>少妇狐疑的说：你见过我？我第一次来，再说这不是我小孩，是我姐的！<br/>气氛好像更尴尬了！

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">6922</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121300362" data-share="/article/121300362" id="c-121300362" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">54</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121300362" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121300362" class="up">
<a href="javascript:voting(121300362,1)" class="voting" data-article="121300362" id="up-121300362" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">6950</span>
</a>
</li>
<li id="vote-dn-121300362" class="down">
<a href="javascript:voting(121300362,-1)" class="voting" data-article="121300362" id="dn-121300362" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-28</span>
</a>
</li>
<li class="comments">
<a href="/article/121300362" id="c-121300362" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121300362" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">胖香：</span>
<div class="main-text">
耍个流氓还废劲搭什么话！
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


105

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_old" id='qiushi_tag_116179073'>


<div class="author clearfix">
<a href="/users/30605174/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3060/30605174/thumb/20151116225731.jpg?imageView2/1/w/90/h/90" alt="忘川的星星">
</a>
<a href="/users/30605174/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
忘川的星星
</h2>
</a>
<div class="articleGender womenIcon">28</div>
</div>

<a href="/article/116179073" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


大白作为一只狗有一米多高，家里还有一牛奶色小小猫一只。每天都和小猫争宠，总是偷偷的用他硕大的狗嘴叼起小猫扔掉。每次都离家很远。有一次老妈买菜回来发现大白叼着小猫扔到街道上的垃圾桶旁！被老妈救了回来！狠狠k了大白一顿！也没起什么用。直到有一天我放学回家看见大白叼着小猫往路边的粑粑上扔！！！！！！我觉得我要做些什么了！这只心机狗！！！

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">1079</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/116179073" data-share="/article/116179073" id="c-116179073" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">24</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_116179073" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-116179073" class="up">
<a href="javascript:voting(116179073,1)" class="voting" data-article="116179073" id="up-116179073" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1140</span>
</a>
</li>
<li id="vote-dn-116179073" class="down">
<a href="javascript:voting(116179073,-1)" class="voting" data-article="116179073" id="dn-116179073" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-61</span>
</a>
</li>
<li class="comments">
<a href="/article/116179073" id="c-116179073" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121337807'>


<div class="author clearfix">
<a href="/users/26217894/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/2621/26217894/thumb/20181209042528.jpg?imageView2/1/w/90/h/90" alt="聊天不撩妹子">
</a>
<a href="/users/26217894/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
聊天不撩妹子
</h2>
</a>
<div class="articleGender manIcon">53</div>
</div>

<a href="/article/121337807" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


帮客户换个淋浴龙头，进门发现女主人穿的睡衣，一眼就能看出她里面没穿  小衣服的。<br/><br/>正换着龙头时女主人过来跟我说，龙头换好到她房间去一趟。<br/><br/>我脑海里立马想到网上看到的，修电脑被女主人浅了画面。我头脑高速运转想着如何拒绝她。<br/>：老师傅你帮查一下这开关怎么经常开了灯不亮。<br/>我想多了 [捂脸][捂脸][捂脸][捂脸][捂脸]

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">1391</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121337807" data-share="/article/121337807" id="c-121337807" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">36</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121337807" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121337807" class="up">
<a href="javascript:voting(121337807,1)" class="voting" data-article="121337807" id="up-121337807" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1400</span>
</a>
</li>
<li id="vote-dn-121337807" class="down">
<a href="javascript:voting(121337807,-1)" class="voting" data-article="121337807" id="dn-121337807" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-9</span>
</a>
</li>
<li class="comments">
<a href="/article/121337807" id="c-121337807" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121337807" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">奔跑的小土狼：</span>
<div class="main-text">
进去了没“进去”
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


32

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121337933'>


<div class="author clearfix">
<a href="/users/32215536/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3221/32215536/thumb/20181122212921.jpg?imageView2/1/w/90/h/90" alt="吃了两碗又盛">
</a>
<a href="/users/32215536/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
吃了两碗又盛
</h2>
</a>
<div class="articleGender manIcon">39</div>
</div>

<a href="/article/121337933" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


我觉得说的对，你觉得呢？<br/>刚结婚，争夺家庭话语权，吵架是正常的，两三年过去，家里谁说了算已经定了，这样就不吵架了。为啥女的一般能赢？因为这段时间，女的怀孕了，男的惹不起，十个月过去了，男的已经习惯了奴隶的生活。所以你仔细看，两口子离婚，十有八九那男的特别硬气。——抖哥

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">1705</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121337933" data-share="/article/121337933" id="c-121337933" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">28</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121337933" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121337933" class="up">
<a href="javascript:voting(121337933,1)" class="voting" data-article="121337933" id="up-121337933" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1714</span>
</a>
</li>
<li id="vote-dn-121337933" class="down">
<a href="javascript:voting(121337933,-1)" class="voting" data-article="121337933" id="dn-121337933" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-9</span>
</a>
</li>
<li class="comments">
<a href="/article/121337933" id="c-121337933" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121337933" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">胖香：</span>
<div class="main-text">
抖哥为什么抖？跪的时间久！
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


26

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121337952'>


<div class="author clearfix">
<a href="/users/33542137/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3354/33542137/thumb/20180907124011.jpg?imageView2/1/w/90/h/90" alt="王云（笨笨）">
</a>
<a href="/users/33542137/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
王云（笨笨）
</h2>
</a>
<div class="articleGender womenIcon">25</div>
</div>

<a href="/article/121337952" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


下雪天，路上结冰，我一路打着出溜滑去上班，滑着滑着刹不住了，咣当追尾了一辆公交车……然后把胸撞小了……也不知道保险公司能不能负责……

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">1461</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121337952" data-share="/article/121337952" id="c-121337952" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">88</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121337952" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121337952" class="up">
<a href="javascript:voting(121337952,1)" class="voting" data-article="121337952" id="up-121337952" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1474</span>
</a>
</li>
<li id="vote-dn-121337952" class="down">
<a href="javascript:voting(121337952,-1)" class="voting" data-article="121337952" id="dn-121337952" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-13</span>
</a>
</li>
<li class="comments">
<a href="/article/121337952" id="c-121337952" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121337952" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">醉酒舞剑砍疯子.：</span>
<div class="main-text">
我不信，除非我摸摸
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


15

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121335845'>


<div class="author clearfix">
<a href="/users/30523551/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3052/30523551/thumb/20181208234521.jpg?imageView2/1/w/90/h/90" alt="秋心不凉">
</a>
<a href="/users/30523551/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
秋心不凉
</h2>
</a>
<div class="articleGender manIcon">32</div>
</div>

<a href="/article/121335845" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


不好意思跟哥们开口借钱，弄了个女号，被他附近人搜到了。因为比较了解他，两人越聊越嗨，这货想看照片，就网上弄组美女照片发给他，还找了几张生活照，变声器语音都是经常的。忽悠了几天，表达了一下缺钱用，这货立马给我转了1314，然后我就把号扔了。<br/>过了几天，这小子难受来找我喝酒，结果我俩都喝大了，不小心说出了真相...

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">3102</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121335845" data-share="/article/121335845" id="c-121335845" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">67</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121335845" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121335845" class="up">
<a href="javascript:voting(121335845,1)" class="voting" data-article="121335845" id="up-121335845" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">3122</span>
</a>
</li>
<li id="vote-dn-121335845" class="down">
<a href="javascript:voting(121335845,-1)" class="voting" data-article="121335845" id="dn-121335845" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-20</span>
</a>
</li>
<li class="comments">
<a href="/article/121335845" id="c-121335845" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121335845" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">日丽贤：</span>
<div class="main-text">
这是钱的事吗？这是一屁股帐
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


61

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_old" id='qiushi_tag_116177656'>


<div class="author clearfix">
<span style="height: 35px">
<img src="//static.qiushibaike.com/images/thumb/anony.png?v=b61e7f5162d14b7c0d5f419cd6649c87" alt="匿名用户">
</span>
<span>
<h2>匿名用户</h2>
</span>
<!-- <div class="articleGender manIcon">32</div> -->
</div>

<a href="/article/116177656" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


总是看遍世态炎凉，才能做到静心，原来的激情，不是我们变了，是这个现实社会让我们的激情散了，原来总以为世界没有多大，也没有多少诱惑，慢慢的长大，才开始佩服那些已经生活在这个世间这么久的别人。慢慢的长大，不是主动失去了纯真，而且不得不丢弃它，不然别人总会把你当做异类。或者人生百态，每一个人都是受害者，不要去怪别人那么多，只有适应了，才能保护自己。

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">108</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/116177656" data-share="/article/116177656" id="c-116177656" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">0</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_116177656" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-116177656" class="up">
<a href="javascript:voting(116177656,1)" class="voting" data-article="116177656" id="up-116177656" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">120</span>
</a>
</li>
<li id="vote-dn-116177656" class="down">
<a href="javascript:voting(116177656,-1)" class="voting" data-article="116177656" id="dn-116177656" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-12</span>
</a>
</li>
<li class="comments">
<a href="/article/116177656" id="c-116177656" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121335592'>


<div class="author clearfix">
<a href="/users/26217894/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/2621/26217894/thumb/20181209042528.jpg?imageView2/1/w/90/h/90" alt="聊天不撩妹子">
</a>
<a href="/users/26217894/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
聊天不撩妹子
</h2>
</a>
<div class="articleGender manIcon">53</div>
</div>

<a href="/article/121335592" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


星期天正准备美美的睡个回笼觉。老婆一大早就把我叫醒了。<br/>问她干啥呢？难得一天休息让我多睡一会不行吗？<br/>她说：没啥事，就是让你知道每次半夜三更把我叫醒有多讨厌。<br/>我。。。。。。

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">1662</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121335592" data-share="/article/121335592" id="c-121335592" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">28</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121335592" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121335592" class="up">
<a href="javascript:voting(121335592,1)" class="voting" data-article="121335592" id="up-121335592" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1669</span>
</a>
</li>
<li id="vote-dn-121335592" class="down">
<a href="javascript:voting(121335592,-1)" class="voting" data-article="121335592" id="dn-121335592" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-7</span>
</a>
</li>
<li class="comments">
<a href="/article/121335592" id="c-121335592" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121335592" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">胖香：</span>
<div class="main-text">
报复！真是赤果果的报复
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


17

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121334827'>


<div class="author clearfix">
<a href="/users/25382466/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/2538/25382466/thumb/20181210232434.jpg?imageView2/1/w/90/h/90" alt="安瑾初">
</a>
<a href="/users/25382466/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
安瑾初
</h2>
</a>
<div class="articleGender manIcon">17</div>
</div>

<a href="/article/121334827" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


缘，妙不可言

</span>

</div>
</a>
<!-- 图片或gif -->



<div class="thumb">

<a href="/article/121334827" target="_blank">
<img src="//pic.qiushibaike.com/system/pictures/12133/121334827/medium/R8N0TU8CQBKNKVAD.jpg" alt="糗事#121334827" class="illustration" width="100%" height="auto">
</a>
</div>


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">2927</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121334827" data-share="/article/121334827" id="c-121334827" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">41</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121334827" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121334827" class="up">
<a href="javascript:voting(121334827,1)" class="voting" data-article="121334827" id="up-121334827" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">2946</span>
</a>
</li>
<li id="vote-dn-121334827" class="down">
<a href="javascript:voting(121334827,-1)" class="voting" data-article="121334827" id="dn-121334827" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-19</span>
</a>
</li>
<li class="comments">
<a href="/article/121334827" id="c-121334827" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121334827" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">圖文君：</span>
<div class="main-text">
我今年也这样干，要是男的接我回来就打死楼主
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


62

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121335055'>


<div class="author clearfix">
<a href="/users/34246786/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3424/34246786/thumb/20181208211338.jpg?imageView2/1/w/90/h/90" alt="老巫婆～～">
</a>
<a href="/users/34246786/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
老巫婆～～
</h2>
</a>
<div class="articleGender womenIcon">22</div>
</div>

<a href="/article/121335055" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


一大早老公就在我耳边吹气，让我想办法帮他给公司里请假。<br/>也不知道这辈子是不是欠他的，他只要在我面前软言软语，我就特别心软。<br/>无奈之下我只能含情脉脉的对老公说:“请假的事包在我身上，但是你要先满 足 我一个 要 求！”<br/>老公立马翻身下床，一边穿衣服一边说:“还是工作要紧！”

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">2875</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121335055" data-share="/article/121335055" id="c-121335055" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">54</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121335055" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121335055" class="up">
<a href="javascript:voting(121335055,1)" class="voting" data-article="121335055" id="up-121335055" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">2894</span>
</a>
</li>
<li id="vote-dn-121335055" class="down">
<a href="javascript:voting(121335055,-1)" class="voting" data-article="121335055" id="dn-121335055" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-19</span>
</a>
</li>
<li class="comments">
<a href="/article/121335055" id="c-121335055" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121335055" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">爱新觉罗.黄瓜：</span>
<div class="main-text">
你万一给我弄骨折了咋办？所以上班才最安全的
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


36

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121306097'>


<div class="author clearfix">
<a href="/users/28831688/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/2883/28831688/thumb/20181027213335.jpg?imageView2/1/w/90/h/90" alt="流星蝴蝶剑！">
</a>
<a href="/users/28831688/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
流星蝴蝶剑！
</h2>
</a>
<div class="articleGender womenIcon">100</div>
</div>

<a href="/article/121306097" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


下午带儿子去公园划船，到湖中心时，看见有两只鸭在游，儿子兴奋地让我快点追上它们，结果还没等船靠近，那两只窜出水面就飞远了!看来不是鸭子。<br/>我们上岸后，儿子对老板说：老板，你教我怎么养会飞的鸭子吧？我让我妈妈陪你唱歌，她唱歌可好听了!

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">1447</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121306097" data-share="/article/121306097" id="c-121306097" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">23</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121306097" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121306097" class="up">
<a href="javascript:voting(121306097,1)" class="voting" data-article="121306097" id="up-121306097" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1454</span>
</a>
</li>
<li id="vote-dn-121306097" class="down">
<a href="javascript:voting(121306097,-1)" class="voting" data-article="121306097" id="dn-121306097" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-7</span>
</a>
</li>
<li class="comments">
<a href="/article/121306097" id="c-121306097" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121306097" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">捉鱼不抓虾：</span>
<div class="main-text">
吹啦弹唱，样样精通！
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


15

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_old" id='qiushi_tag_116177432'>


<div class="author clearfix">
<a href="/users/31486447/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3148/31486447/thumb/20160403081818.jpg?imageView2/1/w/90/h/90" alt="乐果果果～">
</a>
<a href="/users/31486447/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
乐果果果～
</h2>
</a>
<div class="articleGender manIcon">28</div>
</div>

<a href="/article/116177432" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


老板叫庄沛根（装培根），我只能想到豆腐皮，你还能想到啥？

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">147</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/116177432" data-share="/article/116177432" id="c-116177432" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">2</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_116177432" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-116177432" class="up">
<a href="javascript:voting(116177432,1)" class="voting" data-article="116177432" id="up-116177432" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">157</span>
</a>
</li>
<li id="vote-dn-116177432" class="down">
<a href="javascript:voting(116177432,-1)" class="voting" data-article="116177432" id="dn-116177432" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-10</span>
</a>
</li>
<li class="comments">
<a href="/article/116177432" id="c-116177432" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121307842'>


<div class="author clearfix">
<a href="/users/30321363/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3032/30321363/thumb/20180916195434.jpg?imageView2/1/w/90/h/90" alt="捉鱼不抓虾">
</a>
<a href="/users/30321363/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
捉鱼不抓虾
</h2>
</a>
<div class="articleGender manIcon">21</div>
</div>

<a href="/article/121307842" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


儿子刚上幼儿园那阵，我在家教他数数。<br/>我伸出五个手指让他数，无论教几遍，问他几个，都说一把！<br/>“孩子，你咋这么笨呢？”<br/>“爸，能怨我吗，你的手指长短不一样，还动来动去，我咋记得住！老师都是用粉笔让我们数！”

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">1548</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121307842" data-share="/article/121307842" id="c-121307842" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">20</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121307842" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121307842" class="up">
<a href="javascript:voting(121307842,1)" class="voting" data-article="121307842" id="up-121307842" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1559</span>
</a>
</li>
<li id="vote-dn-121307842" class="down">
<a href="javascript:voting(121307842,-1)" class="voting" data-article="121307842" id="dn-121307842" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-11</span>
</a>
</li>
<li class="comments">
<a href="/article/121307842" id="c-121307842" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121307842" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">天涯明月刀。：</span>
<div class="main-text">
你把手指弄一样长，他就数的清了
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


16

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121335224'>


<div class="author clearfix">
<a href="/users/30201529/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3020/30201529/thumb/2018062819414093.JPEG?imageView2/1/w/90/h/90" alt="道士下山会女神">
</a>
<a href="/users/30201529/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
道士下山会女神
</h2>
</a>
<div class="articleGender manIcon">100</div>
</div>

<a href="/article/121335224" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


相过两次亲，一个是姑姑介绍的，一个是我家大姐介绍的。毫无例外，两次相亲的结果，都是姑姑、我家大姐和我满口同意，就特么女方不同意。

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">1529</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121335224" data-share="/article/121335224" id="c-121335224" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">28</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121335224" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121335224" class="up">
<a href="javascript:voting(121335224,1)" class="voting" data-article="121335224" id="up-121335224" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1535</span>
</a>
</li>
<li id="vote-dn-121335224" class="down">
<a href="javascript:voting(121335224,-1)" class="voting" data-article="121335224" id="dn-121335224" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-6</span>
</a>
</li>
<li class="comments">
<a href="/article/121335224" id="c-121335224" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121335224" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">胖香：</span>
<div class="main-text">
别人相亲起码问一句有车吗有房吗？到你那里，看一眼就走[捂脸]
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


21

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121335472'>


<div class="author clearfix">
<a href="/users/34246786/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3424/34246786/thumb/20181208211338.jpg?imageView2/1/w/90/h/90" alt="老巫婆～～">
</a>
<a href="/users/34246786/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
老巫婆～～
</h2>
</a>
<div class="articleGender womenIcon">22</div>
</div>

<a href="/article/121335472" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


洗完澡刚踏出浴室，老公就急急忙忙地压上来，我转了一下眼睛，一只手挡着说：老公，明天双十二！老公停了一秒说：好，清空购物车！<br/>完事之后，老公坐在床头边抽烟边问我：老婆，你刚刚说什么？我不记得了呀！<br/>我………

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">3708</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121335472" data-share="/article/121335472" id="c-121335472" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">89</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121335472" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121335472" class="up">
<a href="javascript:voting(121335472,1)" class="voting" data-article="121335472" id="up-121335472" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">3720</span>
</a>
</li>
<li id="vote-dn-121335472" class="down">
<a href="javascript:voting(121335472,-1)" class="voting" data-article="121335472" id="dn-121335472" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-12</span>
</a>
</li>
<li class="comments">
<a href="/article/121335472" id="c-121335472" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121335472" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">恶霸张：</span>
<div class="main-text">
打他，肯定是装的，三秒前的事不可能忘这么快
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


117

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121336818'>


<div class="author clearfix">
<a href="/users/31792183/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3179/31792183/thumb/20181211222637.jpg?imageView2/1/w/90/h/90" alt="<落落清欢>">
</a>
<a href="/users/31792183/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
&lt;落落清欢&…
</h2>
</a>
<div class="articleGender womenIcon">25</div>
</div>

<a href="/article/121336818" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


刚买了双鞋，问哥哥好不好看。<br/>哥哥说:好看，在哪买的？<br/>我:就步行街那家，那个女老板你认识的，她说她有你微信，还给我打折了呢。<br/>哥哥说:不可能，我微信从不加女的，而且我从来没有女性朋友。<br/>正纳闷哥哥说话好奇怪，嫂子就从门口回来了……

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">1416</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121336818" data-share="/article/121336818" id="c-121336818" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">13</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121336818" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121336818" class="up">
<a href="javascript:voting(121336818,1)" class="voting" data-article="121336818" id="up-121336818" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1425</span>
</a>
</li>
<li id="vote-dn-121336818" class="down">
<a href="javascript:voting(121336818,-1)" class="voting" data-article="121336818" id="dn-121336818" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-9</span>
</a>
</li>
<li class="comments">
<a href="/article/121336818" id="c-121336818" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121336818" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">肖倾城：</span>
<div class="main-text">
预判准确，你哥求生意识超强
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


32

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_old" id='qiushi_tag_116177810'>


<div class="author clearfix">
<a href="/users/12786176/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/1278/12786176/thumb/20141104183211.jpg?imageView2/1/w/90/h/90" alt="榆树新冰峰">
</a>
<a href="/users/12786176/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
榆树新冰峰
</h2>
</a>
<div class="articleGender manIcon">27</div>
</div>

<a href="/article/116177810" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


………………哥几个哥几个…………床上等你，解锁更多姿势

</span>

</div>
</a>
<!-- 图片或gif -->



<div class="thumb">

<a href="/article/116177810" target="_blank">
<img src="//pic.qiushibaike.com/system/pictures/11617/116177810/medium/app116177810.jpg" alt="糗事#116177810" class="illustration" width="100%" height="auto">
</a>
</div>


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">113</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/116177810" data-share="/article/116177810" id="c-116177810" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">0</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_116177810" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-116177810" class="up">
<a href="javascript:voting(116177810,1)" class="voting" data-article="116177810" id="up-116177810" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">124</span>
</a>
</li>
<li id="vote-dn-116177810" class="down">
<a href="javascript:voting(116177810,-1)" class="voting" data-article="116177810" id="dn-116177810" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-11</span>
</a>
</li>
<li class="comments">
<a href="/article/116177810" id="c-116177810" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121335751'>


<div class="author clearfix">
<a href="/users/35959614/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3595/35959614/thumb/20181203204514.jpg?imageView2/1/w/90/h/90" alt="雷霆万钧～">
</a>
<a href="/users/35959614/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
雷霆万钧～
</h2>
</a>
<div class="articleGender manIcon">28</div>
</div>

<a href="/article/121335751" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


赶一天一趟的中巴车回老家村里，车上人爆满，好不容易挤上去，车要开了，一个大叔站在车门边，冲着司机大声说：哎，老李啊，咱们刚刚一起吃饭，你比我还多喝了二两，我都觉得晕了，你还能开车，果然你酒量比我好啊！<br/>只见刚刚还爆满的车瞬间就空了，那个大叔慢悠悠地上了车，冲一脸茫然的司机说：哎呀不好意思，喝多了，认错人了！

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">2476</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121335751" data-share="/article/121335751" id="c-121335751" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">22</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121335751" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121335751" class="up">
<a href="javascript:voting(121335751,1)" class="voting" data-article="121335751" id="up-121335751" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">2481</span>
</a>
</li>
<li id="vote-dn-121335751" class="down">
<a href="javascript:voting(121335751,-1)" class="voting" data-article="121335751" id="dn-121335751" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-5</span>
</a>
</li>
<li class="comments">
<a href="/article/121335751" id="c-121335751" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121335751" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">晓颜诺诺～：</span>
<div class="main-text">
把大家吓得下了车，大叔想坐哪坐哪了
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


35

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121306610'>


<div class="author clearfix">
<a href="/users/30321363/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3032/30321363/thumb/20180916195434.jpg?imageView2/1/w/90/h/90" alt="捉鱼不抓虾">
</a>
<a href="/users/30321363/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
捉鱼不抓虾
</h2>
</a>
<div class="articleGender manIcon">21</div>
</div>

<a href="/article/121306610" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


这几天一直到处跑着交税，连续开车有点困，就让公司一员工跟着，我困的时候陪我聊聊天。<br/>今天中午的时候，开车去拉布大林，温度有点回升，开着暖风，不知不觉竟然睡着啦！<br/>老天眷顾，突然一个激灵猛然醒来，方向把的挺牢，路也直。但也吓的一身冷汗。<br/>我问那小伙，你看我睡着了，你怎么不喊我？<br/>“我看你睡的那么香，不忍心喊你，你要再晚会醒，我也睡着啦！”

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">2517</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121306610" data-share="/article/121306610" id="c-121306610" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">37</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121306610" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121306610" class="up">
<a href="javascript:voting(121306610,1)" class="voting" data-article="121306610" id="up-121306610" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">2537</span>
</a>
</li>
<li id="vote-dn-121306610" class="down">
<a href="javascript:voting(121306610,-1)" class="voting" data-article="121306610" id="dn-121306610" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-20</span>
</a>
</li>
<li class="comments">
<a href="/article/121306610" id="c-121306610" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121306610" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">鱼歌浅唱：</span>
<div class="main-text">
你同事心真大啊！……是不是有点Sha？
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


65

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121302083'>


<div class="author clearfix">
<a href="/users/9214729/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/921/9214729/thumb/20181005115453.jpg?imageView2/1/w/90/h/90" alt="好吃的焦糖饼干～">
</a>
<a href="/users/9214729/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
好吃的焦糖饼干～
</h2>
</a>
<div class="articleGender womenIcon">85</div>
</div>

<a href="/article/121302083" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


我哥带侄子去澡堂子洗澡。没一会儿，侄子哭着回来了：洗澡时，我问了我爸爸一个问题，他就踹我……<br/>嫂子：你问啥了？<br/>侄子一脸委屈：我问爸爸，你为什么没有别人长……

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">5892</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121302083" data-share="/article/121302083" id="c-121302083" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">79</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121302083" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121302083" class="up">
<a href="javascript:voting(121302083,1)" class="voting" data-article="121302083" id="up-121302083" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">5917</span>
</a>
</li>
<li id="vote-dn-121302083" class="down">
<a href="javascript:voting(121302083,-1)" class="voting" data-article="121302083" id="dn-121302083" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-25</span>
</a>
</li>
<li class="comments">
<a href="/article/121302083" id="c-121302083" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121302083" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">爱新觉罗.黄瓜：</span>
<div class="main-text">
嫂子也委屈哭了
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


110

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_121335124'>


<div class="author clearfix">
<a href="/users/17221979/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/1722/17221979/thumb/20180524141023.JPEG?imageView2/1/w/90/h/90" alt="挖鼻孔的老虎">
</a>
<a href="/users/17221979/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
挖鼻孔的老虎
</h2>
</a>
<div class="articleGender manIcon">101</div>
</div>

<a href="/article/121335124" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


有家洗脚店要装修，我去量尺寸、谈条件，一直倒腾到晚上九点，出来时太累就打了出租。<br/>回到小区门口下车，遇到老婆在买烧烤，她走过来问司机：“师傅，他在哪里上车的？”<br/>司机说：“新华书店。”然后一踩油门走了。

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">8094</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/121335124" data-share="/article/121335124" id="c-121335124" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">99</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_121335124" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-121335124" class="up">
<a href="javascript:voting(121335124,1)" class="voting" data-article="121335124" id="up-121335124" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">8120</span>
</a>
</li>
<li id="vote-dn-121335124" class="down">
<a href="javascript:voting(121335124,-1)" class="voting" data-article="121335124" id="dn-121335124" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-26</span>
</a>
</li>
<li class="comments">
<a href="/article/121335124" id="c-121335124" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/121335124" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">醉酒提剑捉泥鳅：</span>
<div class="main-text">
还是男人了解男人。
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


241

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_old" id='qiushi_tag_116177937'>


<div class="author clearfix">
<a href="/users/20062231/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/2006/20062231/thumb/default_avatar.jpg?imageView2/1/w/90/h/90" alt="随便喝一杯">
</a>
<a href="/users/20062231/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
随便喝一杯
</h2>
</a>
<div class="articleGender manIcon">48</div>
</div>

<a href="/article/116177937" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


糗虫们闲时还是点点糗百里的广告吧，免费的糗百也要生存啊

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">134</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/116177937" data-share="/article/116177937" id="c-116177937" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">1</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_116177937" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-116177937" class="up">
<a href="javascript:voting(116177937,1)" class="voting" data-article="116177937" id="up-116177937" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">149</span>
</a>
</li>
<li id="vote-dn-116177937" class="down">
<a href="javascript:voting(116177937,-1)" class="voting" data-article="116177937" id="dn-116177937" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-15</span>
</a>
</li>
<li class="comments">
<a href="/article/116177937" id="c-116177937" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>





<!-- 全局翻页组件 -->

<ul class="pagination">


<li>
<span class="current" >
1
</span>
</li>




<li>
<a href="/hot/page/2/" rel="nofollow">
<!--<a href="/hot/page/2/" rel="nofollow">-->
<span class="page-numbers">
2
</span>
</a>
</li>



<li>
<a href="/hot/page/3/" rel="nofollow">
<!--<a href="/hot/page/3/" rel="nofollow">-->
<span class="page-numbers">
3
</span>
</a>
</li>



<li>
<a href="/hot/page/4/" rel="nofollow">
<!--<a href="/hot/page/4/" rel="nofollow">-->
<span class="page-numbers">
4
</span>
</a>
</li>



<li>
<a href="/hot/page/5/" rel="nofollow">
<!--<a href="/hot/page/5/" rel="nofollow">-->
<span class="page-numbers">
5
</span>
</a>
</li>



<li>
<span class="dots">
…
</span>
</li>


<li>
<a href="/hot/page/13/" rel="nofollow">
<!--<a href="/hot/page/13/" rel="nofollow">-->
<span class="page-numbers">
13
</span>
</a>
</li>


<li>
<a href="/hot/page/2/" rel="nofollow">
<!--<a href="/hot/page/2/" rel="nofollow">-->
<span class="next">
下一页
</span>
</a>
</li>

</ul>


</div>



<div class="col2">
<div id="sidebar" class="sidebar">

<div class="shopwindow">
<!-- 55736473：web-右侧悬浮-up 类型：固定 尺寸：300x250-->
<!-- 新广告代码：2017-05-03 -->
<!-- <script type="text/javascript">
document.write('<a style="display:none!important" id="tanx-a-mm_108378320_8760716_29674533"></a>');
tanx_s = document.createElement("script");
tanx_s.type = "text/javascript";
tanx_s.charset = "gbk";
tanx_s.id = "tanx-s-mm_108378320_8760716_29674533";
tanx_s.async = true;
tanx_s.src = "https://phs.tanx.com/ex?i=mm_108378320_8760716_29674533";
tanx_h = document.getElementsByTagName("head")[0];
if(tanx_h)tanx_h.insertBefore(tanx_s,tanx_h.firstChild);
</script> -->
<!-- <script type="text/javascript">
var cpro_id = "u693365";
</script>
<script type="text/javascript" src="https://cpro.baidustatic.com/cpro/ui/c.js"></script> -->
<script>
document.write('<script src="//becode.qiushibaike.com/common/e9w7.js?kfxohnx=go" type="text/javascript"><\/script>');
</script>
</div>

<div class="shopwindow" id="listAd2">
<!-- 55736473：web-右侧悬浮-up 类型：固定 尺寸：300x250-->
<!-- 新广告代码：2017-05-03 -->
<!-- <script type="text/javascript">
/*右侧2*/
// var cpro_id = "u693365";
// document.write('<script type="text/javascript" src="https://cpro.baidustatic.com/cpro/ui/c.js"><\/script>');
// 2017-5-23 修改
// FTAPI_slotid = 1026761;FTAPI_sync = true
// document.write('<script src="//pic.fastapi.net/sdk/js/a.js" charset="utf-8"><\/script>')
</script> -->
<script type="text/javascript" src="//becode.qiushibaike.com/production/resource/d3nkw.js?m=hgpzzge"></script>
</div>


<div class="sidebar-other">
<img src="/static/images/productlist/ctrl_d.png">
<p>把糗事百科加入收藏夹</p>
</div>
<div class="sidebar-hot clearfix" id="sidebar-qrcode">
<div class="float-left qrcode">
<img src="/static/images/web_v3/sidebar/qiubai_qrcode.png" alt="糗事百科 APP 下载二维码">
</div>
<div class="float-left btn-box">
<a href="javascript:void(0)" class="btn-download ios" onclick="window.open('https://itunes.apple.com/cn/app/id422853458?mt=8')" target="_blank">iOS 下载</a>
<a href="javascript:void(0)" class="btn-download android" onclick="window.open('http://static.qiushibaike.com/qiushibaike.apk')" target="_blank">Android 下载</a>
<p class="tips">扫码下载糗事百科app</p>
</div>
</div>
<!-- 直播下载链接 -->
<div class="sidebar-hot clearfix" id="sidebar-remix">
<a href="https://www.app-remix.com/v1/pc/living?chn=qiubai" onclick="_hmt.push(['_trackEvent', 'web-remix', 'chick']);" target="_blank">
<img src="//static.qiushibaike.com/images/web_v3/sidebar/remix_banner.gif?v=f8bbbe7ca7cd5b9314e8235d6290fb0f" alt="">
</a>
</div>
<!-- 浪人杀下载链接 -->
<!--<div class="sidebar-hot clearfix" id="sidebar-wolf">-->
<!--<img src="//static.qiushibaike.com/images/web_v3/sidebar/wolf_banner.png?v=b18dc8556489b273af99197ebcf01a1c" alt="">-->
<!--</div>-->
<div class="sidebar-hot clearfix">
<h3>爆笑糗事精选</h3>
<ul>

<li class="item">
<a href="/article/121284746" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="//pic.qiushibaike.com/system/pictures/12128/121284746/medium/UOAP3DUGQQY1IKW3.jpg?imageView2/1/w/146/h/146" alt="珍藏版曾志伟姚明合影留念"/></span>
</a>
<a href="/article/121284746" title="珍藏版曾志伟姚明合影留念" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>珍藏版曾志伟姚明合影留念</p>
</a>
</li>

<li class="item">
<a href="/article/121284507" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="//pic.qiushibaike.com/system/pictures/12128/121284507/medium/WMQG6UVBJQ2U10RB.jpg?imageView2/1/w/146/h/146" alt="结巴....."/></span>
</a>
<a href="/article/121284507" title="结巴....." rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>结巴.....</p>
</a>
</li>

<li class="item">
<a href="/article/121297582" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="//pic.qiushibaike.com/system/pictures/12129/121297582/medium/JZLEBJFXHIBQZC4Z.jpg?imageView2/1/w/146/h/146" alt="口腔科医生表示明天没有什么预约"/></span>
</a>
<a href="/article/121297582" title="口腔科医生表示明天没有什么预约" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>口腔科医生表示明天没有什么预约</p>
</a>
</li>

<li class="item">
<a href="/article/121263728" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="//pic.qiushibaike.com/system/pictures/12126/121263728/medium/2GK7A0KX4RU2C36M.jpg?imageView2/1/w/146/h/146" alt="偷拿了人家一架炮"/></span>
</a>
<a href="/article/121263728" title="偷拿了人家一架炮" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>偷拿了人家一架炮</p>
</a>
</li>

<li class="item">
<a href="/article/121239080" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="//pic.qiushibaike.com/system/pictures/12123/121239080/medium/7G69G9B4LKTSEZE8.jpg?imageView2/1/w/146/h/146" alt="我研究发动机"/></span>
</a>
<a href="/article/121239080" title="我研究发动机" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>我研究发动机</p>
</a>
</li>

<li class="item">
<a href="/article/121284116" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="//pic.qiushibaike.com/system/pictures/12128/121284116/medium/6OCC26T5VRX6PHT4.jpg?imageView2/1/w/146/h/146" alt="儿子立马接话"/></span>
</a>
<a href="/article/121284116" title="儿子立马接话" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>儿子立马接话</p>
</a>
</li>

<li class="item">
<a href="/article/121309505" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="//pic.qiushibaike.com/system/pictures/12130/121309505/medium/D7A2KCFZABMNJ2KD.jpg?imageView2/1/w/146/h/146" alt="教科书式操作"/></span>
</a>
<a href="/article/121309505" title="教科书式操作" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>教科书式操作</p>
</a>
</li>

<li class="item">
<a href="/article/121285524" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="//pic.qiushibaike.com/system/pictures/12128/121285524/medium/G99D32PG5ABZYBTI.jpg?imageView2/1/w/146/h/146" alt="不敢拉屎了"/></span>
</a>
<a href="/article/121285524" title="不敢拉屎了" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>不敢拉屎了</p>
</a>
</li>

</ul>
</div>
<div class="sidebar-hot clearfix" id="sidebar-tab">
<div class="tab-head">
<h3 class="active" data-type="0">热门</h3>
<h3 data-type="1">话题</h3>
<h3 data-type="2">专区</h3>
<h3 data-type="3">推荐</h3>
</div>
<div class="sidebar-tag-block tab-content0">

</div>
<div class="sidebar-tag-block tab-content1 hide">

</div>
<div class="sidebar-tag-block tab-content2 hide">


<li><i># </i><a href="/key/6462801/">广州捷普电子厂怎么样</a><i> #</i></li>

<li><i># </i><a href="/key/6486671/">健身人早上吃什么水果好</a><i> #</i></li>

<li><i># </i><a href="/key/6478484/">印度祛痘效果怎么样</a><i> #</i></li>

<li><i># </i><a href="/key/6461124/">广州港集团待遇怎么样</a><i> #</i></li>

<li><i># </i><a href="/key/6477933/">祛痘坑效果怎么样</a><i> #</i></li>

<li><i># </i><a href="/key/6466770/">深圳市希科普科技发展有限公司怎么样</a><i> #</i></li>

<li><i># </i><a href="/key/6464343/">广州的房价怎么样</a><i> #</i></li>

<li><i># </i><a href="/key/6478598/">祛痘印套装怎么样</a><i> #</i></li>

<li><i># </i><a href="/key/6476864/">深圳中天世纪怎么样</a><i> #</i></li>

<li><i># </i><a href="/key/6456333/">广州米度网络科技有限公司怎么样的</a><i> #</i></li>


</div>
<div class="sidebar-tag-block tab-content3 hide">

</div>
</div>

<div class="shopwindow" id="listAd3">
<!-- 55736473：web-右侧悬浮-up 类型：固定 尺寸：300x250-->
<!-- <script type="text/javascript">
document.write('<a style="display:none!important" id="tanx-a-mm_108378320_8760716_29640993"></a >');
tanx_s = document.createElement("script");
tanx_s.type = "text/javascript";
tanx_s.charset = "gbk";
tanx_s.id = "tanx-s-mm_108378320_8760716_29640993";
tanx_s.async = true;
tanx_s.src = "https://phs.tanx.com/ex?i=mm_108378320_8760716_29640993";
tanx_h = document.getElementsByTagName("head")[0];
if(tanx_h)tanx_h.insertBefore(tanx_s,tanx_h.firstChild);
</script> -->
<!-- 新广告代码：2017-05-03 -->
<!-- <script>
var cpro_id = "u1101312";
document.write('<script type="text/javascript" src="https://cpro.baidustatic.com/cpro/ui/c.js"><\/script>');
</script> -->
<script type="text/javascript" src="//becode.qiushibaike.com/production/klcawm.js?gb=tytyyhc"></script>
</div>

<div class="shopwindow">
<!-- 2017.10.16 注释 -->
<!-- <script type="text/javascript" src="https://s.haiyunimg.com/SSP/30169.js"></script> -->
<!-- 2017.10.16 添加 -->
<!-- <script>
var mediav_ad_pub = 'klT513_2129270';
var mediav_ad_width = '300';
var mediav_ad_height = '250';
</script>
<script type="text/javascript" language="javascript" charset="utf-8" src="//static.mediav.com/js/mvf_g2.js"></script> -->
<script type="text/javascript" src="//becode.qiushibaike.com/common/exweb.js?h=cuzuzzie"></script>
</div>

</div>
</div>



</div>
</div>


<div class="foot">
 <div class="foot-ad" id="footAd">
<!-- 68902435：web-底部固定 类型：固定 尺寸：728x90-->
<!-- 2017/2/28 注释旧的广告代码，改为使用 https 的广告 -->
<!-- <script type="text/javascript">//<![CDATA[
ac_as_id = "mm_108378320_13540554_68902435";
ac_format = 1;
ac_mode = 1;
ac_group_id = 1;
ac_server_base_url = "afpeng.alimama.com/";
//]]></script>
<script type="text/javascript" src="//afpmm.alicdn.com/g/mm/afp-cdn/JS/k.js"></script> -->
<!-- <script type="text/javascript">//<!—
google_ad_client = "ca-pub-7443704194229694";
/* IDG.CN_B2C_qiushibaike.com_HY_728x90 */
google_ad_slot = "9826878184";
google_ad_width = 728;
google_ad_height = 90;
//—>
document.write('<script type="text/javascript" src="//pagead2.googlesyndication.com/pagead/show_ads.js"><\/script>');
</script> -->
<script type="text/javascript" src="//becode.qiushibaike.com/production/s401mj.js?ezovy=frbr"></script>
</div>

<div class="foot-nav clearfix">
<div class="foot-nav-col">
<h3>
关于
</h3>
<ul>
<li>
<a href="//about.qiushibaike.com/web_jobs.html#team" target="_blank" rel="nofollow">
关于糗百
</a>
</li>
<li>
<a href="//about.qiushibaike.com/web_jobs.html#tech" target="_blank" rel="nofollow">
加入我们
</a>
</li>
<li>
<a href="//about.qiushibaike.com/web_jobs.html#contact" target="_blank" rel="nofollow">
联系方式
</a>
</li>
</ul>
</div>
<div class="foot-nav-col">
<h3>
帮助
</h3>
<ul>
<li>
<a href="//about.qiushibaike.com/feedback.html" target="_blank" rel="nofollow">
在线反馈
</a>
</li>
<li>
<a href="//about.qiushibaike.com/agreement.html" target="_blank" rel="nofollow">
用户协议
</a>
</li>
<li>
<a href="//about.qiushibaike.com/policy.html" target="_blank" rel="nofollow">
隐私政策
</a>
</li>
</ul>
</div>
<div class="foot-nav-col">
<h3>
下载
</h3>
<ul>
<li>
<a href="https://android.myapp.com/myapp/detail.htm?apkName=qsbk.app"
target="_blank" rel="external nofollow">
Android 客户端
</a>
</li>
<li>
<a href="https://itunes.apple.com/cn/app/id422853458" target="_blank" rel="external nofollow">
iPhone 客户端
</a>
</li>
</ul>
</div>
<div class="foot-nav-col">
<h3>
关注
</h3>
<ul>
<li>
<a href="#" class="foot-wechat">
微信
<div class="foot-wechat-tips">
<span class="foot-wechat-icon"></span>
手机扫描二维码关注
</div>
</a>
</li>
<li>
<a href="http://weibo.com/qiushibaike" target="_blank" rel="external nofollow">
新浪微博
</a>
</li>
<li>
<a href="http://user.qzone.qq.com/1492495058" target="_blank" rel="external nofollow">
QQ空间
</a>
</li>
</ul>
</div>
<div class="foot-nav-col">
<h3>
组织
</h3>
<ul>
<li>
<a href="http://user.qzone.qq.com/1492495058/blog/1408597608" target="_blank"
rel="external nofollow">
官方粉丝群
</a>
</li>
<li>
<a href="https://www.qiushibaike.com/users/37042475" target="_blank"
rel="external nofollow">
<img style="vertical-align: middle;height: 16px;margin-top: -2px;" src="/static/images/beian.png">
首都网警
</a>
</li>
</ul>
</div>
</div>
<div class="foot-copyrights">
<!-- <p>&copy; Qiushibaike.com 糗事百科版权所有</p>
<p>
<span>京ICP备14028348号-1</span>
<span>京ICP证140448号</span>
<span>京网文[2017]2369-247号</span>
<span>
<a style='color:#333' target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502031601" rel="nofollow"><img style='vertical-align: top;' src="/static/images/beian.png?v=d0289dc0a46fc5b15b3363ffa78cf6c7" />京公网安备11010502031601号</a>
</span>
</p>
<p style="margin-top:8px">友际无限（北京）科技有限公司</p>
<p style="margin-top:8px">
<span>互联网违法和不良信息举报电话：010-84872896</span>
<span>邮箱：kefu@qiushibaike.com</span>
</p> -->
<p>互联网ICP备案：京ICP备14028348号-1</p>
<p>
<span>广播电视节目制作经营许可证：（京）字第08319号</span>
<span>网络文化经营许可证：
<a style='color:#333' target="_blank" href="http://sq.ccm.gov.cn:80/ccnt/sczr/service/business/emark/toDetail/"
rel="nofollow">
<img src="/static/images/wenhuajingying.png?v=f5f3976cf4be787ad2be202a19d40823" style='width: 20px; height: 20px; vertical-align: top;'>京网文[2017]2369-247号</a>
</span>
</p>
<p style="margin-top: 8px">电信与信息服务业务经营许可证：京ICP证140448号</p>
<p style="margin-top: 8px"><span>营业性演出许可证：京演(机构)(2018)1940号</span></p>
<p>
<span>计算机信息网络国际联网单位备案：<a style='color:#333' target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502031601" rel="nofollow"><img style='vertical-align: top;' src="/static/images/beian.png?v=d0289dc0a46fc5b15b3363ffa78cf6c7" />京公网安备11010502031601号</a></span>
</p>
<br>
<p style="margin-top: 8px">友际无限（北京）科技有限公司</p>
<p>
<span>违法和不良信息举报电话：0755-86967540</span>
<span>邮箱：kefu@qiushibaike.com</span>
</p>
<br>
<p style="margin-top: 8px">&copy; Qiushibaike.com 糗事百科版权所有</p>
</div>
</div>


<div class="signin-box" id="login-form">
<div class="sigin-left">
<div class="signin-account clearfix">
<h4 class="social-signin-heading">社交帐号登录</h4>
<a rel="external nofollow" oauth_href href="https://open.weixin.qq.com/connect/qrconnect?appid=wx559af2d26b56c655&redirect_uri=http%3A%2F%2Fwww.qiushibaike.com%2Fnew4%2Fsession%3Fsrc%3Dwx&response_type=code&scope=snsapi_login#wechat_redirect" class="social-btn social-wechat">
使用 微信 账号</a>
<a rel="external nofollow" oauth_href href="https://api.weibo.com/oauth2/authorize?client_id=63372306&redirect_uri=http%3A%2F%2Fwww.qiushibaike.com%2Fnew4%2Fsession" class="social-btn social-weibo">
使用 微博 账号</a>
<a rel="external nofollow" oauth_href href="https://graph.qq.com/oauth2.0/authorize?which=Login&display=pc&client_id=100251437&response_type=code&redirect_uri=www.qiushibaike.com/new4/session?src=qq" class="social-btn social-qq">
使用 QQ 账号 </a>
</div>
<div class="signin-form clearfix">
<h4 class="social-signin-heading">糗事百科账号登录</h4>
<form method="post" action="/new4/session">
<input type="hidden" name="_xsrf" value="2|31f38e4e|207678186001f518f80a62c9bc46e1db|1544583587"/>
<div class="signin-section clearfix">
<input type="text" class="form-input form-input-first" name="login" placeholder="昵称或邮箱">
<input type="password" class="form-input" name="password" placeholder="密码">
<input type="checkbox" id="remember_me" name="remember_me" checked="" value="checked" style="display:none">
</div>
<div class="signin-error" id="signin-error"></div>
<button type="submit" id="form-submit" class="form-submit">登录</button>
</form>
</div>
<div class="signin-foot clearfix">
<a rel="nofollow" href="/new4/fetchpass" class="fetch-password">忘记密码?</a>
</div>
</div>
</div>

<div class="float-nav">
<a class="float-nav-backtop" href="#" rel="nofollow">
<span class="float-nav-backtop-icon"></span>
</a>
</div>

<!--[if gte IE 6]>
<script type="text/javascript" src="//static.qiushibaike.com/js/src/web/json3.js?v=3a7f66a11a09842cd7555fad039657be"></script>
<![endif]-->
<script type="text/javascript" src="//static.qiushibaike.com/js/dist/web/libs.min.js?v=bc8ddd36f0e7fed7c27f437c17f23ce0"></script>
<script type="text/javascript" src="//static.qiushibaike.com/js/dist/web/app.min.js?v=5997ad16edca8ec50a1fcc40913785a6"></script>



<script type="text/javascript">
// Google Analytics
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','https://www.google-analytics.com/analytics.js','ga');
ga('create', 'UA-8780108-1', 'auto');
ga('send', 'pageview');
</script>

<script type="text/javascript" async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<script type="text/javascript" src="https://cbjs.baidu.com/js/m.js"></script>
<script type="text/javascript">



window.broadJson = '[]'
</script>
<script type="text/javascript" src="//static.qiushibaike.com/js/dist/web/v3/adsAdmin.min.js?v=9c42f35ae43e17caf141e9d6ebe32cbb"></script>
</body>
</html>
"""

pattern = re.compile(r'<div class="content">\n<span>(.*?)</span>', re.S)   # re.S匹配时包括换行后的内容
results = re.findall(pattern, html_content)
for row in results:
    print(row)
    # pass

pattern2 = re.compile(r'<div class="author clearfix">.*?<h2>.*?</h2>', re.S)
results2 = re.findall(pattern2, html_content)
# print(results2)






# https://www.cnblogs.com/huchong/p/8290340.html
# https://www.cnblogs.com/dreamer-fish/p/3944945.html
