# sqlite示例2      查询 修改 删除
import sqlite3
connect = sqlite3.connect("testsqlite.db")
cursor = connect.cursor()
# 查询表格中所有的值
cursor.execute("""
    SELECT id,name from student;
""")
student_list = cursor.fetchall()
print(student_list)
# 查询表格中某一个值
cursor.execute("""
    SELECT * FROM student WHERE name="小红";
""")
student = cursor.fetchone()
print(student)
# 查询表格中id=0的值
cursor.execute("""
    SELECT * FROM student WHERE id=0;
""")
student2 = cursor.fetchone()
print(student2)

cursor.execute("""
    SELECT * FROM student WHERE id>0;
""")
# student_list3 = cursor.fetchall()
student3 = cursor.fetchone()
# print(student_list3)
print(f'学生姓名是 {student3[1]}')
#修改表格中id等于那一行的值
cursor.execute("""
    UPDATE student3 SET name="大云" WHERE id=2;
""")
connect.commit()
# 查询表格中所有的值
cursor.execute(""" select * from student; """)
print(cursor.fetchall())

cursor.close()
connect.close()

"""
cursor.fetchall()  取回结果集，形如[(1, '小王'), (2, '小红')] 大列表，列表每一项是元组、是一行，元组里的每一项对应每一列的值。结果空返回[]。
cuesor.fetchone()  取回一条数据，形如 (2, '小红')。结果空返回None类型。如果select符合多条，返回多条结果里的一条。

cursor.fetchxxx()  方法为了节省内存和速度采取了生成器结构，只能取一次
"""

"""
sql基础语法补充：
1. 一张表一般都有一列主键，主键primary key一般名叫 id，字段类型一般为自增整数。当insert行内容时，sql语句可以不插入id列,数据库会帮你自动插入并自增auto increase
 主键不能重复，主键好处是确保数据一致性，方便查询。 如果一列为主键，那么必然非空notnull和唯一unique。

2. 如果工作中一个数据库连接实例下有多个库，那么表名要带上命名空间。例如 main， student

2. 丢弃表  drop。 跟delete关键字更加严重，delete删除某行或清空表内容，但是表结构还在,而drop是完全删除丢弃整个表，内容和结构都删除。drop table [表名]。

4. 字段被双引号括住，形如  SELECT "id","name" FROM student;   结果一样，好处是避免数据库关键字导致的错误，当数据库解释器遇到双引号时，会认为引号里的名字就是自定义的字段名而不是内置关键字。平时省事可以不加引号。


数据库概念补充：
数据库存储原理：数据按树型结构存储，查找数据时只需要对比几次就能查出来。数据量增大时，查询时间成对数慢速增长。
索引：index，目录。索引会占据一定存储空间，在数据库中以树型结构存储，建立的是目录到硬盘存储的数据的映射，就好像平时看的书籍。创建主键的那一列会自动创建索引。一般在查询经常比较的字段上创建索引（如id列、phone列）。优点大幅度提高select效率。缺点是占据更多的硬盘空间。
事务：transaction。  当有多句sql语句的时候，例如sql1 插入银行交易表一行数据金额100元、sql2 修改刚才插入的一行数据的金额为98元，但执行sql1的时候由于用户拥堵等原因执行失败，这是在执行sql2必然错误或误修改其他的正常数据。为了避免这种情况，把这两句sql都放入一个事务执行，只要一个事务中任意一条sql执行失败，那么其他已执行的sql会回到修改前状态（回滚rolling），只有当所有sql都执行成功，才会一起commit生效。简单来说，事务要么都执行，要么出错都不行。优点保证数据一致性。
"""

"""
作业一：cursor.fetchall() 默认返回每一行为元组格式[(1, '小王'), (2, '小明')] ， 百度“sqlite python dict”，设置方法的返回值为字典形式[{'id':1, 'name':小王'}, {'id':2, 'name':小明'}]

"""



