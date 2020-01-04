# Redis



### web1.0时代简介
基本上就是一些简单的静态页面的渲染，不会涉及到太多的复杂业务逻辑，功能简单单一，基本上服务器性能不会有太大压力

缺点：1、Service 越来越多，调用关系变复杂，前端搭建本地环境不再是一件简单的事。考虑团队协作，往往会考虑搭建集中式的开发服务器来解决。这种解决方案对编译型的后端开发来说也许还好，但对前端开发来说并不友好。天哪，我只是想调整下按钮样式，却要本地开发、代码上传、验证生效等好几个步骤。也许习惯了也还好，但开发服务器总是不那么稳定，出问题时往往需要依赖后端开发搞定。看似仅仅是前端开发难以本地化，但这对研发效率的影响其实蛮大。

2、JSP 等代码的可维护性越来越差。JSP 非常强大，可以内嵌 Java 代码。这种强大使得前后端的职责不清晰，JSP 变成了一个灰色地带。经常为了赶项目，为了各种紧急需求，会在 JSP 里揉杂大量业务代码。积攒到一定阶段时，往往会带来大量维护成本。

 







### web2.0时代简介

 

随着Web2.0的时代的到来，用户访问量大幅度提升，同时产生了大量的用户数据。加上后来的智能移动设备的普及，所有的互联网平台都面临了巨大的性能挑战。包括web服务器CPU及内存压力。数据库服务器IO压力等

 

为了解决服务器的性能压力问题，出现了各种各样的解决方案，最典型的就是使用MVC的架构，MVC 是个非常好的协作模式，从架构层面让开发者懂得什么代码应该写在什么地方。为了让 View 层更简单干脆，还可以选择 Velocity、Freemaker 等模板，使得模板里写不了 Java 代码。看起来是功能变弱了，但正是这种限制使得前后端分工更清晰。但是同样也会面临以下问题

 

1、前端开发重度依赖开发环境。这种架构下，前后端协作有两种模式：一种是前端写 demo，写好后，让后端去套模板。淘宝早期包括现在依旧有大量业务线是这种模式。好处很明显，demo 可以本地开发，很高效。不足是还需要后端套模板，有可能套错，套完后还需要前端确定，来回沟通调整的成本比较大。另一种协作模式是前端负责浏览器端的所有开发和服务器端的 View 层模板开发，支付宝是这种模式。好处是 UI 相关的代码都是前端去写就好，后端不用太关注，不足就是前端开发重度绑定后端环境，环境成为影响前端开发效率的重要因素。

 

2、前后端职责依旧纠缠不清。Velocity 模板还是蛮强大的，变量、逻辑、宏等特性，依旧可以通过拿到的上下文变量来实现各种业务逻辑。这样，只要前端弱势一点，往往就会被后端要求在模板层写出不少业务代码。还有一个很大的灰色地带是 Controller，页面路由等功能本应该是前端最关注的，但却是由后端来实现。Controller 本身与 Model 往往也会纠缠不清，看了让人咬牙的代码经常会出现在 Controller 层。这些问题不能全归结于程序员的素养，否则 JSP 就够了。

 

关于如何解决Web服务器的负载压力，其中最常用的一种方式就是使用nginx实现web集群的服务转发以及服务拆分等等



