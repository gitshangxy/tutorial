# json和xml
### 引题
不同的编程语言有不同的数据结构。python 字典，java map。不同技术混合，服务器有的用java，有的python、php。不同电脑想互相通讯，由于数据结构只有它们语言自己知道怎么解析，其它语言不理解。需要一个各种服务器语言都理解的通用数据格式。

### 接口
接口（API Application programming interface）：不用考虑内部实现，暴露一个功能窗口，只需请求这个接口，就能获得功能。
好比医院的前台，就医者诉说症状，前台护士告诉你应该去哪个科看病。这个案例好比一个关于获取挂号信息的接口，传入的参数是患者的描述，返回的结果是 目的科室。

### json和xml
想传递处理好的信息 
```python
student = {
    'student_list' : [
        {'no':1, 'name':'小明', 'age':1, 'sex':'male'},
        {'no':2, 'name':'小王', 'age':2, 'sex':'male'},
        {'no':3, 'name':'小红', 'age':3, 'sex':'female'}
    ]
}

```

引题：不同语言和系统，python当中是中括号 列表，js数组 ，py当中字典，java map，它们之间不认识对方的数据结构。
所以客户端与服务器端传递信息，需要一个各种语言各种操作系统都认识的中间格式。
1. 字符串
2. json  。一种键值对存储格式。
```json
{
  "student_list": [
      {"no":1, "name":"小明", "age":10, "sex":"male"},
      {"no":2, "name":"小王", "age":12, "sex":"male"},
      {"no":3, "name":"小红", "age":13, "sex":"female"}
  ],
  "school_name": "智游",
  "address":"经开十五大街"
}
```
json语法，大括号括住，里面全是键值对，键用双引号括住，字符型的值双引号括住。
json键和字符串类型的值必须 双引号括住；python字典单引双引都可以。
本质字符串；c结构体。
无变量；变量。
3. xml
```xml
<?xml version="1.0" encoding="UTF-8"?>
<o>
     <address type="string">经开十五大街</address>
     <school_name type="string">智游</school_name>
     <student_list class="array">
          <e class="object">
               <age type="number">10</age>
               <name type="string">小明</name>
               <no type="number">1</no>
               <sex type="string">male</sex>
          </e>
          <e class="object">
               <age type="number">12</age>
               <name type="string">小王</name>
               <no type="number">2</no>
               <sex type="string">male</sex>
          </e>
          <e class="object">
               <age type="number">13</age>
               <name type="string">小红</name>
               <no type="number">3</no>
               <sex type="string">female</sex>
          </e>
     </student_list>
</o>
```
因为json书写方便，更接近后端语言，所以市场占有率越来越高。但xml也得认识，xml在java项目配置和一些接口中仍占有部分市场。
场景：json、xml 一是不同计算机间通讯。二是作为项目中的配置文件。
xml更适合复杂结构。json适合简单一点。

4. YAML
```YAML
#YAML格式
environments:
    dev:
        url: http://dev.bar.com
        name: Developer Setup
    prod:
        url: http://foo.bar.com
        name: My Cool App
my:
    servers:
        - dev.bar.com
        - foo.bar.com
 
```
场景：配置文件。yaml优点是目录层级比较明确。