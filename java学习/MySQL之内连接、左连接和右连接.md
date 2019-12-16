# [MySQL之内连接、左连接和右连接](https://www.cnblogs.com/zhaoyini/p/join.html)







**数据表内数据如下：**

books表：                                                                         articls表：

![img](https://images2018.cnblogs.com/blog/1416057/201807/1416057-20180706155259500-344494666.png)          ![img](https://images2018.cnblogs.com/blog/1416057/201807/1416057-20180706143502248-687227976.png)

**内连接：**

**关键字：INNER JOIN**

**命令行代码如下：**

**![img](https://images2018.cnblogs.com/blog/1416057/201807/1416057-20180706144202925-1428666589.png)**

其中a.title 表示books表中的title字段，b.title表示的articles表中的字段，这行命令的意思是使用mysql中的inner join关键字来连接两张表（books表与articles表）组合两张表的字段并且返回关联字段相对应的字段（a.title=b.title）

结果如下图所示。

![img](https://images2018.cnblogs.com/blog/1416057/201807/1416057-20180706145335497-173284723.png)

 

**注意:这里也可以省略inner直接写为join,也能实现上述功能。**

**![img](https://images2018.cnblogs.com/blog/1416057/201807/1416057-20180706145447904-336109261.png)**

inner join 获取的就是两个表中的交集部分

![img](https://images2018.cnblogs.com/blog/1416057/201807/1416057-20180706153644861-1419869407.png)

**左连接：**

**关键字：LEFT JOIN**

 左表：books 右表：articles

 ![img](https://images2018.cnblogs.com/blog/1416057/201807/1416057-20180706155050512-573928743.png)

 左连接会读取左边数据表的全部数据，即使右边数据表没有对应数据。(如果两个表中数据有相同部分，只显示一个)

![img](https://images2018.cnblogs.com/blog/1416057/201807/1416057-20180706155703720-623334246.png)

**右连接：**

**关键字：RIGHT JOIN**

 左表：books 右表：articles

![img](https://images2018.cnblogs.com/blog/1416057/201807/1416057-20180706160238725-295764076.png)

右连接会读取右边数据表的全部数据，即使左边数据表没有对应数据。(如果两个表中数据有相同部分，只显示一个)

 ![img](https://images2018.cnblogs.com/blog/1416057/201807/1416057-20180706160503488-749186529.png)

 