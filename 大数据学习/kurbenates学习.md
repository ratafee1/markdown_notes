![image-20191224222805815](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191224222805815.png)

~~~
rpm --import rpm-package-key.gpg yum-key.gpg 
yum install docker-ce kubelet kubeadm kubectl -y
~~~





~~~
vim /usr/lib/systemd/system/docker.service
Environment="HTTPS_PROXY=http://www.ik8s.io:10080"
Environment="NO_PROXY=127.0.0.0/8,172.20.0.0/16"
systemctl daemon-reload
systemctl start docker
docker info
cat /proc/sys/net/bridge//bridge-nf-call-iptables 
~~~



~~~
rpm -ql kubelet
cat /etc/sysconfig/kubelet
tail /var/log/messages 
systemctl enable kubelet
systemctl enable docker

kubeadm init --help
kubeadm init 
~~~





# [WARNING: bridge-nf-call-iptables is disabled解决](https://www.cnblogs.com/wxwgk/p/11809497.html)

~~~
执行docker info出现如下警告

WARNING: bridge-nf-call-iptables is disabled
WARNING: bridge-nf-call-ip6tables is disabled

解决办法：

vi /etc/sysctl.conf

添加以下内容

net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1

最后再执行

sysctl -p

此时docker info就看不到此报错了
~~~

 

