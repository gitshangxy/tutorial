mysql官方入门教程
===
## 步骤
1. 启动服务   shell> mysqld
2. 客户端  shell> mysql --help
3. 客户端登录  mysql -u root -p
如果服务器在另一台计算机 需要ip地址和端口参数 mysql -h 127.0.0.1 -P 3306 -u root -p
如果服务器在另一台计算机 需要ip地址
登录时指定要操作哪个数据库  mysql -u root -p 库名
4. 执行各种sql

## sql
1. select version(), current_date();
关键字大小写都行，函数可以省略(),每句分号结尾。
2. create datebase 库名;
刚连接mysql后，mysql只有几个保存系统信息的内置数据库(表信息 权限信息)我们不应该  所以动内置库。schema是逻辑上的大分块，schema下包含库。当有一个项目想保存信息时，我们需要先新建一个库 dataase下新建表，表里存信息。有些数据库中schema和database一样。
 3. use 库名 ;
 切换数据库。否则跨数据库查询需要跟命名空间。
4. show tables;  查看库下所有文件
5. 


http://www.runoob.com/python3/python3-mysql.html
https://dev.mysql.com/doc/refman/8.0/en/loading-tables.html