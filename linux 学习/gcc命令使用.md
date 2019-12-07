# gcc命令



gcc -c	只执行编译，不链接

ar -rc	test.a	test.o





**(一) gcc的基本用法(二) 警告提示功能选项(三) 库操作选项(四) 调试选项(五) 交叉编译选项**

------


**(一) gcc的基本用法**
使用gcc编译器时，必须给出一系列必要的调用参数和文件名称。**不同参数的先后顺序对执行结果没有影响，只有在使用同类参数时的先后顺序才需要考虑**。如果使用了多个 -L 的参数来定义库目录，gcc会根据多个 -L 参数的先后顺序来执行相应的库目录。
因为很多gcc参数都由多个字母组成，所以gcc参数不支持单字母的组合，Linux中常被叫短参数（short options），如 -dr 与 -d -r 的含义不一样。gcc编译器的调用参数大约有100多个，其中多数参数我们可能根本就用不到，这里只介绍其中最基本、最常用的参数。

**gcc最基本的用法是**：gcc [options] [filenames]
其中，options就是编译器所需要的参数，filenames给出相关的文件名称，最常用的有以下参数：

**-c**    
**只编译，不链接成为可执行文件**。编译器只是由输入的 .c 等源代码文件**生成 .o 为后缀的目标文件**，通常用于编译不包含主程序的子程序文件。
**-o output_filename**    
确定**输出文件的名称**为output_filename。同时这个名称不能和源文件同名。如果不给出这个选项，gcc就给出默认的可执行文件 a.out 。
**-g**
**产生符号调试**工具（GNU的 gdb）所必要的符号信息。想要对源代码进行调试，就必须加入这个选项。
**-O**
对程序进行**优化编译、链接**。采用这个选项，整个源代码会在编译、链接过程中进行优化处理，这样产生的可执行文件的执行效率可以提高，但是编译、链接的速度就相应地要慢一些，而且对执行文件的调试会产生一定的影响，造成一些执行效果与对应源文件代码不一致等一些令人“困惑”的情况。因此，**一般在编译输出软件发行版时使用此选项**。
**-O2**
比 -O 更好的优化编译、链接。当然整个编译链接过程会更慢。
**-Idirname**
将 dirname 所指出的目录加入到程序**头文件目录列表**中，是在预编译过程中使用的参数。
说明：
C程序中的头文件包含两种情况：
\#include <stdio.h>
\#include "stdio.h"
其中，使用尖括号（<>），预处理程序 cpp 在系统默认包含文件目录（如/usr/include）中搜索相应的文件；使用双引号，预处理程序 cpp 首先在当前目录中搜寻头文件，如果没有找到，就到指定的 dirname 目录中去寻找。
在程序设计中，**如果需要的这种包含文件分别分布在不同的目录中，就需要逐个使用 -I 选项给出搜索路径**。
**-Ldirname**
将dirname所指出的目录加入到**程序函数库文件的目录列表**中，是在链接过程中使用的参数。在默认状态下，链接程序 ld 在系统默认路径中（如 /usr/lib）寻找所需要的库文件。这个选项告诉链接程序，首先到 -L 指定的目录中去寻找，然后到系统默认路径中寻找；如果函数库存放在多个目录下，就需要依次使用这个选项，给出相应的存放目录。
**-lname**
**链接时装载名为 libname.a 的函数库**。该函数库位于系统默认的目录或者由 -L 选项确定的目录下。例如，-lm 表示链接名为 libm.a 的数学函数库。

例子：假定有一个程序名为 test.c 的C语言源代码文件，要生成一个可执行文件。
\#include <stdio.h>
int main(void)
{
​    printf("Hello world/n");
​    return 0;
}
最简单的办法：gcc test.c -o test
首先，gcc需要调用**预处理程序 cpp**，由它负责展开在源文件中定义的宏，并向其中插入“#include”语句所包含的内容；接着，gcc调用 **ccl 和 as**，将处理后的源代码编译成目标代码；最后，gcc调用**链接程序 ld**，把生成的目标代码链接成一个可执行程序。因此，默认情况下，预编译、编译链接一次完成。

编译过程的分步执行：
为了更好地理解gcc的工作过程，我们可以让在gcc工作的**4个阶段**中的任何一个阶段中停止下来。相关的参数有：
**-E**
预编译后停下来，生成后缀为 **.i 的预编译文件**。
**-c**
编译后停下来，生成后缀为 **.o 的目标文件**。
**-S**
汇编后停下来，生成后缀为 **.s 的汇编源文件**。

