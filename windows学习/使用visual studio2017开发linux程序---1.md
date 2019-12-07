# 使用visual studio2017开发linux程序





## 环境：

　　win7_x64旗舰版、VS2017企业版、VMware10.0.2、CentOS7

　　在CentOS7上首先需要安装gcc、g++和gdbserver，这里就不多说

## 一、安装VS2017

　　1.1 安装VS2017时，必须要勾选“使用C++的Linux开发”工具集

![img](https://images2015.cnblogs.com/blog/405698/201703/405698-20170322131531424-869607879.png)

## 二、创建Linux项目

2.1 创建一个名称为"TestLinux"的解决方案，我们稍后会在这个解决方案内新建多个Linux项目（包括可执行程序、动态库、静态库等）

 ![img](https://images2015.cnblogs.com/blog/405698/201703/405698-20170322132335190-502636063.png)

2.2 添加新建项目可执行程序项目"test"

2.2.1

![img](https://images2015.cnblogs.com/blog/405698/201703/405698-20170322133214455-722958605.png)

2.2.2

![img](https://images2015.cnblogs.com/blog/405698/201703/405698-20170322133816924-1131669913.png)

 

2.3 添加新建项目，创建动态库

2.3.1

![img](https://images2015.cnblogs.com/blog/405698/201703/405698-20170322134059221-1059958868.png)

2.3.2

![img](https://images2015.cnblogs.com/blog/405698/201703/405698-20170322133946799-2068337467.png)

 

2.4 添加新建项目，创建静态库

2.4.1

![img](https://images2015.cnblogs.com/blog/405698/201703/405698-20170322134234377-226960732.png)

2.4.2

![img](https://images2015.cnblogs.com/blog/405698/201703/405698-20170322134325315-227328988.png)

 

## 三、添加测试代码

3.1 "test"项目中main.cpp代码：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
#include <cstdio>

#include "static_library/static.h"
#include "dynamic_library/dynamic.h.h"

int main()
{
    printf("hello from test!\n");
    printf("static_library test : %d\n", static_test(1));
    printf("dynamic_library test : %d\n", dynamic_test(1));
    return 0;
}
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 

3.2 在"static_library"项目中添加static.h和static.cpp

static.h

```
#ifndef _STATIC_LIBRARY_H_
#define _STATIC_LIBRARY_H_

int static_test(int n);

#endif // !_STATIC_LIBRARY_H_
```

 

static.cpp

```
#include "static.h"

int static_test(int n)
{
    return n * 3;
}
```

3.3 在"dynamic_library"项目中添加dynamic.h和dynamic.cpp

dynamic.h

```
#ifndef _DYNAMIC_LIBRARY_H_
#define _DYNAMIC_LIBRARY_H_

int dynamic_test(int n);

#endif // !_DYNAMIC_LIBRARY_H_
```

 

dynamic.cpp

```
#include "dynamic.h"

int dynamic_test(int n)
{
    return n * 2;
}
```

 

 

## 四、项目配置

4.1 "常规"配置

配置主程序：

![img](https://images2015.cnblogs.com/blog/405698/201704/405698-20170424173950397-922624997.png)

本地输出目录："$(ProjectDir)bin\$(Platform)\$(Configuration)\"修改为"$(ProjectDir)..\bin\$(Platform)\$(Configuration)\"，是为了将所有项目输出文件放到同一个目录中，方便相互引用。

目标文件扩展名：".out"修改为""，是为了不生成文件后缀，一般的Linux可执行程序是没有扩展名称的，可修改也可不修改。

远程生成根目录："~/projects"修改为"/root/projects/$(SolutionName)"，"~"和"/root"是等价的，但是运行时动态库搜索目录不支持~路径，添加“$(SolutionName)”是为了区分不同的解决方案下相同名称的项目。

远程生成项目目录："~/projects"修改为"/root/projects/$(SolutionName)"，"~"和"/root"是等价的，但是运行时动态库搜索目录不支持~路径，添加“$(SolutionName)”是为了区分不同的解决方案下相同名称的项目。

 配置动态库："$(RemoteRootDir)/$(ProjectName)"修改为"$(RemoteRootDir)"

![img](https://images2015.cnblogs.com/blog/405698/201703/405698-20170322143625877-1882461936.png)

本地输出目录："$(ProjectDir)bin\$(Platform)\$(Configuration)\"修改为"$(ProjectDir)..\bin\$(Platform)\$(Configuration)\"

目标文件扩展名：".out"修改为".so"

远程生成根目录："~/projects"修改为"/root/projects/$(SolutionName)"

配置类型："应用程序(.out)"修改为"动态库(.so)"

配置静态库：

![img](https://images2015.cnblogs.com/blog/405698/201703/405698-20170322144029190-1664168222.png)

本地输出目录："$(ProjectDir)bin\$(Platform)\$(Configuration)\"修改为"$(ProjectDir)..\bin\$(Platform)\$(Configuration)\"

目标文件扩展名：".out"修改为".a"

远程生成根目录："~/projects"修改为"/root/projects/$(SolutionName)"

配置类型："应用程序(.out)"修改为"动态库(.a)"

 

4.2 "调试"配置

![img](https://images2015.cnblogs.com/blog/405698/201703/405698-20170322160055799-1408708622.png)

程序："$(RemoteTargetPath)"修改为"$(RemoteRootDir)/bin/$(Platform)/$(Configuration)/$(TargetName)$(TargetExt)"，因为前面修改了本地输出目录导致远程输出目录也相应发生变化，这里修改一致。

工作目录："$(RemoteOutDir)"修改为"$(RemoteRootDir)/bin/$(Platform)/$(Configuration)"，这个是远程主机CentOS上的路径，如果设置不正确将找不到引用的动态库，调试程序无法启动。

![img](https://images2015.cnblogs.com/blog/405698/201703/405698-20170322160245721-261594917.png)

其他调试程序命令：""修改为"set solib-search-path $(SolutionDir)bin/$(Platform)/$(Configuration)"，这个是本地路径，调试符号是从本地加载的，否则调试动态库时，gdb会输出没有找到调试符号文件。

![img](https://images2015.cnblogs.com/blog/405698/201703/405698-20170322154403643-1401187621.png)

 

4.3 "C/C++"配置

![img](https://images2015.cnblogs.com/blog/405698/201703/405698-20170322145805486-1170110270.png)

附加包含目录：在"$(StlIncludeDirectories);%(AdditionalIncludeDirectories)"前面添加"./..;"，这个是远程主机CentOS上的路径，相当于gcc编译时指定"-I[路径]"选项；一般是先把需要的头文件从CentOS复制到windows，然后设置"配置属性"->"VC+ +目录"->"包含目录"，这样在编写Linux程序时，提示信息更加的友好^^。

 

4.4 "链接器"配置

![img](https://images2015.cnblogs.com/blog/405698/201703/405698-20170322150842033-704464666.png)

附加库目录：在"%(AdditionalLibraryDirectories)"前面添加"$(RemoteRootDir)/bin/$(Platform)/$(Configuration);"，这个是远程主机CentOS上的路径，相当于gcc编译时指定"-L[路径]"选项，用于指定引用动态库和静态库的目录；

![img](https://images2015.cnblogs.com/blog/405698/201703/405698-20170322151841643-633445539.png)

库依赖项：添加"dynamic_library;static_library"，相当于gcc设置"-l[库名称]"选项，用于指定链接时所需要的动态库和静态库名称，如果找不到依赖的库文件，链接时会错误，显示"无法解析的符号"。

![img](https://images2015.cnblogs.com/blog/405698/201703/405698-20170322151628330-468406396.png)

其他选项：添加"-Wl,-rpath=$(RemoteRootDir)/bin/$(Platform)/$(Configuration) "，指定程序运行时搜索动态库的路径。

 

## 五、开始调试

5.1 设置远程调试主机

![img](https://images2015.cnblogs.com/blog/405698/201703/405698-20170322153056518-727791470.png)

5.2 显示Linux控制台

![img](https://images2015.cnblogs.com/blog/405698/201703/405698-20170322153433580-472514108.png)

![img](https://images2015.cnblogs.com/blog/405698/201703/405698-20170322161118502-818801958.png)

最后的Demo下载地址：[TestLinux.zip](https://pan.baidu.com/s/1i53IDTz)

 

其他错误：

1）Inferior 1 (process 6074) exited normally

 ![img](https://images2017.cnblogs.com/blog/405698/201710/405698-20171016160542068-496174346.png)

通常是没有生成Debug可执行文件，若使用cmake，则添加CMAKE_BUILD_TYPE=Debug，重新生成即可。

 

 2）如果使用附加到进程(Native GDB代码)进行调试，提示输出"Cannot find or open the symbol file"

　　我们一般会在Linux中设置动态库加载路径，例如：export LD_LIBRARY_PATH=lib

​       此时程序加载动态库使用的就是相对路径，使用ldd命令查看

 　　![img](https://img2018.cnblogs.com/blog/405698/201911/405698-20191107114421921-1966888760.png)

 

　　因为是相对路径，所以VS2017远程附加到进程后，不能在此路径加载动态库的符号

　　解决办法：

　　　　设置动态库加载的绝对路径，例如：export LD_LIBRARY_PATH=/lib，重新启动程序，然后再使用VS2017重新附加进程