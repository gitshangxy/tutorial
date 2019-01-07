-- select * from student2;

-- 在student2中插入id,name项
CREATE TABLE student2(
  id INT PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(10)
);

--查找
SELECT * FROM main.student2 WHERE name="小小";  --返回某一个学生
SELECT * FROM student2 WHERE id=2;      --返回id=2的值
SELECT * FROM student2 WHERE id>0;      --返回id>0的所有值
select id,name from student2;
SELECT "id","name" FROM student2;

-- 在student2中添加项
INSERT INTO student2(id,Name) VALUES (3,'小红');


--修改
UPDATE student2 SET name="小明" WHERE id=2;


--删除student3表中的数据
delete from student3;COMMIT ;
--删除student4表格
drop table student4;


--在student2整张表中修改address
UPDATE student3 SET address="314教室";


--取出列名[id，name]
PRAGMA table_info([student2]);

