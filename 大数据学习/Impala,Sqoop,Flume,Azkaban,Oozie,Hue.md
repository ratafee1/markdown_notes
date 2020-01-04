# impala

![image-20191219224348549](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191219224348549.png)







~~~
yum install -y impala impala-server impala-state-store impala-catalog impala-shell
~~~





~~~
cp -r /export/servers/apache-hive-2.1.1-bin/conf/hive-site.xml /etc/impala/conf/hive-site.xml
~~~









The necessary tables required for the metastore are missing in MySQL. Manually create the tables and restart hive metastore.

The schema files for MySQL will be available under the path `$HIVE_HOME/scripts/metastore/upgrade/mysql/`.

```
cd $HIVE_HOME/scripts/metastore/upgrade/mysql/

< Login into MySQL >

mysql> drop database IF EXISTS hive;
mysql> create database hive;
mysql> use hive;
mysql> source hive-schema-2.1.1.mysql.sql;
```

Restart Hive metastore.









如果在hive里面做了新增、删除数据库、表或者数据等更新操作，需要执行在impala里面执行INVALIDATE METADATA;

命令才能将hive的数据同步impala； 

如果直接在impala里面新增、删除数据库、表或者数据，会自动同步到hive，无需执行任何命令。





# sqoop



# 测试连接

~~~
bin/sqoop list-databases \
--connect jdbc:mysql://localhost:3306/ \
--username root --password 123456
~~~



# 导入hdfs

~~~
bin/sqoop import \
--connect jdbc:mysql://node01:3306/userdb \
--username root \
--password 123456 \
--target-dir /sqoopresult214 \
--fields-terminated-by '\t' \
--split-by id \
--table emp --m 2
~~~





#  导入hive

~~~
bin/sqoop create-hive-table \
--connect jdbc:mysql://node01:3306/userdb \
--table emp_add \
--username root \
--password 123456 \
--hive-table test.emp_add_sp
~~~

~~~
bin/sqoop import \
--connect jdbc:mysql://node01:3306/userdb \
--username root \
--password 123456 \
--table emp_add \
--hive-table test.emp_add_sp \
--hive-import \
--m 1
~~~

~~~
bin/sqoop import \
--connect jdbc:mysql://node01:3306/userdb \
--username root \
--password 123456 \
--table emp_conn \
--hive-import \
--m 1 \
--hive-database test;
~~~

# 增量导入

~~~
bin/sqoop import \
--connect jdbc:mysql://node01:3306/userdb \
--username root \
--password 123456 \
--target-dir /appendresult \
--table emp --m 1
~~~

~~~
bin/sqoop import \
--connect jdbc:mysql://node01:3306/userdb \
--username root  --password 123456 \
--table emp --m 1 \
--target-dir /appendresult \
--incremental append \
--check-column id \
--last-value  1204
~~~



# 导出

~~~
bin/sqoop export \
--connect jdbc:mysql://node01:3306/userdb \
--username root \
--password 123456 \
--table employee \
--export-dir /emp_data
~~~

~~~
bin/sqoop export \
--connect jdbc:mysql://node01:3306/userdb \
--username root \
--password 123456 \
--table updateonly \
--export-dir /updateonly_1/
~~~

~~~
bin/sqoop export \
--connect jdbc:mysql://node01:3306/userdb \
--username root --password 123456 \
--table updateonly \
--export-dir /updateonly_2/ \
--update-key id \
--update-mode updateonly
~~~



# 创建job

~~~
bin/sqoop job --create itcastjob -- import --connect jdbc:mysql://node01:3306/userdb \
--username root \
--password 123456 \
--target-dir /sqoopresult333 \
--table emp --m 1
~~~

~~~
<property>

  <name>sqoop.metastore.client.record.password</name>

  <value>true</value>

  <description>If true, allow saved passwords in the metastore.

  </description>

</property>
~~~





# 数据源

爬虫、服务器日志、各种传感器

# 消费实用数据

MapReduce、hive、spark、数据挖掘、机器学习



