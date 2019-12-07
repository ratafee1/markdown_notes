# Linux下安装python 2.7





安装依赖的库

```
yum -y install python-devel openssl openssl-devel gcc sqlite sqlite-devel mysql-devel libxml2-devel libxslt-devel
```

#### Python

**================================================= **

#### 下载python 2.7.13

[www.python.org](https://link.jianshu.com/?t=http://www.python.org/)

```
[root@server2 ~]# mkdir /software



[root@server2 ~]# cd /software/



[root@server2 software]# wget https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tgz



[root@server2 software]# ll



总用量 36852



-rw-r--r-- 1 root root 17076672 12月 18 04:21 Python-2.7.13.tgz



-rw-r--r-- 1 root root 20656090 1月  17 16:07 Python-3.5.3.tgz
```

#### 解压文件

```
[root@server2 software]# tar -zxf Python-2.7.13.tgz 
```

#### 进入目录

```
[root@server2 software]# cd Python-2.7.13
```

#### 编译安装

```
[root@server2 Python-2.7.13]# ./configure --prefix=/usr/local/python2.7 --with-threads --enable-shared



[root@server2 Python-2.7.13]# make && make altinstall
```

#### 备份旧python相关命令

```
===> 有些版本/usr/bin/目录下不存在pip 忽略下面第一行命令即可



[root@server2 Python-2.7.13]# mv /usr/bin/pip /usr/bin/pip_old  



[root@server2 Python-2.7.13]# mv /usr/bin/easy_install /usr/bin/easy_install_old



[root@server2 Python-2.7.13]# mv /usr/bin/python /usr/bin/python_old
```

#### 新版本python命令做软连接，快捷使用

```
[root@server2 Python-2.7.13]# ln -s /usr/local/python2.7/lib/libpython2.7.so /usr/lib



[root@server2 Python-2.7.13]# ln -s /usr/local/python2.7/lib/libpython2.7.so.1.0 /usr/lib



[root@server2 Python-2.7.13]# ln -s /usr/local/python2.7/bin/python2.7 /usr/bin/python



[root@server2 Python-2.7.13]# ln -s /usr/local/python2.7/lib/libpython2.7.so /usr/lib64



[root@server2 Python-2.7.13]# ln -s /usr/local/python2.7/lib/libpython2.7.so.1.0 /usr/lib64
```

#### 测试python是否可以正常使用

```
[root@server2 ~]# python



Python 2.7.13 (default, Apr 11 2017, 11:14:36) 



[GCC 4.4.7 20120313 (Red Hat 4.4.7-18)] on linux2



Type "help", "copyright", "credits" or "license" for more information.



>>> 
```

#### 安装pip

下载最新版的pip，然后安装

```
[root@server2 Python-2.7.13]# cd /software/



[root@server2 software]# wget https://bootstrap.pypa.io/get-pip.py



[root@server2 software]# python get-pip.py 
```

查找pip的位置

```
[root@server2 software]# find / -name pip



/usr/local/python2.7/bin/pip
```

找到pip2.7的路径，为其创建软链作为系统默认的启动版本

```
[root@server2 software]# ln -s /usr/local/python2.7/bin/pip /usr/bin/pip
```

测试pip是否可用

```
[root@server2 software]# pip install Pillow



Collecting Pillow



  Downloading Pillow-4.1.0-cp27-cp27m-manylinux1_x86_64.whl (5.7MB)



    100% |████████████████████████████████| 5.7MB 129kB/s 



Collecting olefile (from Pillow)



  Downloading olefile-0.44.zip (74kB)



    100% |████████████████████████████████| 81kB 541kB/s 



Building wheels for collected packages: olefile



  Running setup.py bdist_wheel for olefile ... done



  Stored in directory: /root/.cache/pip/wheels/20/58/49/cc7bd00345397059149a10b0259ef38b867935ea2ecff99a9b



Successfully built olefile



Installing collected packages: olefile, Pillow



Successfully installed Pillow-4.1.0 olefile-0.44
```

#### 安装easy_install

下载最新版的easy_install，然后安装

```
[root@server2 software]# wget https://bootstrap.pypa.io/ez_setup.py



[root@server2 software]# python ez_setup.py 
```

找到easy_install的路径，为其创建软链作为系统默认的启动版本

```
[root@server2 software]# ln -s /usr/local/python2.7/bin/easy_install /usr/bin/easy_install
```

测试easy_install是否可用

```
[root@server2 software]# easy_install beautifulsoup4



Searching for beautifulsoup4



Reading https://pypi.python.org/simple/beautifulsoup4/



Downloading https://pypi.python.org/packages/9b/a5/c6fa2d08e6c671103f9508816588e0fb9cec40444e8e72993f3d4c325936/beautifulsoup4-4.5.3.tar.gz#md5=937e0df0d699a1237646f38fd567f0c6



Best match: beautifulsoup4 4.5.3



Processing beautifulsoup4-4.5.3.tar.gz



Writing /tmp/easy_install-OSpCW5/beautifulsoup4-4.5.3/setup.cfg



Running beautifulsoup4-4.5.3/setup.py -q bdist_egg --dist-dir /tmp/easy_install-OSpCW5/beautifulsoup4-4.5.3/egg-dist-tmp-m3PXo5



zip_safe flag not set; analyzing archive contents...



Moving beautifulsoup4-4.5.3-py2.7.egg to /usr/local/python2.7/lib/python2.7/site-packages



Adding beautifulsoup4 4.5.3 to easy-install.pth file



 



Installed /usr/local/python2.7/lib/python2.7/site-packages/beautifulsoup4-4.5.3-py2.7.egg



Processing dependencies for beautifulsoup4



Finished processing dependencies for beautifulsoup4
```

#### yum 安装工具只支持系统自带的python版本， 修改配置文件使其可正常使用

查看原版本python

```
[root@server2 software]# ll /usr/bin/python*



lrwxrwxrwx 1 root root   34 4月  11 11:20 /usr/bin/python -> /usr/local/python2.7/bin/python2.7



lrwxrwxrwx 1 root root    6 2月  15 14:33 /usr/bin/python2 -> python



-rwxr-xr-x 2 root root 9032 8月  18 2016 /usr/bin/python2.6  ==> 这个就是系统自带的python 



-rwxr-xr-x 1 root root 1418 8月  18 2016 /usr/bin/python2.6-config



lrwxrwxrwx 1 root root   16 4月  11 10:47 /usr/bin/python-config -> python2.6-config



-rwxr-xr-x 2 root root 9032 8月  18 2016 /usr/bin/python_old
```

修改配置文件 /usr/bin/yum

```
#!/usr/bin/python  ===>  修改为  #!/usr/bin/python2.6
```

测试yum是否可用

```
[root@server2 software]# yum -y install python-devel



已加载插件：fastestmirror, security



设置安装进程



Loading mirror speeds from cached hostfile



 * epel: mirrors.aliyun.com



包 python-devel-2.6.6-66.el6_8.x86_64 已安装并且是最新版本



无须任何处理
```

好了，大功告成。
<br />

### 优化

#### 编写一键安装python2.7的脚本

由于Centos 6.x的系统默认都是python2.6 ，如果服务器需要用2.7环境的话每台都得手动操作升级，工作量比较大， 编写脚本提升效率。（Centos 7.x版本的默认的python都是2.7.5版本）

创建用于存放python脚本的目录

```
[root@server2 software]# mkdir /script/python/



[root@server2 software]# cd /script/python/
```

由于国外python网站下载python安装包缓慢，可以提前下载下来，和install_py27.sh放在一起，在脚本中直接解压本地文件进行安装，我已经上传到网盘
[点击我下载](https://link.jianshu.com/?t=http://url.cn/47PjiDY)

开始编写脚本 install_py27.sh

```
#!/bin/sh 



# __author__ = 'junxi'



 



# This script is used by fast installed python2.7 ......



# write by 2017/04/11



 



echo "##############start run install for python2.7 script############"



yum -y install python-devel openssl openssl-devel gcc sqlite sqlite-devel mysql-devel libxml2-devel libxslt-devel



mkdir /software



mv Python-2.7.13.tgz /software



cd /software



tar -zxf Python-2.7.13.tgz



cd Python-2.7.13/



./configure --prefix=/usr/local/python2.7 --with-threads --enable-shared



make



make altinstall



mv /usr/bin/pip /usr/bin/pip_old



mv /usr/bin/easy_install /usr/bin/easy_install_old



mv /usr/bin/python /usr/bin/python_old



ln -s /usr/local/python2.7/lib/libpython2.7.so /usr/lib



ln -s /usr/local/python2.7/lib/libpython2.7.so.1.0 /usr/lib



ln -s /usr/local/python2.7/bin/python2.7 /usr/bin/python



ln -s /usr/local/python2.7/lib/libpython2.7.so /usr/lib64



ln -s /usr/local/python2.7/lib/libpython2.7.so.1.0 /usr/lib64



cd /software



wget https://bootstrap.pypa.io/get-pip.py



python get-pip.py



ln -s /usr/local/python2.7/bin/pip /usr/bin/pip



echo "############更换pip源为国内淘宝源##########"



mkdir /root/.pip/



touch /root/.pip/pip.conf



cat >> /root/.pip/pip.conf << EOF



[global]



index-url=http://mirrors.aliyun.com/pypi/simple/ 



 



[install]



trusted-host=mirrors.aliyun.com



EOF



 



pip install Pillow



sed -i 's#\/usr/bin/python#\/usr/bin/python2.6#g' /usr/bin/yum



yum -y install python-devel



echo 'the install script is the end......'
```

把Python-2.7.13.tgz文件和install_py27.sh脚本下载下来，放在同一个目录下：
运行下面命令进行安装

```
/bin/sh install_py27.sh
```

安装完成后执行python查看版本