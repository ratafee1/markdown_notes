# CLion中使用CMake导入第三方库的方法









最近尝试使用CLion这款IDE来写C++程序。由于CLion的工程都是基于CMake来构建的，因此导入第三方库就需要在CMake文件中进行配置。这里把利用CMake导入第三方库的过程记录下来。

CMake的配置信息写在了CMakeList.txt文件中。在CMakeList.txt文件里，我们首先定义两个变量INC_DIR和LINK_DIR，用来表示头文件路径和库的路径。这里以我放在Downloads文件下的wfdb库为例，代码如下：

set(INC_DIR /Users/haoran/Downloads/wfdb/include)
set(LINK_DIR /Users/haoran/Downloads/wfdb/lib)
1
2
然后依次设置头文件目录、库目录、要链接的库，如下：

include_directories(${INC_DIR})
link_directories(${LINK_DIR})
link_libraries(wfdb)
1
2
3
注意以上代码须放在add_executable语句之前，而接下来的链接库操作则须放在add_executable语句之后。

使用如下语句完成库的链接操作：

target_link_libraries(wfdb_demo wfdb)
1
括号中的wfdb_demo为工程名称，wfdb为库的名称。

至此我们就完成第三方库的链接过程。

作为参考，此工程完整的CMake代码如下：

cmake_minimum_required(VERSION 3.6)
project(wfdb_demo)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES main.cpp)

set(INC_DIR /Users/haoran/Downloads/wfdb/include)
set(LINK_DIR /Users/haoran/Downloads/wfdb/lib)

include_directories(${INC_DIR})
link_directories(${LINK_DIR})
link_libraries(wfdb)

add_executable(wfdb_demo ${SOURCE_FILES})
target_link_libraries(wfdb_demo wfdb)



