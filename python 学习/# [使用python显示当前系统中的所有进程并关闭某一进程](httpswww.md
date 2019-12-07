# [使用python显示当前系统中的所有进程并关闭某一进程](https://www.cnblogs.com/ljmjjy0820/p/7896154.html)

环境：

Windows 10操作系统

python idle

原理：

调用windows系统自带的命令task，该命令使用方式：

第一步、调用cmd命令行，显示当前系统中所有进程；

​    Win+R->cmd->(input)tasklist

第二步、调用taskkill命令，关闭指定的进程；

taskkill [/S system [/U username [/P [password]]]]

​            {[/FI filter][/PID processid] | /IM imagename} [/T][/F]

常用调用方式为：

![img](https://images2018.cnblogs.com/blog/1036831/201711/1036831-20171125193044406-526641760.png)

进程终止过程示例：

\##假定关闭进程SougouCloud.exe

一、window10 cmd命令行中

```
C:\User\username\ tasklist            ##显示的列表中查看是否找到SougouCloud.exe
C:\User\username\ taskkill /IM SougouCloud.exe /F
```

 

二、python idle中

```
>>>import os
>>>print(os.popen('tasklist'))
>>>os.system('taskkill /IM SougouCloud.exe /F')
```