# cmake快速入门



<https://blog.csdn.net/kai_zone/article/details/82656964>



### 本博文的大概框架：

1， cmake 的介绍，下载，安装和使用

2， cmake 的手册详解，我关注了 -C和-G 的使用

3， 在Linux中构建cmake 的工程

第一个问题： cmake 介绍，下载和安装以及使用：https://fukun.org/archives/0421949.html

cmake是kitware公司以及一些开源开发者在开发几个工具套件(VTK)的过程中所产生的衍生品。后来经过发展，最终形成体系，在2001年成为一个独立的开放源代码项目。其官方网站是www.cmake.org，可以通过访问官方网站来获得更多关于cmake的信息，而且目前官方的英文文档比以前有了很大的改进，可以作为实践中的参考手册。

cmake的流行离不开KDE4的选择。KDE开发者在使用autotools近10年之后，终于决定为KDE4项目选择一个新的工程构建工具。之所以如此，用KDE开发者们自己话来说，就是：只有少数几个“编译专家”能够掌握KDE现在的构建体系。在经历了unsermake，scons以及cmake的选型和尝试之后，KDE4最终决定使用cmake作为自己的构建系统。在迁移过程中，进展一场的顺利，并获得了cmake开发者的支持。所以，目前的KDE4开发版本已经完全使用cmake来进行构建。

随着cmake 在KDE4项目中的成功，越来越多的项目正在使用cmake作为其构建工具，这也使得cmake正在成为一个主流的构建体系。



cmake -G"MinGW Makefiles" ../

make