![image-20191220173615480](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191220173615480.png)







### Apache Flume

- 概述

  - flume是一款大数据中海量数据采集传输汇总的软件。特别指的是数据流转的过程，或者说是数据搬运的过程。把数据从一个存储介质通过flume传递到另一个存储介质中。

- 核心组件

  - source ：用于对接各个不同的数据源
  - sink：用于对接各个不同存储数据的目的地（数据下沉地）
  - channel：用于中间临时存储缓存数据

- 运行机制

  - flume本身是java程序 在需要采集数据机器上启动 ----->agent进程

  - agent进程里面包含了：source  sink  channel

  - 在flume中，数据被包装成event 真是的数据是放在event body中

    event是flume中最小的数据单元

- 运行架构

  - 简单架构

    只需要部署一个agent进程即可

  - 复杂架构

    多个agent之间的串联  相当于大家手拉手共同完成数据的采集传输工作

    在串联的架构中没有主从之分 大家的地位都是一样的

------

- flume的安装部署

  - 在conf/flume-env.sh  导入java环境变量

    保证flume工作的时候一定可以正确的加载到环境变量

- flume开发步骤

  - 中的就是根据业务需求编写采集方案配置文件

  - 文件名见名知意  通常以souce——sink.conf

  - 具体需要描述清楚sink source channel组件配置信息 结合官网配置

  - 启动命令

    ```
    bin/flume-ng agent --conf conf --conf-file conf/netcat-logger.conf --name a1 -Dflume.root.logger=INFO,console  命令完整版
    
    bin/flume-ng agent -c ./conf -f ./conf/spool-hdfs.conf -n a1 -Dflume.root.logger=INFO,console  命令精简版
    
    --conf指定配置文件的目录
    --conf-file指定采集方案路径
    --name  agent进程名字 要跟采集方案中保持一致
    ```

---

- 案例：监控目录数据变化到hdfs

  - hdfs sink

    ```
    roll控制写入hdfs文件 以何种方式进行滚动
    a1.sinks.k1.hdfs.rollInterval = 3  以时间间隔
    a1.sinks.k1.hdfs.rollSize = 20     以文件大小
    a1.sinks.k1.hdfs.rollCount = 5     以event个数
    如果三个都配置  谁先满足谁触发滚动
    如果不想以某种属性滚动  设置为0即可
    
    是否开启时间上的舍弃  控制文件夹以多少时间间隔滚动
    以下述为例：就会每10分钟生成一个文件夹
    a1.sinks.k1.hdfs.round = true
    a1.sinks.k1.hdfs.roundValue = 10
    a1.sinks.k1.hdfs.roundUnit = minute
    ```

  - spooldir  source

    - 注意其监控的文件夹下面不能有同名文件的产生
    - 如果有 报错且罢工 后续就不再进行数据的监视采集了
    - 在企业中通常给文件追加时间戳命名的方式保证文件不会重名

- 案例：监控文件的变化采集到hdfs

  - exec source  可以执行指定的linux command  把命令的结果作为数据进行收集

    ```
    while true; do date >> /root/logs/test.log;done
    使用该脚本模拟数据实时变化的过程
    ```

---

- flume的负载均衡

  - 所谓的负载均衡 用于解决一个进程或者程序处理不了所有请求 多个进程一起处理的场景
  - 同一个请求只能交给一个进行处理 避免数据重复
  - 如何分配请求就涉及到了负载均衡的算法：轮询（round_robin）  随机（random）  权重

- flume串联跨网络传输数据

  - avro sink  

  - avro source

    使用上述两个组件指定绑定的端口ip 就可以满足数据跨网络的传递 通常用于flume串联架构中

- flume串联启动

  通常从远离数据源的那一级开始启动

----

- flume failover
  - 容错又称之为故障转移  容忍错误的发生。
  - 通常用于解决单点故障 给容易出故障的地方设置备份
  - 备份越多 容错能力越强  但是资源的浪费越严重

----

