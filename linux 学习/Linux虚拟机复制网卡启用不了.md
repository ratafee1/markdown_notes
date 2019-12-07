# Linux虚拟机复制网卡启用不了



虚拟机复制到新的机器上之后网卡启动不了，是因为复制之后网卡的MAC地址 变了，启动网卡的配置文件的网卡名称，和配置文件的mac地址改为正确即可。
1.查看当前网卡名称和MAC地址
[root@centos net]# cd /sys/class/net
[root@centos net]# ll
lrwxrwxrwx 1 root root 0 7月  23 02:45 eth1 -> ../../devices/pci0000:00/0000:00:11.0/0000:02:01.0/net/eth1
lrwxrwxrwx 1 root root 0 7月  23 02:37 lo -> ../../devices/virtual/net/lo
当前网卡的名称为eth1
[root@centos net]# cat eth1/address 
00:0c:29:53:18:55
MAC地址为：00:0c:29:53:18:55
2..修改网卡配置文件
[root@centos net]# cd /etc/sysconfig/network-scripts/
[root@centos network-scripts]# ll
总用量 224
-rw-r--r--. 1 root root   137 7月  23 02:49 ifcfg-eth0
-rw-r--r--. 1 root root   254 1月  18 2017 ifcfg-lo
复制过来网卡名称为eth0,需要更改为正确的名称eth1
mv ifcfg-eth0 ifcfg-eth1
或者在该目录下新建ifcfg-eth1 配置文件
touch ifcfg-eth1
修改配置文件MAC地址
vi ifcfg-eth1
DEVICE=eth1
HWADDR=00:0C:29:53:18:55
TYPE=Ethernet
UUID=8800a9ae-dc62-4cbb-a003-d18d8dafe71e
ONBOOT=yes
NM_CONTROLLED=yes
BOOTPROTO=dhcp

注意两点：DEVICE 名称要和/sys/class/net 名称一样
​                 HWADDR 修改为查到正确的mac地址
wq保存退出
注意：以上网卡是动态获得ip地址
也可以静态设置ip
DEVICE=eth1                 #网卡对应的设备别名
BOOTPROTO=static            #网卡获得ip地址的方式（默认为dhcp，表示自动获取）
HWADDR=00:0C:29:53:18:55    #网卡MAC地址（物理地址）
IPADDR=192.168.2.100        #IP地址
NETMASK=255.255.255.0       #子网掩码 
GATEWAY=192.168.100.1      #设置网关的IP地址
DNS1=192.168.100.1         #设置DNS地址
ONBOOT=yes 

3.重启网卡
serivce network restart

[root@centos network-scripts]# service network restart
关闭环回接口：                                             [确定]
弹出环回接口：                                             [确定]
弹出界面 eth1： 
正在决定 eth1 的 IP 信息...完成。
​                                                           [确定]
网卡重启成功
ifconfig 查看

eth1      Link encap:Ethernet  HWaddr 00:0C:29:53:18:55  
​          inet addr:192.168.2.102  Bcast:255.255.255.255  Mask:255.255.255.0
​          inet6 addr: fe80::20c:29ff:fe53:1855/64 Scope:Link
​          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
​          RX packets:603 errors:0 dropped:0 overruns:0 frame:0
​          TX packets:386 errors:0 dropped:0 overruns:0 carrier:0
​          collisions:0 txqueuelen:1000 
​          RX bytes:57205 (55.8 KiB)  TX bytes:53843 (52.5 KiB)

lo        Link encap:Local Loopback  
​          inet addr:127.0.0.1  Mask:255.0.0.0
​          inet6 addr: ::1/128 Scope:Host
​          UP LOOPBACK RUNNING  MTU:65536  Metric:1
​          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
​          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
​          collisions:0 txqueuelen:0 
​          RX bytes:0 (0.0 b)  TX bytes:0 (0.0 b)


eth1 网卡已经成功启动了，到此就可以愉快的上网了。