![img](file:///C:\Users\app\AppData\Local\Temp\ksohtml10344\wps4.jpg) 

但是这样也会存在问题，后端服务器的多个tomcat之间如何解决session共享的问题，以及session存放的问题等等

为了解决session存放的问题，也有多种解决方案

方案一：存放在cookie里面。不安全，否定

方案二：存放在文件或者数据库当中。速度慢

方案三：session复制。大量session冗余，节点浪费大

方案四：使用NoSQL缓存数据库。例如redis或者memcache等，完美解决

 



# NoSQL适用场景

• 对数据高并发的读写

• 海量数据的读写

• 对数据高可扩展性的

• 速度够快，能够快速的存取数据

# NoSQL不适用场景

• 需要事务支持

• 基于sql的结构化查询存储，处理复杂的关系,需要即席查询（用户自定义查询条件的查询）。



## 总结用不着sql的和用了sql也不行的情况，请考虑用NoSql





## 2、redis介绍

• 几乎覆盖了Memcached的绝大部分功能

• 数据都在内存中，支持持久化，主要用作备份恢复

• 除了支持简单的key-value模式，还支持多种数据结构的存储，比如 list、set、hash、zset等。

• 一般是作为缓存数据库辅助持久化的数据库

• 现在市面上用得非常多的一款内存数据库



## 4、列式存储HBase介绍

• HBase是Hadoop项目中的数据库。它用于需要对大量的数据进行随机、实时的读写操作的场景中。HBase的目标就是处理数据量非常庞大的表，可以用普通的计算机处理超过10亿行数据，还可处理有数百万列元素的数据表。



## ***\*3.2、\*******\*redis的适用场景\****

 

***\*1.取最新N个数据的操作\****

比如典型的取你网站的最新文章，通过下面方式，我们可以将最新的5000条评论的ID放在Redis的List集合中，并将超出集合部分从数据库获取

· 使用LPUSH latest.comments<ID>命令，向list集合中插入数据

· 插入完成后再用LTRIM latest.comments 0 5000命令使其永远只保存最近5000个ID

· 然后我们在客户端获取某一页评论时可以用下面的逻辑（伪代码）

FUNCTION get_latest_comments(start,num_items):

  id_list = redis.lrange("latest.comments",start,start+num_items-1)

  IF id_list.length < num_items

​    id_list = SQL_DB("SELECT ... ORDER BY time LIMIT ...")

  END

  RETURN id_list

END

如果你还有不同的筛选维度，比如某个分类的最新N条，那么你可以再建一个按此分类的List，只存ID的话，Redis是非常高效的。

***\*2.排行榜应用，取TOP N操作\****

这个需求与上面需求的不同之处在于，前面操作以时间为权重，这个是以某个条件为权重，比如按顶的次数排序，这时候就需要我们的sorted set出马了，将你要排序的值设置成sorted set的score，将具体的数据设置成相应的value，每次只需要执行一条ZADD命令即可。

***\*3.需要精准设定过期时间的应用\****

比如你可以把上面说到的sorted set的score值设置成过期时间的时间戳，那么就可以简单地通过过期时间排序，定时清除过期数据了，不仅是清除Redis中的过期数据，你完全可以把Redis里这个过期时间当成是对数据库中数据的索引，用Redis来找出哪些数据需要过期删除，然后再精准地从数据库中删除相应的记录。

***\*4.计数器应用\****

Redis的命令都是原子性的，你可以轻松地利用INCR，DECR命令来构建计数器系统。

***\*5.Uniq操作，获取某段时间所有数据排重值\****

这个使用Redis的set数据结构最合适了，只需要不断地将数据往set中扔就行了，set意为集合，所以会自动排重。

***\*6.实时系统，反垃圾系统\****

通过上面说到的set功能，你可以知道一个终端用户是否进行了某个操作，可以找到其操作的集合并进行分析统计对比等。没有做不到，只有想不到。

***\*7.Pub/Sub构建实时消息系统\****

Redis的Pub/Sub系统可以构建实时的消息系统，比如很多用Pub/Sub构建的实时聊天系统的例子。

***\*8.构建队列系统\****

使用list可以构建队列系统，使用sorted set甚至可以构建有优先级的队列系统。

***\*9.缓存\****

将数据直接存放到内存中，性能优于Memcached，数据结构更多样化。





## ***\*3.3、redis的\*******\*特点\****

高效性：Redis读取的速度是110000次/s，写的速度是81000次/s

原子性：Redis的所有操作都是原子性的，同时Redis还支持对几个操作全并后的原子性执行。

支持多种数据结构：string（字符串）；list（列表）；hash（哈希），set（集合）；zset(有序集合)

稳定性：持久化，主从复制（集群）

其他特性：支持过期时间，支持事务，消息订阅。



![image-20191222135417560](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191222135417560.png)



![image-20191222135511595](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191222135511595.png)

### redis操作

~~~
keys *	查看所有key
flushdb 清空数据
~~~





# Hbase

# HBase课程

hbase的基本简介：hbase依赖于hdfs，hbase是一个nosql数据库，是一个非关系型的数据库。支持读写查询操作等等

hbase当中所有的数据都是byte[] 

HBase中的表一般有这样的特点：

²  大：一个表可以有上十亿行，上百万列

²  面向列:面向列(族)的存储和权限控制，列(族)独立检索。

²  稀疏:对于为空(null)的列，并不占用存储空间，因此，表可以设计的非常稀疏。



hdfs对随机读写不是支持的太良好，

hbase是一个数据库，支持随机读写。

hbase是基于hdfs的，hbase的数据都是存储在hdfs上面的。hbase支持随机读写，hbase的数据存储在hdfs上面的，hbase是如何基于hdfs的数据做到随机读写的？？



## hbase的简要特征

**1****）海量存储**

Hbase适合存储PB级别的海量数据，在PB级别的数据以及采用廉价PC存储的情况下，能在几十到百毫秒内返回数据。这与Hbase的极易扩展性息息相关。正式因为Hbase良好的扩展性，才为海量数据的存储提供了便利。

**2****）列式存储**

这里的列式存储其实说的是列族存储，Hbase是根据列族来存储数据的。列族下面可以有非常多的列，列族在创建表的时候就必须指定。

**3****）极易扩展**

Hbase的扩展性主要体现在两个方面，一个是基于上层处理能力（RegionServer）的扩展，一个是基于存储的扩展（HDFS）。
 通过横向添加RegionSever的机器，进行水平扩展，提升Hbase上层的处理能力，提升Hbsae服务更多Region的能力。

备注：RegionServer的作用是管理region、承接业务的访问，这个后面会详细的介绍通过横向添加Datanode的机器，进行存储层扩容，提升Hbase的数据存储能力和提升后端存储的读写能力。

**4****）高并发**

由于目前大部分使用Hbase的架构，都是采用的廉价PC，因此单个IO的延迟其实并不小，一般在几十到上百ms之间。这里说的高并发，主要是在并发的情况下，Hbase的单个IO延迟下降并不多。能获得高并发、低延迟的服务。

**5****）稀疏**

稀疏主要是针对Hbase列的灵活性，在列族中，你可以指定任意多的列，在列数据为空的情况下，是不会占用存储空间的。





## HBase的数据存储架构：

主节点：HMaster

​	监控regionServer的健康状态

​	处理regionServer的故障转移

​	处理元数据变更

​	处理region的分配或者移除

​	空闲时间做数据的负载均衡



从节点：HRegionServer

​	负责存储HBase的实际数据

​	处理分配给他的region

​	刷新缓存的数据到HDFS上面去

​	维护HLog

​	执行数据的压缩

​	负责处理region的分片



一个HRegionServer = 1个HLog  +  很多个region

1个region  = 很多个store模块

1个store模块 =  1个memoryStore + 很多个storeFile



HLog：hbase当中预写日志模块，write ahead  log







## HBase的表模型

rowKey：行键，每一条数据都是使用行键来进行唯一标识的

columnFamily：列族。列族下面可以有很多列

column：列的概念。每一个列都必须归属于某一个列族

timestamp：时间戳，每条数据都会有时间戳的概念

versionNum：版本号，每条数据都会有版本号，每次数据变化，版本号都会进行更新



创建一张HBase表最少需要两个条件：表名  +  列族名

注意：rowkey是我们在插入数据的时候自己指定的，列名 也是在我们插入数据的时候动态指定的，时间戳是插入数据的时候，系统自动帮我们生成的，versionNum是系统自动维护的

![image-20191231163315547](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191231163315547.png)

hbase当中数据的查询：

第一种查询方式：  get  rowkey   直接获取某一条数据

第二种查询方式  ：  scan  startRow   stopRow   范围值扫描

第三种查询方式：scan   tableName   全表扫描



总结：HBase是一个nosql数据库，支持增删改查的操作，重点是查询操作。更新与添加操作是一样的



hbase是一个数据库，适合实时的增删改查操作，hbase的数据是保存在hdfs上面的，hdfs是一个适合一次写入，多次读取的文件系统

```
元数据信息
ROW                             COLUMN+CELL                                                                              
 hbase:namespace                column=table:state, timestamp=1558938984497, value=\x08\x00                              
 hbase:namespace,,1558938982489 column=info:regioninfo, timestamp=1559005133554, value={ENCODED => d042e71dc1c25676200cbe
 .d042e71dc1c25676200cbec8fb762 c8fb762263, NAME => 'hbase:namespace,,1558938982489.d042e71dc1c25676200cbec8fb762263.', S
 263.                           TARTKEY => '', ENDKEY => ''}                                                             
 hbase:namespace,,1558938982489 column=info:seqnumDuringOpen, timestamp=1559005133554, value=\x00\x00\x00\x00\x00\x00\x00
 .d042e71dc1c25676200cbec8fb762 \x07                                                                                     
 263.                                                                                                                    
 hbase:namespace,,1558938982489 column=info:server, timestamp=1559005133554, value=node03:16020                          
 .d042e71dc1c25676200cbec8fb762                                                                                          
 263.                                                                                                                    
 hbase:namespace,,1558938982489 column=info:serverstartcode, timestamp=1559005133554, value=1559005110816                
 .d042e71dc1c25676200cbec8fb762                                                                                          
 263.                                                                                                                    
 hbase:namespace,,1558938982489 column=info:sn, timestamp=1559005132098, value=node03,16020,1559005110816                
 .d042e71dc1c25676200cbec8fb762                                                                                          
 263.                                                                                                                    
 hbase:namespace,,1558938982489 column=info:state, timestamp=1559005133554, value=OPEN                                   
 .d042e71dc1c25676200cbec8fb762                                                                                          
 263.                                                                                                                    
 myuser                         column=table:state, timestamp=1558954806615, value=\x08\x00                              
 myuser,,1558954806023.bece64ca column=info:regioninfo, timestamp=1559005133924, value={ENCODED => bece64ca523746f8ab334e
 523746f8ab334ee9f0b8c0af.      e9f0b8c0af, NAME => 'myuser,,1558954806023.bece64ca523746f8ab334ee9f0b8c0af.', STARTKEY =
                                > '', ENDKEY => ''}                                                                      
 myuser,,1558954806023.bece64ca column=info:seqnumDuringOpen, timestamp=1559005133924, value=\x00\x00\x00\x00\x00\x00\x00
 523746f8ab334ee9f0b8c0af.      \x07                                                                                     
 myuser,,1558954806023.bece64ca column=info:server, timestamp=1559005133924, value=node02:16020                          
 523746f8ab334ee9f0b8c0af.                                                                                               
 myuser,,1558954806023.bece64ca column=info:serverstartcode, timestamp=1559005133924, value=1559005111092                
 523746f8ab334ee9f0b8c0af.                                                                                               
 myuser,,1558954806023.bece64ca column=info:sn, timestamp=1559005133018, value=node02,16020,1559005111092                
 523746f8ab334ee9f0b8c0af.                                                                                               
 myuser,,1558954806023.bece64ca column=info:state, timestamp=1559005133924, value=OPEN                                   
 523746f8ab334ee9f0b8c0af.                                                                                               
 user                           column=table:state, timestamp=1558949032333, value=\x08\x00                              
 user,,1558946603100.7d0f1aebaa column=info:regioninfo, timestamp=1559005133566, value={ENCODED => 7d0f1aebaa8569c0a4532e
 8569c0a4532e6f1926b1d3.        6f1926b1d3, NAME => 'user,,1558946603100.7d0f1aebaa8569c0a4532e6f1926b1d3.', STARTKEY => 
                                '', ENDKEY => ''}                                                                        
 user,,1558946603100.7d0f1aebaa column=info:seqnumDuringOpen, timestamp=1559005133566, value=\x00\x00\x00\x00\x00\x00\x00
 8569c0a4532e6f1926b1d3.        \x1A                                                                                     
 user,,1558946603100.7d0f1aebaa column=info:server, timestamp=1559005133566, value=node03:16020                          
 8569c0a4532e6f1926b1d3.                                                                                                 
 user,,1558946603100.7d0f1aebaa column=info:serverstartcode, timestamp=1559005133566, value=1559005110816                
 8569c0a4532e6f1926b1d3.                                                                                                 
 user,,1558946603100.7d0f1aebaa column=info:sn, timestamp=1559005133015, value=node03,16020,1559005110816                
 8569c0a4532e6f1926b1d3.                                                                                                 
 user,,1558946603100.7d0f1aebaa column=info:state, timestamp=1559005133566, value=OPEN                                   
 8569c0a4532e6f1926b1d3.                                                                                                 
6 row(s)
```





HMaster记录了有哪些可用的region可以被分配，还记录了region分配给了哪些region server



## HBase与mr的整合

mr的程序里面，使用了hbase的jar包，我们可以使用打包插件，将hbase的jar包都打包到mr的程序里面去



添加hbase的jar包到Hadoop的classpath路径下面去

```
export HADOOP_HOME=/export/servers/hadoop-2.7.5/
export HBASE_HOME=/export/servers/hbase-2.0.0/
export HADOOP_CLASSPATH=`${HBASE_HOME}/bin/hbase mapredcp`
yarn jar original-hbaseStudy-1.0-SNAPSHOT.jar  cn.itcast.hbasemr.HbaseMR

```



总结：如果读取hbase里面的数据  mapper类需要继承TableMapper

如果需要读取hdfs上面的文本文件数据，mapper类需要继承Mapper

如果要将reduce程序处理完的数据，保存到hbase里面去，reduce类，一定要继承TableReducer





## hive与hbase总结

hive：擅长做数据分析工作

hbase：擅长做数据实时查询的工作



需求一：将hive分析结果数据，保存到hbase里面去

insert  overwrite  table user2  select  * from user ;

```
create table course.hbase_score(id int,cname string,score int)  
stored by 'org.apache.hadoop.hive.hbase.HBaseStorageHandler'    -- 指定数据存储到哪里去
with serdeproperties("hbase.columns.mapping" = "cf:name,cf:score")  --指定数据的映射字段
tblproperties("hbase.table.name" = "hbase_score");  -- 配置hbase表名

```



score表字段

```
score.id        score.cname     score.score
```



需求二：hbase当中已经存在了一张表，并且有了一些数据，对hbase当中存在的数据进行分析，使用hive映射hbase当中表数据，然后对hbase表数据进行分析

```
CREATE external TABLE course.hbase2hive(id int, name string, score int) 
STORED BY 'org.apache.hadoop.hive.hbase.HBaseStorageHandler' 
WITH SERDEPROPERTIES ("hbase.columns.mapping" = ":key,cf:name,cf:score") TBLPROPERTIES("hbase.table.name" ="hbase_hive_score");
```



## HBase的预分区：

可以在创建表的时候提前定义分区的规则，然后将对应的数据，落到对应的region里面去，实现数据的均匀负载。



## hbase的rowkey设计技巧

1：rowkey不宜过长

2：rowkey均匀的散列。将数据均匀的落到不同的region里面去，避免所有的数据都落第到一个region里面去了，造成数据热点问题。在rowkey高几位，随机生成一些数字，实现均匀的负载



避免rowkey的热点问题：

加盐：在rowkey高几位随机生成一些字符串

hash取值：对rowkey进行取hashcode

反转：对rowkey进行反转   三大运营商查询流量，以及话费

时间戳反转：

查询条件：手机号码  业务类型   查询时间

13391508372

rowkey：手机号反转27380519331:业务类型：时间戳



## HBase的协处理器

hbase当中不支持  sql语法

总结：协处理器分为两大类，

observer：可以对数据进行前置或者后置拦截

endpoint：可以用来求最大值，最小值，平均值



## HBase的二级索引

一级索引：按照rowkey进行查询

get

scan  startRow  stopRow

scan   全表

复杂的查询条件：

select name ,count(1)  from   user    where  age >30  group by name 

二级索引：使用空间换取时间的概念



## hue的学习

通过一个框架，hue与其他的框架进行整合，然后我们就可以通过hue来操作所有其他的框架

hue的架构：

UI：操作管理界面

hueServer：服务端，为UI提供各种服务

hueDB：数据库，可以保存各种任务

一句话总结：Hue是一个友好的界面集成框架，可以集成我们各种学习过的以及将要学习的框架，一个界面就可以做到查看以及执行所有的框架 









































# Kafka

## Kafaka集群操作

创建topic

kafka-topics.sh --create --partitions 3 --replication-factor 2 --topic test --zookeeper node01:2181

查看topic

kafka-topics.sh --list --zookeeper node01

生产数据

kafka-console-producer.sh --broker-list node01:9092 --topic test

消费数据

kafka-console-consumer.sh --from-beginning --topic test --zookeeper node01

查看topic的一些信息

kafka-topics.sh --describe --topic test --zookeeper node01

修改topic的配置属性

kafka-topics.sh --zookeeper node01:2181 --alter --topic test --partitions 8





bin/kafka-topics.sh --zookeeper node01:2181 --alter --topic test --config flush.messages=1

bin/kafka-topics.sh --zookeeper node01:2181 --alter --topic test --delete-config flush.messages

kafka-topics.sh --zookeeper node01:2181 --delete --topic test







# ELK



## 1、全文检索需求：

因为数据库已经解决不了海量数据的快速查询，所以引入了全文检索。最原生的是lucene，经过封装出现solr，solr有一个缺点，在建立索引的时候，搜索性能下降，后来出现es，性能最高



## 2、ELK日志协议栈

E：elasticsearch   全文检索的框架，基于lucene

L：logstash   日志数据收集采集框架。类似于flume

K：kibana       报表展示工具。类似于echarts



使用logstash来采集数据，采集的数据全部都存储到es里面去，使用kibana展示es索引库当中的数据



## 3、es的基本介绍

es与传统关系型数据库对比

relationDB  ==》  databases  ==》  tables   ==》  row   ==》  column

ES     ==》 indexes   ==》  types   ==》  Document   ==》  field

es当中的核心概念

index：索引库，我们在es当中创建的一个个的索引库，类似于mysql数据库

type：类型，在索引库下面创建的类型，类似于mysql当中数据库表

document：文档，es当中一条数据就是一个document

filed：字段，一条document数据是由多个字段组成的

mappings：映射关系，映射field的字段的类型，字段的分词，索引，存储的特性

settings：设置  设置es索引库当中数据的分片数以及副本数

cluster：集群  es每一个节点叫做一个node，所有的node组织起来就变成了集群的概念

node：每一个es节点都是一个node



## 4、kibana管理索引库

创建索引库

curl -XPUT http://node01:9200/blog01/article/1?pretty -d  '{"id": "1", "title": "What is lucene"}' 



## 5、es当中索引的映射mappings

在mysql数据库当中，每个字段都有确切的类型

在es当中每个字段有没有类型？？es会对对应的字段进行类型的推断，会自动的推断出来每条数据是什么类型的。

实际工作当中，我们一般都会提前定义好es当中每个字段的类型，方便于我们后面使用JavaBean来映射索引库里面的数据

mappings用于提前定义我们每个字段的类型，便于后期JavaBean进行映射。

mappings还可以用于定义对这个字段是否索引，是否存储，是否分词



message：今天天气还不错

索引：如果对这个字段创建了索引，那么我就可以搜索这个字段里面的数据

分词：如果对字段进行分词，那么就可以按照字段里面的词语进行检索

存储：存储不存储决定了我们查询的结果是否显示这个字段





## 6、es当中的settings

settings主要就是决定了索引库的分片数以及副本数

分片数不能够更改，副本数可以更改



## 7、零停机，重新索引数据

实际工作当中某个字段是string类型的，但是后期业务发展，变成了date类型，mappings一旦定了字段的类型之后就不让改了，我们可以进行重新索引数据





## 8、es的分页操作

lucene当中不支持分页的操作，lucene当中分页需要我们手动自己去封装

es基于lucene的框架，已经帮我们封装好了分页的过程

from+size  浅分页：获取第五页的数据，每页显示10条。获取前五页的数据，一共是50条数据，然后过滤掉前四页数据，过滤掉40条，剩下的就是第五页的数据

适用于数据量不是太大的情况进行分页。

如果数据量太大，效率急剧下降



scroll缓存数据：将查询出来的对应页码的数据进行内存缓存，然后下次需要的时候直接获取







## 9、es当中的分词与停词

新词热词出来，凤姐，老铁，肿么了，传智播客



```
  GET _analyze?pretty
  {
    "analyzer": "ik_max_word",
    "text": "传智播客，老铁，凤姐，肿么了"
  }

```



# ELK第二天

logStash与flume非常的类似，也是做日志数据采集的工作

logstash主要有三个组件

input plugins   ：主要是用于定义从哪些地方可以采集数据  。类似于flume当中source组件

output plugin  ： 主要是定义将采集好的数据保存到哪里去 。类似于flume当中的sink组件

filter  plugin      ： 主要是对采集的数据做加工和格式转换的等一些工作。类似于flume当中的拦截器  interceptor





```
36.157.150.1 
- - 
[05/Nov/2018:12:59:28 +0800]
"GET 
/phpmyadmin_8c1019c9c0de7a0f/js/get_scripts.js.php?scripts%5B%5D=jquery/jquery-1.11.1.min.js&scripts%5B%5D=sprintf.js&scripts%5B%5D=ajax.js&scripts%5B%5D=keyhandler.js&scripts%5B%5D=jquery/jquery-ui-1.11.2.min.js&scripts%5B%5D=jquery/jquery.cookie.js&scripts%5B%5D=jquery/jquery.mousewheel.js&scripts%5B%5D=jquery/jquery.event.drag-2.2.js&scripts%5B%5D=jquery/jquery-ui-timepicker-addon.js&scripts%5B%5D=jquery/jquery.ba-hashchange-1.3.js 
HTTP/1.1" 
200
139613 
"-" 
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
```



## es整合hbase实现二级索引的功能

第一步：数据的搜索都去查询es

第二步：数据的详情都去查询hbase



HBase是一个nosql的非关系型数据库，适合存储海量的数据

es：是一个全文检索的框架，适合做数据的搜索，然后数据的详情我们可以去查询hbase获取

使用es来冗余存储数据，来解决数据的检索问题，然后将数据的详情内容保存到es里面去

需求：使用es整合hbase，实现对文章内容的检索。

第一步：使用代码来解析excel，读取excel内容

第二步：将读取的excel内容，保存到es以及hbase里面去

第三步：搜索es里面的数据，选择某一个详情数据

第四步：通过hbase的查询，找到这一条数据的详情内容



数据保存到es里面去  ==》  启动es服务

数据保存到hbase里面去  =》  启动hbase服务  依赖于zk，依赖于Hadoop环境  ==》 先启动zk，再启动Hadoop  ，再启动hbase



#### 

~~~
bin/logstash -e 'input { stdin{}} output{stdout{codec=>rubydebug}}'
~~~



























