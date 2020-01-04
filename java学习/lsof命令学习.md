# 列出所有网络连接

~~~shell
lsof -i		+[tcp,udp] +[4,6]
~~~



# 找到使用某个端口的进程

~~~shell
lsof -i:25
~~~



#### 使用@host:port显示基于主机与端口的连接

~~~shell
#  lsof  -i@172.16.12.5:22
~~~



# 找出监听端口



~~~shell
#  lsof  -i -sTCP:LISTEN[ESTABLISHED]
~~~





# **查看所属root用户进程所打开的文件类型为txt的文件**

~~~shell
lsof -a -u root -d txt
~~~



# 使用来显示除指定用户以外的其它所有用户所做的事情

~~~shell
#  lsof  -u ^daniel
~~~



# 杀死指定用户所做的一切事情

~~~shell
#  kill  -9  `lsof -t -u daniel`
~~~



# 显示与指定目录交互的所有一切

~~~shell
 #  lsof  /var/log/messages/
~~~



# **查找谁在使用文件系统**

~~~shell
lsof /GTES11/ 
~~~





# **搜索被程序打开的所有文件及打开的文件相关联进程**
如果想知道执行PID号为637的sendmail命令打开的所有文件、设备、库及套接字等，可以执行
lsof -p 637





# **c 显示出以字母 c开头进程现在打开的文件**
例:显示以init进程现在打开的文件
\# lsof -c init



**login name(登入名称)或UID所正在打开文件。**
\# lsof -u loginname



# lsof +L1显示所有打开的链接数小于1的文件

~~~shell
 #  lsof  +L1
~~~