- 静态拦截器

  ```
  如果没有使用静态拦截器
  Event: { headers:{} body:  36 Sun Jun  2 18:26 }
  
  使用静态拦截器之后 自己添加kv标识对
  Event: { headers:{type=access} body:  36 Sun Jun  2 18:26 }
  Event: { headers:{type=nginx} body:  36 Sun Jun  2 18:26 }
  Event: { headers:{type=web} body:  36 Sun Jun  2 18:26 }
  ```

  后续在存放数据的时候可以使用flume的规则语法获取到拦截器添加的kv内容

  ```
  %{type}
  ```

- 模拟数据实时产生

  ```
  while true; do echo "access access....." >> /root/logs/access.log;sleep 0.5;done
  while true; do echo "web web....." >> /root/logs/web.log;sleep 0.5;done
  while true; do echo "nginx nginx....." >> /root/logs/nginx.log;sleep 0.5;done
  ```

----

- 



# Azkaban



## 1. 工作流产生背景

工作流（Workflow），指“业务过程的部分或整体在计算机应用环境下的***\*自动化\****”。是对工作流程及其各操作步骤之间业务规则的抽象、概括描述。工作流解决的主要问题是：为了实现某个业务目标，利用计算机软件在多个参与者之间按某种预定规则***\*自动\****传递文档、信息或者任务。

一个完整的数据分析系统通常都是由多个前后依赖的模块组合构成的：数据采集、数据预处理、数据分析、数据展示等。各个模块单元之间存在时间先后依赖关系，且存在着周期性重复。

为了很好地组织起这样的复杂执行计划，需要一个工作流调度系统来调度执行。





![image-20191221004344725](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191221004344725.png)





![image-20191221004918668](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191221004918668.png)





~~~
source /export/softwares/azkaban/azkaban-db-0.1.0-SNAPSHOT/create-all-sql-0.1.0-SNAPSHOT.sql
~~~





### Azkaban

- azkaban
  - 是由领英退出的一款开源免费的工作流调度器软件
  - 特点
    - 功能强大  可以调度几乎所有软件的执行（command）
    - 配置简单  job配置文件
    - 提供了web页面使用
    - java语言开发 源码清晰可见  可以进行二次开发
  - 架构
    - web服务器 ：对外提供web服务 用户在页面上进行项目的相关管理
    - executor服务器：负责具体的工作流的调度提交。
    - 数据库：用于保存工作流相关信息（比如：mysql）
  - 部署模式
    - 单节点模式：web、executor在同一个进程  适用于测试体验
    - two-server:web、executor在不同的进程中  可以使用第三方数据库
    - mutil-executor-server:web、executor在不同的机器上 可以部署多个executor服务器

-----

- 安装部署

  - 单节点部署模式  注意时区  内存检测的关闭

  - 启动时候必须在安装包的根目录下进行启动

    ```
    bin/start-solo.sh  正确
    ./start-solo.sh  错误
    ```

- azkaban开发流程

  - 编写job的配置文件   xxxxx.job

    ```
    type=command
    command=xxxx
    ```

  - 把所有job配置打成一个zip的压缩包

  - 登录页面node-1:8081  创建工程（默认用户名密码都是azkaban）

  - 上传zip压缩包

  - 选择调度schduler或者立即执行executor工程。

- two server模式部署

  - 该模式的特点是web服务器和executor服务器分别位于不同的进程中
  - 使用第三方的数据库进行数据的保存 ：mysql
  - 安装部署注意事项
    - 先对mysql进行初始化操作
    - 配置azkaban.properties 注意时区 mysql相关  ssl 
    - 启动时候注意需要自己手动的激活executor服务器  在根目录下启动
    - 如果启动出错  通过安装包根目录下的日志进行判断
    - 访问的页面https

- multiple-executor部署模式

  - 所谓的  multiple-executor指的是可以在多个机器上分别部署executor服务器

    相当于做了一个负载均衡

  - 特别注意：executor启动（包括重启）的时候 默认不会激活 需要自己手动激活

    对应的mysql中的表executors  active ：0 表示未激活 1表示激活

    可以自己手动修改数据提交激活 也可以使用官方的命令请求激活

    ```
    curl -G "node-3:$(<./executor.port)/executor?action=activate" && echo
    ```

