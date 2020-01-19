# [mySql分组排序](https://www.cnblogs.com/longxok/p/10980509.html)





1、建表语句

CREATE TABLE `student` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`name` varchar(50) COLLATE utf8_bin NOT NULL COMMENT '姓名',
`score` int(11) NOT NULL COMMENT '成绩,
`classid` int(11) NOT NULL COMMENT '班级',
PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='学生';

 2、插入数据

insert into student(Name, Score, ClassId) values("lqh", 60, 1);
insert into student(Name, Score, ClassId) values("cs", 99, 1);
insert into student(Name, Score, ClassId) values("wzy", 62, 1);
insert into student(Name, Score, ClassId) values("zqc", 88, 2);
insert into student(Name, Score, ClassId) values("bll", 100, 2);



3、开始玩转MySQL

查询每个班级最大分数

select max(t.score) score,t.classid from student t group by t.classid 

![img](https://img2018.cnblogs.com/blog/1387024/201906/1387024-20190605161810186-2039843382.png)

 

显然这个在实际应用中不合场景，上面只能查出每个班级的最高分，但是是谁查不到

用下面这个语句，用分组的最高分、班级去原表中去匹配，命中出结果，就是相应的学生信息：

select s.* from student s join
(select max(t.score) score,t.classid from student t group by t.classid )r
on s.classid=r.classid and s.score=r.score　　

![img](https://img2018.cnblogs.com/blog/1387024/201906/1387024-20190605161823959-1632899296.png)

最高的第一名查出来了，但是比如我们要找前3名，前5名是谁，怎么搞？group by的max函数只能取最大值，前几个怎么玩？？？

limit 3,limit 5,group 里面没有这么玩的，limit只是对查出的结果做最外层的封装

按 Ctrl+C 复制代码

按 Ctrl+C 复制代码

先给结果，但是这个我理解不了，为什么where条件为什么这样写？

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
select a.classid,a.`name`,a.score ,a.id ,b.id ,count(b.id)from student a left join student b 
on a.classid=b.classid and a.score<b.score
GROUP BY a.classid,a.`name`,a.score 

having count(b.id)<2

order by a.classid,a.score
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

上面这个SQL就好理解多了

```
select a.classid,a.`name`,a.score ,a.id ,b.id ,count(b.id)from student a left join student b 
on a.classid=b.classid and a.score<b.score
GROUP BY a.classid,a.`name`,a.score 
```

先看这个，一下子就明白了，把a表中的每个成绩都排个序，count(b.id)就是成绩的排名，0就是第一，没有比这个分数更高的，1就表示第二，只有一个比这个分数高的，依次类推

having count下 ，你要取前2名的话 having count就小于2，感觉这个好理解多了 