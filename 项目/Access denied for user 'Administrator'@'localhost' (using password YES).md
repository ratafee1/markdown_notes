# [Access denied for user 'Administrator'@'localhost' (using password: YES)](https://www.cnblogs.com/tongxuping/p/7081656.html)



在Spring容器中通过配置 <context:property-placeholder location="classpath:/jdbc.properties"/> 调用properties数据源配置文件时出现 **Access denied for user 'Administrator'@'localhost' (using password: YES) 错误！！！！**

**![img](https://images2015.cnblogs.com/blog/959658/201706/959658-20170627184632524-1497079287.png)**

 

**Properties配置（C3p0数据源）：**

```
dirver=com.mysql.jdbc.Driver
jdbcUrl=jdbc:mysql://localhost:3306/mydb1
username=root
password=admin
```

**Spring基本配置（完成注入）：**

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
<context:property-placeholder location="classpath:/jdbc.properties"/>

<bean id="datasouce" class="com.mchange.v2.c3p0.ComboPooledDataSource">
    <property name="driverClass"  value="${dirver}"/>
    <property name="jdbcUrl" value="${jdbcUrl}"/>
    <property name="user" value="${username}"/>
    <property name="password" value="${password}"/>
</bean>
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

---- 在获取数据源中的连接时出现上述的错误。

 **错误原因：**

　　在系统中也有个username属性，这时系统变量覆盖了Properties中的值，这时取得username的值为系统的用户名Administrator，密码为properties中的password去查询数据库，此时用户名名和密码并不匹配就会报错。在Spring完成注入时是用 "${..}"  方式获取值完成注入的。而通过这种表达式也能直接获取到JVM系统属性..........

 

**解决方案：**

　　方案一：将properties文件中的username换成user或其他就字符串就可以成功获取连接访问数据库。建议：username时敏感词汇，为了安全起见还是尽量不要使用username。

　　方案二：在Spring配置文件中修改成：<context:property-placeholder location="classpath:/jdbc.properties" system-properties-mode="FALLBACK / NEVER"/>   

　　　　　　添加一个system-properties-mode属性

　　　　　　该属性有三个值：FALLBACK　　--- 默认值，不存在时覆盖

　　　　　　　　　　　　　　NEVER　　　   --- 不覆盖

　　　　　　　　　　　　　　OVERRIDE　　--- 覆盖







# Tomcat报错Invalid message received with signature 18245



运行tomcat最后在窗口打印出   Invalid message received with signature 18245这个错误，只是写了一个简单的demo，最后百度了一通，说是Tomcat的Ajp端口8009，外网访问的原因，如果没有指定IP地址的话，默认是绑定任意地址，这样就导致外网也可以访问这个端口。因此出于安全考虑，我们需要增加这个address的设置，并且绑定到127.0.0.1，结果如下：<Connector port="8009" protocol="AJP/1.3" address="127.0.0.1" redirectPort="8443" />，修改的目录是tomcat下的conf/server.xml文件，里面找一下port=‘8009’的那一行，添加address="127.0.0.1"。

错误截图

参考文章：

http://www.mobibrw.com/2013/996













# [(28000): Access denied for user 'root'@'127.0.0.1' (using password: YES)](https://www.cnblogs.com/kerrycode/p/7597258.html)







在一台测试服务器测试Python脚本时，执行Python脚本时报如下错误：

  

[![clip_image001](https://images2017.cnblogs.com/blog/73542/201709/73542-20170926155924760-611558177.png)](http://images2017.cnblogs.com/blog/73542/201709/73542-20170926155923932-997324643.png)

 

 

主要错误信息为“operation the sql fail!1045 (28000): Access denied for user 'root'@'127.0.0.1' (using password: YES)”。 部分测试脚本如下所示，如下所，mysql.connector.connect的host为127.0.0.1 其它账号信息做了脱敏处理.

 

```
def record_server_info():
    try:
        server_ip = get_host_ip();
 
        server_name= str.strip(get_host_name());
 
        server_system=platform.system();
 
        linux_dis =platform.linux_distribution();
        os_version =''
        os_version = ' '.join(linux_dis)
 
        os_bitinfo = platform.architecture()
        os_bit =os_bitinfo[0][0:2]
 
        processor = str.strip(commands.getoutput("cat /proc/cpuinfo | grep name | cut -f2 -d: | uniq -c"))
 
        cpu_slot= commands.getoutput("cat /proc/cpuinfo | grep 'model name' | sort | uniq | wc -l");
 
        cpu_core =  multiprocessing.cpu_count();
 
        processor_core =int(cpu_core)/int(cpu_slot);
 
        memory = get_physical_memory()
 
        disk_space = get_disk_info()["capacity"]/1024/1024;
  
 
        dbcon = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            passwd='123456',
            database='mysql'
        )
        cursor = dbcon.cursor()
        sql_tex =( "insert into db_server_info("
                   "factory_cd      ,"
                   "server_name     ,"
                   "server_ip       ,"
                   "server_type     ,"
                   "server_system   ,"
                   "is_production   ,"
                   "os_version      ,"
                   "os_patch        ,"
                   "os_bit          ,"
                   "processors      ,"
                   "cpu_slot        ,"
                   "processors_core ,"
                   "memory          ,"
                   "disk_space      ,"
                   "server_purpose)  "
                   "values(%(factory_cd)s,%(server_name)s,%(server_ip)s,%(server_type)s,%(server_system)s,%(is_production)s,%(os_version)s,%(os_patch)s,%(os_bit)s,%(processors)s,%(cpu_slot)s,%(processors_core)s,%(memory)s,%(disk_space)s,%(server_purpose)s)")
        data={'factory_cd':factory_cd, 'server_name':server_name, 'server_ip':server_ip,"server_type":server_type,"server_system":server_system,"is_production":is_productin,"os_version":os_version, "os_patch":'',"os_bit":int(os_bit), "processors":processor,"cpu_slot":cpu_slot, "processors_core":processor_core,"memory":memory,"disk_space":disk_space,"server_purpose":''}
 
        cursor.execute('truncate table db_server_info')
        dbcon.commit()
        cursor.execute(sql_tex, data)
        dbcon.commit()
 
    except mysql.connector.Error as e:
        print('operation the sql fail!{0}'.format(e))
    finally:
        cursor.close;
        dbcon.close;
```

 

 

mysql -u root -p 测试登录MySQ发现没有问题，但是一检查发现，如果不指定host的情况下，当前用户为[root@localhost](mailto:root@localhost)，而root@'127.0.0.1'的密码为空。

 

```
mysql> select current_user();
+----------------+
| current_user() |
+----------------+
| root@localhost |
+----------------+
1 row in set (0.00 sec)
 
mysql> show grants for root@'localhost';
+---------------------------------------------------------------------------------------------------------------------------+
| Grants for root@localhost                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------+
| GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' IDENTIFIED BY PASSWORD '*9B67EF98D94F2B81011D6D2CEDE4' WITH GRANT OPTION|
| GRANT PROXY ON ''@'' TO 'root'@'localhost' WITH GRANT OPTION                                                              |
+---------------------------------------------------------------------------------------------------------------------------+
2 rows in set (0.00 sec)
 
mysql> show grants for root@'127.0.0.1';
+---------------------------------------------------------------------+
| Grants for root@127.0.0.1                                           |
+---------------------------------------------------------------------+
| GRANT ALL PRIVILEGES ON *.* TO 'root'@'127.0.0.1' WITH GRANT OPTION |
+---------------------------------------------------------------------+
1 row in set (0.00 sec)
 
mysql> 
```

 

立即检查my.cnf的配置，发现可能某次测试时，设置了参数 skip-name-resolve， 后面忘记取消了。由于启动mysqld时使用了'--skip-name-resolve'参数，此种情况下由于不做域名解析，127.0.0.1和localhost对mysql数据库来讲，是不同的主机，而root@'127.0.0.1'为空密码，所以Python脚本执行时，访问MySQL报错“(28000): Access denied for user 'root'@'127.0.0.1' (using password: YES)”