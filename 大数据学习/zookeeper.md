![image-20191212155703689](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191212155703689.png)



![image-20191212155724136](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191212155724136.png)

node1：00:50:56:3C:23:45

node2：00:50:56:2A:75:9B

node3：00:50:56:30:61:40



![image-20191212161542139](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191212161542139.png)

192.168.174.100 node01 node01.hadoop.com

192.168.174.110 node02 node02.hadoop.com

192.168.174.120 node03 node03.hadoop.com



![image-20191212162911591](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191212162911591.png)

修改

![image-20191212163213870](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191212163213870.png)

关闭selinux



### ssh配置

ssh-keygen -t rsa

ssh-copy-id node01



![image-20191212164428017](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191212164428017.png)

### 三台机时钟同步

![image-20191212164727053](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191212164727053.png)



![image-20191212164840729](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191212164840729.png)





![image-20191212170141576](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191212170141576.png)



![image-20191212171353652](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191212171353652.png)

![image-20191212190809905](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191212190809905.png)



### SQLyog注册

2、选择完成后弹出注册窗口，我们将软件的注册码：
 名称：ddooo；
 证书秘钥：8d8120df-a5c3-4989-8f47-5afc79c56e7c；
 逐一填到软件的注册框内，点击“注册”按钮，sqlyog会自动检测注册信息；



![img](https:////upload-images.jianshu.io/upload_images/4687074-30ff7a0bb54d173b.jpg?imageMogr2/auto-orient/strip|imageView2/2/w/534/format/webp)

### 特殊字符

$# 传递到脚本的参数个数
$* 以一个单字符串显示所有向脚本传递的参数。
$$ 脚本运行的当前进程 ID 号
$! 后台运行的最后一个进程的 ID 号
$@ 与$*相同，但是使用时加引号，并在引号中返回每个参数。
$? 显示最后命令的退出状态。 0 表示没有错误，其他任何值表明有错误。



# zookeeper



![image-20191212205743120](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191212205743120.png)

![image-20191212205810590](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191212205810590.png)



在第一台机器的
/export/servers/zookeeper-3.4.9/zkdatas /这个路径下创建一个文件，文件名为myid ,文件内容
为1

echo 1 > /export/servers/zookeeper-3.4.9/zkdatas/myid







# 第五步：安装包分发并修改myid的值

### 安装包分发到其他机器
第一台机器上面执行以下两个命令
scp -r /export/servers/zookeeper-3.4.9/ node02:/export/servers/
scp -r /export/servers/zookeeper-3.4.9/ node03:/export/servers/
### 第二台机器上修改myid的值为2
echo 2 > /export/servers/zookeeper-3.4.9/zkdatas/myid





# 三台机器启动zookeeper服务
这个命令三台机器都要执行
/export/servers/zookeeper-3.4.9/bin/zkServer.sh start
# 查看启动状态
/export/servers/zookeeper-3.4.9/bin/zkServer.sh status



### zookeeper客户端连接服务器

bin/zkCli.sh -server node01:2181



![image-20191212214943365](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191212214943365.png)

![image-20191212215002080](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191212215002080.png)



![image-20191212215637460](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191212215637460.png)



![image-20191212220406213](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191212220406213.png)