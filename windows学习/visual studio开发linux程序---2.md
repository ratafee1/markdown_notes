# visual studio开发linux程序

## 2.6.1 前言  

​       在linux环境下开发C++程序，除了需要掌握C++的知识外，还需要掌握如何写makefile和使用GDB进行调试，这对于不熟悉makefile和GDB的开发人员是比较麻烦的，目前vs2015及以上的版本能够支持linux c++程序的开发和调试，与传统vs上的windows编程不同的是，vs所需要的Linux环境需要搭载在一个linux的服务器上，vs相当于将windows系统和这个linux系统之间建立了某种映射，可以将代码复制到linux中对应的目录中，并且windows系统中的vs能够看到运行的情况，甚至是对代码进行断点调试，方便了在windows环境下的开发人员。

## 2.6.2 开发环境

在开发之前我们需要特定的环境和安装一些必须的软件：

1.环境：win7及以上版本的操作系统，CentOS或ubuntu等任何一种linux操作系统；

2.安装软件：windows操作系统上安装VS2015及以上版本；linux系统上安装gcc、g++和gdbserver,ssh-server软件；

环境的准备和依赖软件的安装请网上搜索自行安装，这里就不详细介绍。

注意：

(1).安装vs的时候我们除了安装一些基本的开发组件外，还需要安装c++的linux开发组件，如下图：



