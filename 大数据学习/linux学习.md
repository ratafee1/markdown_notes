# 使用yum安装计划任务功能，结果提示：Another app is currently ...........





```
#rm -f /var/run/yum.pid
```



# linux最小安装没有ifconfig命令，yum不能安装包

cd /etc/sysconfig/network-scripts/ifcfg-eth0	增加IPADDR	GATEWAY

onboot改为yes

service network restart

yum install net-tools.x86_64

修改/etc/resolv.conf	加入nameserver 8.8.8.8



### linux每隔固定时间执行命令

watch -n 3 'date +"%H:%M:%S"'

watch uptime

