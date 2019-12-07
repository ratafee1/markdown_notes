# Linux动态库常见问题之-"cannot open shared object file No such file or directory"的解决办法





Linux编写程序时，会经常的接触动态库，而在程序运行时可能会遇到类似于:libxxx.so cannot open shared object file No such file or directory的问题，这个代表什么含义，该怎么解决呢？

含义
这个问题代表的含义是，可执行程序在加载libxxx.so库时，找不到该库。至于找不到的情况分为两种:系统里根本不存在libxxx.so库；libxxx.so库在系统中存在，但是ld找不到，即libxxx.so库的位置没有告知ld。

解决办法
对于第一种情况，需要将libxxx.so放到系统ld的搜索路径中；对于第二种情况，通过locate工具定位libxxx.so的位置，然后将其放到ld的搜索路径中。

动态库的搜索路径配置
Linux下ld对于动态库的搜索路径的配置方式包括以下几种方式:

通过配置gcc编译器的参数-Wl,-rpath指定；
通过LD_LIBRARY_PATH环境变量指定；
通过/etc/ld.so.conf指定，切记修改完ld.so.conf之后必须执行/sbin/ldconfig -v同步动态库;
默认搜素路径/lib、/usr/lib/指定；
同时，上述几种方式存在一定的搜索顺序，按照搜索的先后依次为:1 > 2 > 3 > 4。对于动态库的搜索路径的配置可以参考21aspnet的这篇博文。

依赖动态库的查看
我们可以通过ldd(x86环境)或者CROSS_COMPILE-readelf -d(ARM环境，CROSS_COMPILE为具体交叉编译前缀，-d 为读取动态库信息的参数)来分析相应平台下可执行程序所依赖的动态库的情况，我们可以举一例：

test.c：

#include <stdio.h>                                                                                                                                                                                                  

void test() 
{
​    printf("test()\n");
}

$ $(CC) -fPIC -c test.c //生成test.o，-fPIC(Position-independent code)为了生成位置无关的代码，一般用于动态库编译选项。
$ $(CC) -static -fPIC -o libtest.so test.o

extern void test();                                                                                                                                                                                                 

main.c:

int main()
{
​    test();
​    return 0;
}

$ $(CC) -c main.c
$ $(CC) main.o -o main -L. -ltest

其中，CC代表不同平台的编译器；
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
通过，修改CC为gcc或者arm-linux-gnueabi-gcc分别生成X86、ARM平台下的main可执行程序，下面分别通过ldd和arm-linux-gnueabi-readelf查看main所依赖的动态库:

X86:

  ldd main
  linux-vdso.so.1 =>  (0x00007ffc98f6a000)
  libtest.so => /home/qihua/develop/linux/static_dynamic_libs/code/libtest.so (0x00007fe850df4000)
  libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fe850a10000)
  /lib64/ld-linux-x86-64.so.2 (0x000055950a132000)
1
2
3
4
5
ARM:

  arm-linux-gnueabi-readelf -d  main
  Dynamic section at offset 0xf10 contains 25 entries:
​    标记        类型                         名称/值
   0x00000001 (NEEDED)                     共享库：[libtest.so]
   0x00000001 (NEEDED)                     共享库：[libc.so.6]
   0x0000000c (INIT)                       0x10430
   0x0000000d (FINI)                       0x10590
   0x00000019 (INIT_ARRAY)                 0x20f08
   0x0000001b (INIT_ARRAYSZ)               4 (bytes)
   0x0000001a (FINI_ARRAY)                 0x20f0c
   0x0000001c (FINI_ARRAYSZ)               4 (bytes)
   0x00000004 (HASH)                       0x101ac
   0x00000005 (STRTAB)                     0x10300
   0x00000006 (SYMTAB)                     0x10200
   0x0000000a (STRSZ)                      200 (bytes)
   0x0000000b (SYMENT)                     16 (bytes)
   0x00000015 (DEBUG)                      0x0
   0x00000003 (PLTGOT)                     0x21000
   0x00000002 (PLTRELSZ)                   32 (bytes)
   0x00000014 (PLTREL)                     REL
   0x00000017 (JMPREL)                     0x10410
   0x00000011 (REL)                        0x10408
   0x00000012 (RELSZ)                      8 (bytes)
   0x00000013 (RELENT)                     8 (bytes)
   0x6ffffffe (VERNEED)                    0x103e8
   0x6fffffff (VERNEEDNUM)                 1
   0x6ffffff0 (VERSYM)                     0x103c8
   0x00000000 (NULL)                       0x0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
NOTE
如果一个可执行程序(常见于第三方库提供的bin)依赖了某些动态库，但可执行程序的CPU架构与本地的CPU架构不同(例如，可执行程序为32位，但本地系统为64位，本地系统安装的动态库也为64位的)，那么程序运行时，通过会提示:libxxx.so cannot open shared object file No such file or directory。这是，我们通过locate是可以定位到libxxx.so库，并且libxxx.so处于合适的ld搜索路径之下，这是我们通过修改libxxx.so路径是没有用的。解决问题的方式有这么几种:

