转移数据库 use 库名

新建  CREATE TABLE pet (
         name VARCHAR(20),
         CREATE TABLE pet (name VARCHAR(20), 
         species VARCHAR(20), 
         sex CHAR(1), 
         birth DATE, 
         death DATE);

打开 show tables;

查看  DESCRIBE pet;

添加  insert into pet values ('阿黄', '小明', '狗', 'f', '2006-06-04');
      insert into pet values ('Whisler', 'Gwen', '鸟', 'f', '2000-08-09', now() );
      insert into pet values ('阿黄', '小明', '狗', 'f', '2006-06-04', null);

修改  名为阿花的sex=f
打印  select * from pet;


输出sex=f的成员 select name,owner,sex from pet where sex='f';








