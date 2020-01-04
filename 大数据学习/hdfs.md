

![image-20191213182549711](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191213182549711.png)



![image-20191213182718165](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191213182718165.png)



![image-20191213183200753](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191213183200753.png)



![image-20191213183958836](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191213183958836.png)

![image-20191213184030289](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191213184030289.png)



![image-20191213184345286](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191213184345286.png)



![image-20191213184526623](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191213184526623.png)



![image-20191213184555472](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191213184555472.png)





# bin/hadoop checknative



# 配置hadoop配置文件，scp -r hadoop-2.7.5 node02:$PWD





# 启动hadoop

![image-20191214002508778](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191214002508778.png)





三个端口查看界面
http://node01:50070/explorer.html#/ 查看hdfs
http://node01:8088/cluster 查看yarn集群
http://node01:19888/jobhistory 查看历史完成的任务





# 3. HDFS 的架构

HDFS是一个主/从（Mater/Slave）体系结构，
HDFS由四部分组成，HDFS Client、NameNod e、DataNode和Secondary NameNode。



### **1、Client：就是客户端。
文件切分。文件上传 HDFS 的时候，Client 将文件切分成 一个一个的Block，然后进行存
储。
与 NameNode 交互，获取文件的位置信息。
与 DataNode 交互，读取或者写入数据。
Client 提供一些命令来管理 和访问HDFS，比如启动或者关闭HDFS。

### 2、NameNode：就是 master，它是一个主管、管理者。
管理 HDFS 的名称空间
管理数据块（Block）映射信息
配置副本策略
处理客户端读写请求。

### 3、DataNode：就是Slave。NameNode 下达命令，DataNode 执行实际的操作。
存储实际的数据块。
执行数据块的读/写操作。
### 4、Secondary NameNode：并非 NameNode 的热备。当NameNode 挂掉的时候，它并不
能马上替换 NameNode 并提供服务。
辅助 NameNode，分担其工作量。
定期合并 fsimage和fsedits，并推送给NameNode。
在紧急情况下，可辅助恢复 NameNode。





# 4:NameNode和DataNode



NameNode在内存中保存着整个文件系统的名称空间和文件数据块的地址映射
整个HDFS可存储的文件数受限于NameNode的内存大小
### 1、NameNode元数据信息 文件名，文件目录结构，文件属性(生成时间，副本数，权限)每个
文件的块列表。 以及列表中的块与块所在的DataNode之间的地址映射关系 在内存中加载文件
系统中每个文件和每个数据块的引用关系(文件、block、datanode之间的映射信息) 数据会定
期保存到本地磁盘（fsImage文件和edits文件）
### 2、NameNode文件操作 NameNode负责文件元数据的操作 DataNode负责处理文件内容的读写
请求，数据流不经过NameNode，会询问它跟那个DataNode联系
### 3、NameNode副本 文件数据块到底存放到哪些DataNode上，是由NameNode决定的，NN根
据全局情况做出放置副本的决定
### 4、NameNode心跳机制 全权管理数据块的复制，周期性的接受心跳和块的状态报告信息（包
含该DataNode上所有数据块的列表） 若接受到心跳信息，NameNode认为DataNode工作正
常，如果在10分钟后还接受到不到DN的心跳，那么NameNode认为DataNode已经宕机 ,这时候
NN准备要把DN上的数据块进行重新的复制。 块的状态报告包含了一个DN上所有数据块的列
表，blocks report 每个1小时发送一次.





# 4.2 DataNode作用

提供真实文件数据的存储服务。
1、Data Node以数据块的形式存储HDFS文件
2、Data Node 响应HDFS 客户端读写请求
3、Data Node 周期性向NameNode汇报心跳信息

4、Data Node 周期性向NameNode汇报数据块信息
5、Data Node 周期性向NameNode汇报缓存数据块信息



# 5:HDFS的副本机制和机架感知

## 5.1 HDFS 文件副本机制
所有的文件都是以 block 块的方式存放在 HDFS 文件系统当中,作用如下

1. 一个文件有可能大于集群中任意一个磁盘，引入块机制,可以很好的解决这个问题

2. 使用块作为文件存储的逻辑单位可以简化存储子系统

3. 块非常适合用于数据备份进而提供数据容错能力
在 Hadoop1 当中, 文件的 block 块默认大小是 64M, hadoop2 当中, 文件的 block 块大小默认是
128M, block 块的大小可以通过 hdfs-site.xml 当中的配置文件进行指定

~~~
<property>
<name>dfs.block.size</name>
<value>块大小 以字节为单位</value>
</property>
~~~



### 5.2 机架感知
HDFS分布式文件系统的内部有一个副本存放策略：以默认的副本数=3为例：
1、第一个副本块存本机


2、第二个副本块存跟本机同机架内的其他服务器节点
3、第三个副本块存不同机架的一个服务器节点上





# 6、hdfs的命令行使用

# 7、hdfs的高级使用命令

### hdfs dfs -count -q -h /user/root/dir1 #查看配额信息

## 7.1.1、数量限额

### hdfs dfs -mkdir -p /user/root/dir #创建hdfs文件夹
hdfs dfsadmin -setQuota 2 dir # 给该文件夹下面设置最多上传两个文件，发现只能
上传一个文件
hdfs dfsadmin -clrQuota /user/root/dir # 清除文件数量限制