第一步：进行预编译，使用 -E 参数
gcc **-E** test.c **-o test.i**
查看 test.i 文件中的内容，会发现 stdio.h 的内容确实都插到文件里去了，而其他应当被预处理的宏定义也都做了相应的处理。
第二步：将 test.i 编译为目标代码，使用 -c 参数
gcc **-c** test.c **-o test.o**
第三步：生成汇编源文件
gcc **-S** test.c **-o test.s**
第四步：将生成的目标文件链接成可执行文件
gcc **test.o** - o **test**

对于稍微复杂的情况，比如有多个源代码文件、需要链接库或有其他比较特别的要求，就要给定适当的调用选项参数。

例子：整个源代码程序由两个文件 testmain.c 和 testsub.c 组成，程序中使用了系统提供的数学库（所有与浮点相关的数学运算都必须使用数学库）。
gcc testmain.c testsub.c **-lm** -o test
其中，**-lm 表示链接系统的数学库 libm.a** 。

说明：
在编译一个包含许多源文件的工程时，若只用一条gcc命令来完成编译是非常浪费时间的。假如项目中有100个源文件需要编译，并且每个源文件中都包含一万行代码，如果像上面那样仅用一条gcc命令来完成编译工作，那么gcc需要将每个源文件都重新编译一遍，然后再全部链接起来。很显然，这样浪费的时间相当多，尤其是当用户只是修改了其中某个文件的时候，完全没有必要将每个文件都重新编译一遍，因为很多已经生成的目标文件是不会发生改变的。要解决这个问题，需要借助像**make**这样的工具。

**(二) 警告提示功能选项**
gcc包含完整的出错检查和警告提示功能，它们可以帮助Linux程序员写出更加专业的代码。
**(1) -pedantic 选项**
当gcc在编译不符合ANSI/ISO C 语言标准的源代码时，将产生相应的警告信息。

 

 

[cpp]

