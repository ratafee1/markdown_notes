

# Neither the JAVA_HOME nor the JRE_HOME environment variable is defined 完美解决（tomcat error）



error：
Linux下启动和关闭tomcat报错，如下图所示：

![img](https://img-blog.csdn.net/20161018143115249?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)



原因：
因为启动tomcat会调用tomcat安装文件中的startup.bat，而它调用了catalina.bat则调用了setclasspath.bat。因此需要在setclasspath.bat的开头手动声明环境变量。



解决方案：
用vim打开tomcat的bin目录下的setclasspath.sh，添加JAVA_HOME和JRE_HOME两个环境变量（下图红色方框内），两个环境变量路径为您安装的java JDK的路径。

windows下将export改为set即可。

![img](https://img-blog.csdn.net/20161018141757039?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

保存并且退出即可。

再次使用service tomcat start没报错，如下图所示：

![img](https://img-blog.csdn.net/20161018143128155?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

成功用service tomcat start开启tomcat服务。








# Centos6 打开关闭防火墙



- 打开防火墙：service iptables start
- 关闭防火墙：service iptables stop
- 查看防火墙状态：service iptables status