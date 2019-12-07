不保存退出vim	:q!

查看centos版本	cat /etc/issue

















# wget: unable to resolve host address的解决方法

wget：无法解析主机地址。这就能看出是DNS解析的问题。

解决办法：

登入root（VPS）
 `sudo vim /etc/resolv.conf`
 修改内容为下

```css
nameserver 8.8.8.8 #google域名服务器
nameserver 8.8.4.4 #google域名服务器
```























# [添加阿里云的yum源](https://www.cnblogs.com/yunjisuan1024/p/11652272.html)

1. 将旧的yum源移到其他位置，只使用阿里云的yum源安装软件

cd /etc/yum.repos.d

mkdir backup

mv C* backup

 

2. 下载阿里云的yum源，默认就下载到了/etc/yum.repos.d中，所以不需要切换到/etc/yum.repos.d目录下

CentOS 5

wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-5.repo

CentOS 6

wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-6.repo

CentOS 7

wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo





![](C:\Users\app\Desktop\1457147-20191011095019202-678384203.png)

3. 下载软件测试，安装了yum源之后，可以不用清理缓存和建立新的yum源，直接下载安装即可

yum -y install lrzsz





git需要很多依赖环境：因此安装git需要先安装下列软件：

[root@root]#yum install curl-devel expat-devel gettext-devel openssl-devel zlib-devel perl-devel gcc-c++

安装git

make prefix=/usr/local all

make prefix=/usr/local install



创建git用户

useradd git

设置git用户的密码

passwd git

#切换到git用户

su - git

git init --bare taotao.git

ll -a





git show 03fe



















#  mysql修改密码

use mysql;

update user set password=password("123456") where user="root";

flush privileges;

