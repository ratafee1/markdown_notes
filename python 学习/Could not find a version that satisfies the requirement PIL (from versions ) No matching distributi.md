# Could not find a version that satisfies the requirement PIL (from versions: ) No matching distributi



1、软件版本

首先我先安装了

python 2.7

pip是  8.1.2

2、当我要安装PIL时，我在cmd下面输入：pip install PIL

错误提示是：

Could not find a version that satisfies the requirement PIL (from versions: )

No matching distribution found for PIL

如下图所示：



3、错误原因：后来找了很多方法，发现我的电脑是64位的，而官网只提供32位的，就是自己去官网下载的其他PIL，

也是32位的。

4、解决方法：找一个非官方的64位大家通用的PIL安装

（1）打开网址 http://www.lfd.uci.edu/~gohlke/pythonlibs/

（2）搜索PIL（ctrl+F），找到下面的图片所示，如果你的python是2.7版本就下载cp27的，3.5就下载cp35



![img](https://img-blog.csdn.net/20181008095211290?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3l1c2h1YW5ncGluZw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

（3）还要先安装wheel。选择相应版本下载后，打开cmd（win+r），你要先安装pip，具体pip安装百度一下怎么安装，

输入pip install wheel  后如图所示



![img](https://img-blog.csdn.net/20181008095523182?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3l1c2h1YW5ncGluZw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

（4）wheel安装好后，找到我们下载好的Pillow‑5.3.0‑cp27‑cp27m‑win_amd64.whl（这是我的版本）

由于我把它放在桌面，所以我打开cmd后，找到存放该文件的桌面，然后pip 安装就成功了

![img](https://img-blog.csdn.net/20181008095738187?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3l1c2h1YW5ncGluZw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

5、成功后，就可以使用了

![img](https://img-blog.csdn.net/20181008100329369?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3l1c2h1YW5ncGluZw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

6、安装的第三方模块位置：pycharm->File->Settings->Project Interpreter

![img](https://img-blog.csdn.net/20181008101744874?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3l1c2h1YW5ncGluZw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

7、卸载模块

pip uninstall xxx #卸载

例如卸载第三方模块redis:

![img](https://img-blog.csdn.net/20181008101910564?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3l1c2h1YW5ncGluZw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