1）下载与本地系统CPU架构相匹配的程序；

2）在本地系统重新编译该程序；

3）编译、更新与可执行程序CPU架构相匹配的动态库；





# [Linux缺少动态连接库.so--cannot open shared object file: No such file or directory](https://www.cnblogs.com/fanblogs/p/11141403.html)

1 Liunx安装报错时，缺少动态链接库时，形式如下：

/usr/local/libexec/gcc/x86_64-unknown-liunx-gnu/4.8.2/cc1: error while loading shared libraries: libmpc.so.2: cannot open shared object file: No such file or directory


那就表示Linux系統不知道libmpc.so.2 放在哪个目录下。

2  一般而言，有很多so文件会在/usr/local/lib or /usr/lib 目录下，现在改目录找到 libmpc.so.2。

3 在 /etc/ld.so.conf 中加入/usr/local/lib 这一行 ，将 /etc/ld.so.conf 保存后；

4 执行【/sbin/ldconfig –v 】命里更新一下才生效 ，然后在执行其他按装命令；

PS 若没有看到 libmpc.so.2的文件，说明这是个链接文件，需要创建一个，于是进入libmpc.so.2.0.0所在目录i386-linux-gnu创建链接文件；
root@Nikola :/usr/lib# ln -s libmpc.so.2.0.0 libmpc.so.2
创建成功，然后重新编译zlib，OK

















# 解决ImportError:lib***.so--cannot open shared object file: No such file or directory





1-软链接方式
​    1.1 找到文件

            find  /  -name  lib**.so   (缺失的动态链接库)  
    
    1.2 建立软链接
    
            ln - /path/to/lib**.so   /usr/lib
    
     1.3 sudo ldconfig

(后两种没有试过)

2- 修改LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/where/you/install/lib:$LD_LIBRARY_PATH
sudo ldconfig

3-修改/etc/ld.so.conf

vim  /etc/ld.so.conf

add  /where/you/install/lib

sudo ldconfig









# error while loading shared libraries 错误解决办法总结，





最近安装了装了几次ACE库，装起来会出现很多问题。 其实我发现直接按照ace的帮助文档进行编写。就差不多。

安装完成后，经常会遇到以下问题error while loading shared libraries，就是编译器没有找到相应的lib库文件。

 

从互联网上找到了一些文章， 解决了我的问题：贴一下。

缺少libclntsh.so.11.1

当运行./alibaba_prof.out时，报错./alibaba_prof.out: error while loading shared libraries: libclntsh.so.11.1: cannot open shared object file: No such file or directory



加载共享库出错:libclntsh.so.11.1:不能打开共享对象文件:没有这样的文件或目录

设置LD_LIBRARY_PATH=dir dir 为 libssl.so 的目录，假设libssl.so 在 /home/lib/ 目录下 执行命令： export LD_LIBRARY_PATH="/home/lib" 

 

 

while loading shared libraries: libXXX.so.1.2.3: cannot open shared object file: No such file or directory

 

关于 error while loading shared libraries: libXXX.so.1.2.3: cannot open shared object file: No such file or directory

此时你可以locate libXXX.so.1.2.3 (如果你的文件系统比以前有了变化，如安装了可能是需要的库的开发包，则需要 locate -u 一下)

然 后如果发现了libXXX.so.1.2.3的确存在，就把libXXX.so.1.2.3所在的目录加入到 /etc/ld.so.conf 中，或者在 /etc/ld.so.conf.d/ 下新建一文件，如 XXX.conf ，其内容是libXXX.so.1.2.3所在的目录。
如果发现libXXX.so.1.2.3不存在，你可能没安装包含库的程序。一般google一下“XXX linux”就能找到相应的软件。

如果提示是error while loading shared libraries: libXXX.so，但你的系统上有libXXX.so.5，你可以为libXXX.so.5
做一个软链接 ln -s libXXX.so.5 libXXX.so


如，我执行一个ACE开发包中的样例程序时，出现以下提示：
./logging_app: error while loading shared libraries: libACE.so.5.4.7: cannot open shared object file: No such file or directory


[root@lf ld.so.conf.d]# locate libACE.so.5.4.7
/opt/ace/ace/libACE.so.5.4.7
/opt/ace/lib/libACE.so.5.4.7
[root@lf ld.so.conf.d]# vi ace.conf

ace.conf中只有一行： /opt/ace/lib

然后再执行 ldconfig

OK，现在执行logging_app就没有错误了。


Trackback: http://tb.blog.csdn.net/TrackBack.aspx?PostId=1033392

 

 

 

以上文章解决了我的问题。
