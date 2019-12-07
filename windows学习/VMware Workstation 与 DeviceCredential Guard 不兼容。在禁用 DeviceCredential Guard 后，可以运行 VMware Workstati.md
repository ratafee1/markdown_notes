# VMware Workstation 与 Device/Credential Guard 不兼容。在禁用 Device/Credential Guard 后，可以运行 VMware Workstati



打开的时候提示VMware Workstation 与 Device/Credential Guard 不兼容，且在禁用Device/Credential Guard后才能运行VMware，该怎么办呢，本文就给大家分享一下Win10系统下提示VMware与Device/Credential Guard不兼容的具体解决方法。

本人系统为win10家庭版

![img](https://img-blog.csdnimg.cn/20191002143650105.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2x1Y2t5c2lnbg==,size_16,color_FFFFFF,t_70)



原因分析：
VMware和Hyper-V不兼容导致。
解决方法：

Win10专业版解决方法：
1、控制面板—程序——打开或关闭Windows功能，取消勾选Hyper-V，确定禁用Hyper-V服务。
2、之后重新启动计算机，再运行VM虚拟机即可。
Win10家庭版解决方法：

1、按下WIN+R打开运行，然后输入services.msc回车；
2、在服务中找到 HV主机服务，双击打开设置为禁用

![img](https://img-blog.csdnimg.cn/20191002143736740.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2x1Y2t5c2lnbg==,size_16,color_FFFFFF,t_70)



3、windowns键+X   再打开Windows PowerShell（管理员）



4、运行命令：bcdedit /set hypervisorlaunchtype off；

![img](https://img-blog.csdnimg.cn/20191002144356600.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2x1Y2t5c2lnbg==,size_16,color_FFFFFF,t_70)



5、重启windowns10系统


————————————————
版权声明：本文为CSDN博主「小角色也有大梦想」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/luckysign/article/details/101915064