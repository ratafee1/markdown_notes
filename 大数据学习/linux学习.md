# 使用yum安装计划任务功能，结果提示：Another app is currently ...........





```
#rm -f /var/run/yum.pid
```



# linux最小安装没有ifconfig命令，yum不能安装包

/etc/udev/rules.d/70-persistent-net.rules

cd /etc/sysconfig/network-scripts/ifcfg-eth0	增加IPADDR	GATEWAY

onboot改为yes

service network restart

yum install net-tools.x86_64

修改/etc/resolv.conf	加入nameserver 8.8.8.8



### linux每隔固定时间执行命令

watch -n 3 'date +"%H:%M:%S"'

watch uptime



# 配置时间同步

yum install -y ntp

service ntpd start

ntpstat



# 修改主机名

vi /etc/sysconfig/network

vi /etc/hosts



# 关闭SElinux

setenforce 0

vi /etc/selinux/config

getenforce



# 关闭防火墙

service iptables stop

chkconfig iptables off



# ssh 免密登录

ssh-keygen -t rsa

ssh-copy-id root@cdh01



![image-20200106035804896](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20200106035804896.png)





# 配置yum源

wget https://archive.cloudera.com/cdh5/redhat/6/x86_64/cdh/cloudera-cdh5.repo

mv cloudera-cdh5.repo /etc/yum.repos.d/

yum install -y yum-utils createrepo

reposync -r cloudera-cdh5





![image-20200106044509193](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20200106044509193.png)

createrepo .

