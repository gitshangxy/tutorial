create database jd1;

create database test;
select * from menagerie.pet; -- 如果没有切换数据库，查询时要声明从哪个库中的表查。


show tables;

create table shop(
  article int(4) unsigned zerofill default '0000' NOT NULL, -- 商品编号
  dealer char(20) default '' not null, -- 经销商
  price double(16,2) default '0.00' not null, -- 价格
  primary key(article,dealer)
);

insert into shop values (1,'A',3.45),(2,'B',4.66),(3,'C',3.47);

select * from shop;

select MAX(article) as max_article from shop; -- 函数

-- 子查询。 需求把最贵的商品信息查询出来
select article,dealer from shop
where price = (select max(price) from shop);

-- 分组。 需求查出每一个商品的最高价格
-- 可能出现的错误，使用函数时应注意一般都都先分组。
select min(price) from shop where article=3;
select min(price) from shop where article=1;
select article,min(price)as price from shop group by article;

-- 外键
create table person(
  id int primary key auto_increment, -- id 主键 自增
  name varchar(20) not null
);

create table shirt(
  id int primary key auto_increment,
  style varchar(20) not null,
  color varchar(20) not null,
  person_id int references person.id   -- owner列关联存储person表的id列

  -- foreign key (此表的外键列person_id) references 关联表（主键列）。
);

insert into person values (null,'南宫问迁');
insert into person values (null,'宫商角羽');
insert into person values (null,'笙枝蔓叶');


insert into shirt values (null,'羊毛衫','白',1),(null,'棉靴','黑',2),(null,'毛呢','粉',3);
insert into shirt values (null,'毛衣','黑',1),(null,'棉靴','黑',2),(null,'面包服','宝石蓝',3);

select * from person;
select * from shirt;
show create table shirt;

-- join查询
select p.name,s.style,s.color from person as p inner join shirt s on p.id = s.person_id where s.color = '白' and s.style = '羊毛衫';


-- 修改
UPDATE shirt SET color='藏青' WHERE person_id=3;


-- 删除
DELETE FROM shirt WHERE id=8;
DELETE FROM shirt WHERE id=9;
DELETE FROM shirt WHERE id=10;


select count(id) as amount,product_color from comment group by product_color;
select rate_content, append_content, rate_date from comments order by  rate_date desc;

-- 避免过多的表直接连接降低查询效率

-- 外键关系，当关联表的某一行删除，外键的值不存在时，
-- （cascade级联）有外键表的行可以跟着删除
-- （noaction不作操作）行其它字段保留不变
-- （setnull）行其他数据清空
-- （restrict）行其他字段有数据时不允许删除外键



-- 数量关系
-- 学生表 班级表 学科表 学生体检表
-- 多对一（最常见）：学生表对一个班有多个学生
-- 多对多：一个学生学多个学科，一个学科有多个学生。
-- 一对一（情况较少）：一个学生对应 学生体检表里的一行记录。


-- 房上的猫博客 https://www.cnblogs.com/lsy131479/p/8495741.html
