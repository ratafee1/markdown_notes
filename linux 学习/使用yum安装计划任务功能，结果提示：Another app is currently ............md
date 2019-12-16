# 使用yum安装计划任务功能，结果提示：Another app is currently ...........



```
# yum -y install vixie-cron
Loaded plugins: fastestmirror, refresh-packagekit, security
Existing lock /var/run/yum.pid: another copy is running as pid 25960.
Another app is currently holding the yum lock; waiting for it to exit...
```

可能是系统自动升级正在运行，yum在锁定状态中。 
已经有一个yum进程在运行了，使用kill干掉它：

```
# kill -s 9 25960
# ps aux|grep yum
root      6744  0.0  0.0 103260   900 pts/1    S+   14:59   0:00 grep yum
root     25960  0.0  0.0      0     0 ?        Z    Sep19   0:01 [yumBackend.py] <defunct>
```

很遗憾，kill对付不了它，那怎么办呢？

可以通过强制关掉yum进程：

```
#rm -f /var/run/yum.pid
```

然后就可以使用yum了。