### 7.1.2、空间大小限额
#### 在设置空间配额时，设置的空间至少是block_size * 3大小

hdfs dfsadmin -setSpaceQuota 4k /user/root/dir # 限制空间大小4KB
hdfs dfs -put /root/a.txt /user/root/dir

#### 生成任意大小文件的命令:

dd if=/dev/zero of=1.txt bs=1M count=2 #生成2M的文件

#### 清除空间配额限制

hdfs dfsadmin -clrSpaceQuota /user/root/dir



### 7.2、hdfs的安全模式

安全模式是hadoop的一种保护机制，用于保证集群中的数据块的安全性。当集群启动的时
候，会首先进入安全模式。当系统处于安全模式时会检查数据块的完整性。
假设我们设置的副本数（即参数dfs.replication）是3，那么在datanode上就应该有3个副本存
在，假设只存在2个副本，那么比例就是2/3=0.666。hdfs默认的副本率0.999。我们的副本率
0.666明显小于0.999，因此系统会自动的复制副本到其他dataNode，使得副本率不小于0.999。
如果系统中有5个副本，超过我们设定的3个副本，那么系统也会删除多于的2个副本。
在安全模式状态下，文件系统只接受读数据请求，而不接受删除、修改等变更请求。在，当
整个系统达到安全标准时，HDFS自动离开安全模式。
安全模式操作命令

hdfs dfsadmin -safemode get #查看安全模式状态
hdfs dfsadmin -safemode enter #进入安全模式
hdfs dfsadmin -safemode leave #离开安全模式





# 8. HDFS基准测试
实际生产环境当中，hadoop的环境搭建完成之后，第一件事情就是进行压力测试，测试我们
的集群的读取和写入速度，测试我们的网络带宽是否足够等一些基准测试
### 8.1 测试写入速度
向HDFS文件系统中写入数据,10个文件,每个文件10MB,文件存放到/benchmarks/TestDFSIO中

~~~
hadoop jar /export/servers/hadoop-2.7.5/share/hadoop/mapreduce/hadoopmapreduce-
client-jobclient-2.7.5.jar TestDFSIO -write -nrFiles 10 -
fileSize 10MB
~~~

完成之后查看写入速度结果

~~~
hdfs dfs -text /benchmarks/TestDFSIO/io_write/part-00000
~~~



### 8.2 测试读取速度

测试hdfs的读取文件性能
在HDFS文件系统中读入10个文件,每个文件10M

~~~
hadoop jar /export/servers/hadoop-2.7.5/share/hadoop/mapreduce/hadoopmapreduce-
client-jobclient-2.7.5.jar TestDFSIO -read -nrFiles 10 -
fileSize 10MB
~~~

查看读取果

~~~
hdfs dfs -text /benchmarks/TestDFSIO/io_read/part-00000
~~~



### 8.3 清除测试数据

~~~
hadoop jar /export/servers/hadoop-2.7.5/share/hadoop/mapreduce/hadoopmapreduce-
client-jobclient-2.7.5.jar TestDFSIO -clean
~~~



![image-20191214113347003](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191214113347003.png)



![image-20191214114543791](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191214114543791.png)



# 11.HDFS 的元数据辅助管理

当 Hadoop 的集群当中, NameNode的所有元数据信息都保存在了 FsImage 与 Eidts 文件当中,
这两个文件就记录了所有的数据的元数据信息, 元数据信息的保存目录配置在了 hdfssite.
xml 当中

~~~
<property>
<name>dfs.namenode.name.dir</name>
<value>
file:///export/servers/hadoop2.7.5/hadoopDatas/namenodeDatas,
file:///export/servers/hadoop-
2.7.5/hadoopDatas/namenodeDatas2
</value>
</property>
<property>
<name>dfs.namenode.edits.dir</name>
<value>file:///export/servers/hadoop-
2.7.5/hadoopDatas/nn/edits</value
</property>>
~~~



### 11.1 FsImage 和 Edits 详解
### edits
edits 存放了客户端最近一段时间的操作日志

客户端对 HDFS 进行写文件时会首先被记录在 edits 文件中

edits 修改时元数据也会更新

### fsimage
NameNode 中关于元数据的镜像, 一般称为检查点, fsimage 存放了一份比较完整的
元数据信息

因为 fsimage 是 NameNode 的完整的镜像, 如果每次都加载到内存生成树状拓扑结
构，这是非常耗内存和CPU, 所以一般开始时对 NameNode 的操作都放在 edits 中



fsimage 内容包含了 NameNode 管理下的所有 DataNode 文件及文件 block 及 block
所在的 DataNode 的元数据信息.



随着 edits 内容增大, 就需要在一定时间点和 fsimage 合并



![image-20191214121844157](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191214121844157.png)
![image-20191214121921389](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191214121921389.png)



### 1.3 使用url方式访问数据（了解）

### 1.4 使用文件系统方式访问数据（掌握）

# 1.4.6 hdfs访问权限控制

# 1.4.7 小文件合并



### [Git 修改commit message](https://www.cnblogs.com/revel171226/p/9208589.html)

1、git log --oneline -5

  查看最近5次commit的简要信息，



2，修改最近一次的commit 信息

　　git commit --amend