![img](https:////upload-images.jianshu.io/upload_images/17118229-ace45d083bff8697.png?imageMogr2/auto-orient/strip|imageView2/2/w/670/format/webp)

linux组件

(2).在linux系统上安装好ssh软件后，需要启动ssh-server服务，保证编译程序时，能将windows系统下的代码成功复制到linux中对应的目录中。

ssh-server服务的启动命令：

CentOS系统 : systemctl start sshd

redhat系统 : service sshd start

ubuntu系统 : service ssh start

## 2.6.3 创建简单的linux工程

我们以vs2017创建工程在ubuntu系统中运行为例：

1.创建一个linux平台的空项目，vs界面中选择：文件->新建->项目，然后弹出下面的对话框，开始新建工程；



![img](https:////upload-images.jianshu.io/upload_images/17118229-f84727b6ac73a8c3.png?imageMogr2/auto-orient/strip|imageView2/2/w/848/format/webp)

新建项目

2.配置远程环境，这是我们程序运行的linux环境，需要在配置ssh远程登录；

vs界面中选择：工具->选项->跨平台->连接管理器，界面如下图所示：



![img](https:////upload-images.jianshu.io/upload_images/17118229-baba92dd0659a4ed.png?imageMogr2/auto-orient/strip|imageView2/2/w/738/format/webp)

配置ssh登录

添加ssh远程登录连接配置：点击添加按钮，界面如下：



![img](https:////upload-images.jianshu.io/upload_images/17118229-071d853994f27082.png?imageMogr2/auto-orient/strip|imageView2/2/w/724/format/webp)

ssh配置

配置成功后，需要设置远程的存放代码的目录，即windows系统下的代码复制到linux中对应的目录；



![img](https:////upload-images.jianshu.io/upload_images/17118229-6e2f69f943cccc92.png?imageMogr2/auto-orient/strip|imageView2/2/w/389/format/webp)

工程设置



![img](https:////upload-images.jianshu.io/upload_images/17118229-3c1b2e7ae8f8684d.png?imageMogr2/auto-orient/strip|imageView2/2/w/967/format/webp)

远程目录设置

3.创建工程代码文件，创建一个test.cpp文件，写上经典的打印“Hello,World!”；



![img](https:////upload-images.jianshu.io/upload_images/17118229-7a834634199ebbf3.png?imageMogr2/auto-orient/strip|imageView2/2/w/809/format/webp)

hello工程

调试运行之前，我们需要调出Linux 控制台窗口；

vs界面中选择：调试->Linux 控制台

启动调试后，界面如下;



![img](https:////upload-images.jianshu.io/upload_images/17118229-327d9b54150c3a0e.png?imageMogr2/auto-orient/strip|imageView2/2/w/600/format/webp)

调试配置

程序在编译，运行之前会把windows系统下的代码复制到linux中对应的目录，如下图所示：



![img](https:////upload-images.jianshu.io/upload_images/17118229-bf3aafb381acf3bf.png?imageMogr2/auto-orient/strip|imageView2/2/w/418/format/webp)

代码目录设置



![img](https:////upload-images.jianshu.io/upload_images/17118229-9cfa0272c047e902.png?imageMogr2/auto-orient/strip|imageView2/2/w/342/format/webp)

代码

## 2.6.4 创建有依赖库的linux工程

以访问boost库的日期为例介绍如何调试并运行程序：

1.修改test.cpp的代码如下：

\#include <iostream>

\#include <boost/date_time/gregorian/gregorian.hpp>

using namespace boost::gregorian;

using namespace std;

int main()

{

​    date d(2019, 4, 20);

​    cout << "date: " << to_iso_extended_string(d) << endl;

​    return 0;

}

2.添加依赖的头文件目录



![img](https:////upload-images.jianshu.io/upload_images/17118229-cf860c5d3be105a5.png?imageMogr2/auto-orient/strip|imageView2/2/w/801/format/webp)

头文件配置

3.添加依赖库的文件目录



![img](https:////upload-images.jianshu.io/upload_images/17118229-9bb60348005f59e5.png?imageMogr2/auto-orient/strip|imageView2/2/w/962/format/webp)

库目录设置

4.添加依赖库的库文件名称



![img](https:////upload-images.jianshu.io/upload_images/17118229-33b734d870454aa4.png?imageMogr2/auto-orient/strip|imageView2/2/w/722/format/webp)

添加依赖库

5.完成了以上的步骤，编译程序成功，但在运行的时候会报错；如下图所示：



![img](https:////upload-images.jianshu.io/upload_images/17118229-ca18266c8c3746d3.png?imageMogr2/auto-orient/strip|imageView2/2/w/1103/format/webp)

错误信息

因为程序最终还是在linux系统中运行的，而使用vs2017做调试，只是与linux系统做了某种映射，使调试结果，运行结果在vs界面展示出来，所以我们需要在linux系统设置依赖库的查找路径。

linux下设置动态库的查找路径一般有以下三种方式：

(1).使用export LD_LIBRARY_PATH=XXX，这种方式在退出当前终端后就失效

export LD_LIBRARY_PATH=/root/opt/boost/lib:

(2).修改~ /.bashrc或~/.bash_profile或系统级别的/etc/profile中LD_LIBRARY_PATH的路径；

在文件中添加export LD_LIBRARY_PATH=/root/opt/boost/libsource

命令可以用于重新执行刚修改的初始化文件，使之立即生效，而不必注销并重新登录

source .bashrc 或者 source /etc/profile

(3).在/etc/ld.so.conf文件中添加库的搜索路径，这种方式不受用户的限制

在/etc/ld.so.conf下面加一行/root/opt/boost/lib

然后执行命令 /sbin/ldconfig 会更新搜索路径到 /etc/ld.so.cache，此文件保存已排好序的动态链接库名字列表；

程序运行时的搜索目录会从默认搜寻目录(/lib和/usr/lib)以及动态库配置文件/etc/ld.so.conf内所列的目录下,搜索出可共享的动态链接库(格式如前介绍,lib*.so*),进而创建出动态装入程序(ld.so)所需的连接和缓存文件。

6.在linux系统中修改程序的查找路径

使用方式一设置查找路径后，依然报错，因为方式一是临时的设置方式，只对当前终端生效；

使用方式二，方式三设置后，程序能正常调试运行；

如下图所示：



![img](https:////upload-images.jianshu.io/upload_images/17118229-c78668bf54bbcd1e.png?imageMogr2/auto-orient/strip|imageView2/2/w/785/format/webp)

运行界面

## 2.6.5 总结

1.使用vs2017做调试，只是与linux系统做了某种映射，使调试结果，运行结果在vs界面展示出来。 

2.程序编译时，如果不能把代码拷贝到linux中设置的远程目录下，则可能是ssh服务没有启动。 

3.程序调试运行时，如果找不到需要链接的库，则需要在linux系统中加入依赖库的查找路径。