view plain

 [copy](http://blog.csdn.net/delphiwcdj/article/details/6555073#)

 

 [print](http://blog.csdn.net/delphiwcdj/article/details/6555073#)[?](http://blog.csdn.net/delphiwcdj/article/details/6555073#)

1. \#include <stdio.h>  
2.   
3.  void main(void)  
4.  {  
5. ​     long long int var = 1;  
6. ​     printf("It is not standard C code!/n");  
7.  }  

 

![pic](http://hi.csdn.net/attachment/201106/19/45214_1308484963nVGv.jpg)

 

它有以下问题：
\> main 函数的返回值被声明为 void，但实际上应该是 int。
\> 使用了 GNU 语法扩展，即使用 long long 来声明64位整数，不符合 ANSI/ISO C 语言标准。
\> main 函数在终止前没有调用 return 语句。

**(2) -Wall 选项**
除了 -pedantic 之外，gcc 还有一些其他编译选项，也能够产生有用的警告信息。这些选项大多以 -W 开头。其中最有价值的当数 -Wall 了，使用它能够使 gcc 产生尽可能多的警告信息。

![pic](http://hi.csdn.net/attachment/201106/19/45214_13084849643GqG.jpg)

 

gcc 给出的警告信息虽然从严格意义上说不能算作错误，但却和可能成为错误来源。一个优秀的程序员应该尽量避免产生警告信息，使自己的代码始终保持简洁、优美和健壮的特性。
**建议**：gcc 给出的警告信息是很有价值的，它们不仅可以帮助程序员写出更加健壮的程序，而且还是跟踪和调试程序的有力工具。**建议在用 gcc 编译源代码时始终带上 -Wall 选项**，并把它逐渐培养成一种习惯，这对找出常见的隐式编程错误很有帮助。

**(3) -Werror 选项**
在处理警告方面，另一个常用的编译选项是 -Werror。**它要求 gcc 将所有的警告当成错误进行处理，这在使用自动编译工具（如 Make 等）时非常有用**。如果编译时带上 -Werror 选项，那么 gcc 会在所有产生警告的地方停止编译，迫使程序员对自己的代码进行修改。只有当相应的警告信息消除时，才可能将编译过程继续朝前推进。

![pic](http://hi.csdn.net/attachment/201106/19/45214_130848496584OO.jpg)

 

**(4) -Wcast-align 选项**
当源程序中地址不需要对齐的指针指向一个地址需要对齐的变量地址时，则产生一个警告。例如，char * 指向一个 int * 地址，而通常在机器中 int 变量类型是需要地址能被2或4整除的对齐地址。

**(5) 其他常用选项**
-v                            输出 gcc 工作的详细过程
--target-help       显示目前所用的gcc支持CPU类型
-Q                           显示编译过程的统计数据和每一个函数名

**(三) 库操作选项**
在[Linux](http://lib.csdn.net/base/linux)下开发软件时，完全不使用第三方函数库的情况是比较少见的，通常来讲都需要借助一个或多个函数库的支持才能够完成相应的功能。
从程序员的角度看，函数库实际上就是一些头文件（.h）和库文件（.so 或 .a）的集合。虽然Linux下的大多数函数都默认将头文件放到 /usr/include/ 目录下，而库文件则放到 /usr/lib/ 目录下，但并不是所有的情况都是这样。正因如此，gcc 在编译时必须有自己的办法来查找所需要的头文件和库文件。常用的方法有：
**(1) -I** 
可以向 gcc 的头文件搜索路径中添加新的目录。
**(2) -L** 
如果使用了不在标准位置的库文件，那么可以通过 -L 选项向 gcc 的库文件搜索路径中添加新的目录。
**(3) -l** 
Linux下的库文件在命名时有一个约定，就是应该以 lib 这3个字母开头，由于所有的库文件都遵循了同样的规范，因此在用 -l 选项指定链接的库文件名时可以省去 lib 这3个字母。例如，gcc 在对 -lfoo 进行处理时，会自动去链接名为 libfoo.so 的文件。
**(4) -static**
Linux下的库文件分为两大类，分别是：动态链接库（通常以 .so 结尾）和静态链接库（通常以 .a 结尾）。
两者的差别仅在程序执行时所需的代码是在运行时动态加载的，还是在编译时静态加载的。
默认情况下，gcc 在链接时优先使用动态链接库，只有当动态链接库不存在时才考虑使用静态链接库。
如果需要的话，可以在编译时加上 -static 选项，强制使用静态链接库。
**(5) -shared**
生成一个共享的目标文件，它能够与其他的目标一起链接生成一个可执行的文件。

**(四) 调试选项**
对于Linux程序员来讲，**gdb（GNU Debugger）**通过与 gcc 的配合使用，为基于Linux的软件开发提供了一个完善的调试环境。常用的有：
**(1) -g 和 -ggdb**
默认情况下，gcc 在编译时不会将调试符号插入到生成的二进制代码中，因为这样会增加可执行文件的大小。如果需要在编译时生成调试符号信息，可以使用 gcc 的 -g 或 -ggdb 选项。
gcc 在产生调试符号时，同样采用了分级的思路，开发人员可以通过在 -g 选项后附加数字1、2、3指定在代码中加入调试信息的多少。默认的级别是2（-g2），此时产生的调试信息包括：扩展的符号表、行号、局部或外部变量信息。
级别3（-g3）包含级别2中的所有调试信息以及源代码中定义的宏。
级别1（-g1）不包含局部变量和与行号有关的调试信息，因此只能够用于回溯跟踪和堆栈转储。
回溯追踪：指的是监视程序在运行过程中函数调用历史。
堆栈转储：则是一种以原始的十六进制格式保存程序执行环境的方法。

注意：使用任何一个调试选项都会使最终生成的二进制文件的大小急剧增加，同时增加程序在执行时的开销，因此，调试选项通常仅在软件的开发和调试阶段使用。

**(2) -p 和 -pg**
会将剖析（Profiling）信息加入到最终生成的二进制代码中。剖析信息对于找出程序的性能瓶颈很有帮助，是协助Linux程序员开发出高性能程序的有力工具。

**(3) -save-temps**
保存编译过程中生成的一些列中间文件。
\# gcc test.c -o test **-save-temps**
**除了生成执行文件test之外，还保存了test.i 和 test.s 中间文件，供用户查询调试。**

**(五) 交叉编译选项**
通常情况下使用 gcc 编译的目标代码都与使用的机器是一致的，但 gcc 也支持交叉编译的功能，**能够编译其他不同CPU的目标代码**。
使用 gcc 开发嵌入式系统，我们几乎都是以通用的PC机（X86）平台来做宿主机，通过 gcc 的交叉编译功能对其他嵌入式CPU的开发任务。
（具体的选项设置，此处省略）







关于undefined reference这样的问题，大家其实经常会遇到，在此，我以详细地示例给出常见错误的各种原因以及解决方法，希望对初学者有所帮助。

**1.  链接时缺失了相关目标文件（.o）**

​    测试代码如下：

[![img](https://gss0.baidu.com/-Po3dSag_xI4khGko9WTAnF6hhy/zhidao/wh%3D600%2C800/sign=105baa12a364034f0f98ca009ff35509/a71ea8d3fd1f4134ccaa61b12d1f95cad0c85e5b.jpg)](https://gss0.baidu.com/-Po3dSag_xI4khGko9WTAnF6hhy/zhidao/pic/item/a71ea8d3fd1f4134ccaa61b12d1f95cad0c85e5b.jpg)

 

​    然后编译。

gcc -c test.c  gcc –c main.c 

​    得到两个 .o 文件，一个是 main.o，一个是 test.o ，然后我们链接 .o 得到可执行程序：

gcc -o main main.o 



​    这时，你会发现，报错了：

main.o: In function `main':  main.c:(.text+0x7): undefined reference to `test'  collect2: ld returned 1 exit status 

​    这就是最典型的undefined reference错误，因为在链接时发现找不到某个函数的实现文件，本例中test.o文件中包含了test()函数的实现，所以如果按下面这种方式链接就没事了。

gcc -o main main.o test.o 

   【扩展】：其实上面为了让大家更加清楚底层原因，我把编译链接分开了，下面这样编译也会报undefined reference错，其实底层原因与上面是一样的。

gcc -o main main.c //缺少test()的实现文件 

需要改成如下形式才能成功，将test()函数的实现文件一起编译。

gcc -o main main.c test.c //ok,没问题了 

**2.    链接时缺少相关的库文件（.a/.so）**

​    在此，只举个静态库的例子，假设源码如下。

[![img](https://gss0.baidu.com/9fo3dSag_xI4khGko9WTAnF6hhy/zhidao/wh%3D600%2C800/sign=4ec1deab9ceef01f4d4110c3d0ceb51d/242dd42a2834349bf975094ac1ea15ce37d3be8a.jpg)](https://gss0.baidu.com/9fo3dSag_xI4khGko9WTAnF6hhy/zhidao/pic/item/242dd42a2834349bf975094ac1ea15ce37d3be8a.jpg)



​    先把test.c编译成静态库(.a)文件

gcc -c test.c  ar -rc test.a test.o 

​    至此，我们得到了test.a文件。我们开始编译main.c

gcc -c main.c 

​    这时，则生成了main.o文件，然后我们再通过如下命令进行链接希望得到可执行程序。

gcc -o main main.o 

​    你会发现，编译器报错了：

/tmp/ccCPA13l.o: In function `main':  main.c:(.text+0x7): undefined reference to `test'  collect2: ld returned 1 exit status 

​    其根本原因也是找不到test()函数的实现文件，由于该test()函数的实现在test.a这个静态库中的，故在链接的时候需要在其后加入test.a这个库，链接命令修改为如下形式即可。

gcc -o main main.o ./test.a  //注：./ 是给出了test.a的路径 

​     【扩展】：同样，为了把问题说清楚，上面我们把代码的编译链接分开了，如果希望一次性生成可执行程序，则可以对main.c和test.a执行如下命令。

gcc -o main main.c ./test.a  //同样，如果不加test.a也会报错 

**3.    链接的库文件中又使用了另一个库文件**

​    这种问题比较隐蔽，也是我最近遇到的与网上大家讨论的不同的问题，举例说明如下，首先，还是看看测试代码。

[![img](https://gss0.baidu.com/-fo3dSag_xI4khGko9WTAnF6hhy/zhidao/wh%3D600%2C800/sign=c4707f0ae8fe9925cb596156049872e7/023b5bb5c9ea15cec88a87c6be003af33b87b29d.jpg)](https://gss0.baidu.com/-fo3dSag_xI4khGko9WTAnF6hhy/zhidao/pic/item/023b5bb5c9ea15cec88a87c6be003af33b87b29d.jpg)



​    从上图可以看出，main.c调用了test.c的函数，test.c中又调用了fun.c的函数。
​    首先，我们先对fun.c，test.c，main.c进行编译，生成 .o文件。

gcc -c func.c  gcc -c test.c  gcc -c main.c 

​    然后，将test.c和func.c各自打包成为静态库文件。

ar –rc func.a func.o  ar –rc test.a test.o 

​    这时，我们准备将main.o链接为可执行程序，由于我们的main.c中包含了对test()的调用，因此，应该在链接时将test.a作为我们的库文件，链接命令如下。

gcc -o main main.o test.a 

​    这时，编译器仍然会报错，如下：

test.a(test.o): In function `test':  test.c:(.text+0x13): undefined reference to `func'  collect2: ld returned 1 exit status 

​    就是说，链接的时候，发现我们的test.a调用了func()函数，找不到对应的实现。由此我们发现，原来我们还需要将test.a所引用到的库文件也加进来才能成功链接，因此命令如下。

gcc -o main main.o test.a func.a 

​    ok，这样就可以成功得到最终的程序了。同样，如果我们的库或者程序中引用了第三方库（如pthread.a）则同样在链接的时候需要给出第三方库的路径和库文件，否则就会得到undefined reference的错误。

**4 多个库文件链接顺序问题**

​    这种问题也非常的隐蔽，不仔细研究你可能会感到非常地莫名其妙。我们依然回到第3小节所讨论的问题中，在最后，如果我们把链接的库的顺序换一下，看看会发生什么结果？

gcc -o main main.o func.a test.a 

​    我们会得到如下报错.

test.a(test.o): In function `test':  test.c:(.text+0x13): undefined reference to `func'  collect2: ld returned 1 exit status 

​    因此，我们需要注意，在链接命令中给出所依赖的库时，需要注意库之间的依赖顺序，依赖其他库的库一定要放到被依赖库的前面，这样才能真正避免undefined reference的错误，完成编译链接。

**5. 在c++代码中链接C语言的库**

​    如果你的库文件由c代码生成的，则在c++代码中链接库中的函数时，也会碰到undefined reference的问题。下面举例说明。

​    首先，编写c语言版库文件： 

  

[![img](https://gss0.baidu.com/-Po3dSag_xI4khGko9WTAnF6hhy/zhidao/wh%3D600%2C800/sign=8547f510c61b9d168a929267c3ee98b7/8644ebf81a4c510f2a7885d56859252dd52aa545.jpg)](https://gss0.baidu.com/-Po3dSag_xI4khGko9WTAnF6hhy/zhidao/pic/item/8644ebf81a4c510f2a7885d56859252dd52aa545.jpg)

 

​    编译，打包为静态库：test.a

gcc -c test.c  ar -rc test.a test.o 

​    至此，我们得到了test.a文件。下面我们开始编写c++文件main.cpp

​    

[![img](https://gss0.baidu.com/-4o3dSag_xI4khGko9WTAnF6hhy/zhidao/wh%3D600%2C800/sign=3c41fbfe44086e066afd374d323857cc/b7fd5266d01609242fc0c5d4dc0735fae7cd3413.jpg)](https://gss0.baidu.com/-4o3dSag_xI4khGko9WTAnF6hhy/zhidao/pic/item/b7fd5266d01609242fc0c5d4dc0735fae7cd3413.jpg)

​    然后编译main.cpp生成可执行程序：

g++ -o main main.cpp test.a 

​    会发现报错：

/tmp/ccJjiCoS.o: In function `main': main.cpp:(.text+0x7): undefined reference to `test()' collect2: ld returned 1 exit status 

​    原因就是main.cpp为c++代码，调用了c语言库的函数，因此链接的时候找不到，解决方法：即在main.cpp中，把与c语言库test.a相关的头文件包含添加一个extern "C"的声明即可。例如，修改后的main.cpp如下：

​    

[![img](https://gss0.baidu.com/9fo3dSag_xI4khGko9WTAnF6hhy/zhidao/wh%3D600%2C800/sign=d7ed04b19a58d109c4b6a1b4e168e087/11385343fbf2b21199aae281c28065380dd78e7c.jpg)](https://gss0.baidu.com/9fo3dSag_xI4khGko9WTAnF6hhy/zhidao/pic/item/11385343fbf2b21199aae281c28065380dd78e7c.jpg)

g++ -o main main.cpp test.a 

​    再编译会发现，问题已经成功解决。