# 如何在IDEA中连接mysql数据库





# 查看mysql版本号

登入mysql 	

~~~
select version();
~~~

### status



```
总结一下：
不管是mysql-5.7.22-win32 还是 mysql-5.7.22-win64。
1、解压到目录
2、创建my-default.ini ，或者my.ini （至于内容，似乎不存在）
3、cmd进入解压后的bin目录 输入 mysqld --install  注册服务
4、输入  mysql --initialize --console
    然后你可以在初始化的最后面看到有一个 root@localhost: 后面有一连串的字母数字符号, 这是 MySQL 为你自动生成的随机密码，一定要记下来,    一会我们登陆 MySQL 数据库的时候要用。

    PS(我未使用)：使用-initialize生成随机密码，使用mysqld --initialize-insecure --user=mysql生成空密码，初始化后data文件夹会自动生成，不用自己新建。
5、net start mysql 启动mysql
6、mysql -u root -p 
password:*********(上面生成的随机密码)
7、mysql> set password = password('你的密码')
8、mysql> quit
9、net stop mysql 
10、重新启动，用你的密码
```