----

- azkaban调度总结
  - 理论上任何一款软件，只有可以通过shell command执行 都可以转化成为azkaban的调度执行
  - type=command   command = sh xxx.sh









# Oozie



### Apache Oozie

- Apache oozie

  - 是一个工作流调度软件  本身属于cloudera  后来贡献给了apache
  - oozie目的根据一个定义DAG（有向无环图）执行工作流程
  - oozie本身的配置是一种xml格式的配置文件   oozie跟hue配合使用将会很方便
  - oozie特点：顺序执行 周期重复定时  可视化  追踪结果

- Apache  Oozie 

  - Oozie  client：主要是提供一种方式给用户进行工作流的提交启动（cli  javaapi  rest）

  - Oozie server(本身是一个java web应用)

  - Hadoop生态圈

    - oozie各种类型任务提交底层依赖于mr程序 首先启动一个没有reducetak的mr  通过这个mr

      把各个不同类型的任务提交到具体的集群上执行

-----

- oozie 流程节点

  - oozie 核心配置是在一个workflow.xml文件 文件中顶一个工作流的执行流程规则

  - 类型

    - control node  控制工作流的执行路径：start  end  fork  join  kill
    - action node 具体的任务类型：mr  spark  shell  java hive

    上述两种类型结合起来 就可以描绘出一个工作流的DAG图。

- oozie工作流类型

  - workflow  基本类型的工作流  只会按照定义顺序执行 无定时触发
  - coordinator 定时触发任务  当满足执行时间 或者输入数据可用 触发workflow执行
  - bundle  批处理任务 一次提交多个coordinator 

----

- Apache oozie 安装

  - 版本问题：Apache官方提供的是源码包 需要自己结合hadoop生态圈软件环境进行编译  兼容性问题特别难以处理  因此可以使用第三方商业公司编译好  Cloudera（CDH）

  - 修改hadoop的相关配置 启动服务

    - httpfs
    - jobhistory

    配置修改之后需要重启hadoop集群

  - 解压oozie安装包 拷贝相关依赖的软件

  - 修改oozie-site.xml  主要是mysql相关信息 hadoop配置文件

  - 初始化mysql  创建库表

  - 生成执行需要的war包

----

- oozie 实战

  - 解压出官方自带的案例 里面封装了各种类型任务的配置模板
  - 优化更新hadoop环境资源配置
    - yarn资源相关的  申请资源的上下限   yarn调度策略（fair 多线程执行模式）
    - mapreduce申请资源相关的  maptask reducetask申请内存的大小
    - scp给其他机器  重启集群 （hadoop ）  oozie

- oozie 调度流程

  - 根据官方自带的示例编写配置文件

    job.properties  workflow.xml

  - 把任务配置信息连同依赖的资源一起上传到hdfs指定的路径 这个路径在配置中有

  - 利用oozie的命令进行提交

- oozie调度hive脚本

  - 首先必须保证hiveserve2服务是启动正常的，如果配置metastore服务，要首先启动metastore

    ```
    nohup /export/servers/hive/bin/hive --service metastore &
    nohup /export/servers/hive/bin/hive --service hiveserver2 &
    ```

- oozie调度mapreduce程序

  - 需要在workflow.xml中开启使用新版的 api  hadoop2.x

- oozie调度串联任务

  通过action节点 成功失败控制执行的流程

  如果上一个action成功  跳转到下一个action 这样就可以变成首尾相连的串联任务

- oozie基于时间的定时

  主要是需要coordinator来配合workflow进行周期性的触发执行

  需要注意时间的格式问题  时区的问题







cp /export/servers/hadoop-2.7.5/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.5.jar /export/servers/oozie-4.1.0-cdh5.14.0/oozie_works/map-reduce/lib/















