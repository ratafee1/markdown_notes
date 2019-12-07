# 跨平台IDE集成开发环境Clion教程：创建和开发简单CMake项目













**（一）基本CMake项目**

CMake是一个元构建系统，它使用名为 CMakeLists的脚本为特定环境生成构建文件（例如，Unix机器上的makefile）。在CLion中创建新的CMake项目时，会在项目根目录下自动生成CMakeLists.txt文件。

让我们从创建一个新的CMake项目开始。为此，请转到文件| New Project并选择C ++ Executable。在我们的示例中，项目名称是cmake_testapp和C ++ 14中选定的语言标准。

默认情况下，我们使用单个源文件main.cpp和包含以下命令的自动创建的根CMakeLists.txt获取项目：

![Clion教程：创建和开发简单CMake项目](https://www.evget.com/Content/images/201908/07/1565168957.png)

| 命令                                   | 描述                                                         |
| -------------------------------------- | ------------------------------------------------------------ |
| cmake_minimum_required(VERSION 3.13)   | 指定CMake所需的最低版本。它设置为CLion捆绑的CMake版本（始终是最新版本之一）。 |
| project(cmake_testapp)                 | 根据我们在项目创建期间提供的内容定义项目名称。               |
| set(CMAKE_CXX_STANDARD 14)             | 设置的 CMAKE_CXX_STANDARD变量的值设置为 14，因为我们选择创建项目时。 |
| add_executable(cmake_testapp main.cpp) | 添加将从main.cpp构建的 cmake_testapp可执行目标。             |

**（二）构建目标和运行/调试配置**

Target是使用CMake脚本构建的可执行文件或库。您可以在单个脚本中定义多个构建目标。

目前，我们的测试项目只有一个构建目标cmake_testspp。加载第一个项目后，CLion会自动添加与此目标关联的运行/调试配置：

![Clion教程：创建和开发简单CMake项目](https://www.evget.com/Content/images/201908/07/1565168958.png)

单击切换台中的编辑配置或选择运行| 从主菜单中编辑配置以查看详细信息。目标名称和可执行文件名称直接来自CMakeLists.txt：

![Clion教程：创建和开发简单CMake项目](https://image.evget.com/Content/images/201908/07/1565169143.png)

请注意此对话框的Before启动区域：默认情况下，Build设置为启动前步骤。因此，我们可以使用此配置不仅可以调试或运行目标，还可以执行构建。

**（三）添加目标并重新加载项目** 

现在让我们添加另一个源文件calc.cpp并从中创建一个新的可执行目标。

右键单击Project树中的根文件夹，然后选择New | C / C ++源文件。CLion提示将文件添加到现有目标：

 

![Clion教程：创建和开发简单CMake项目](https://image.evget.com/Content/images/201908/07/1565169291.png)

由于我们的目标是创建新目标，因此我们清除添加到目标复选框。因此，CLion通知我们新文件当前不属于任何目标：

![1565169322.png](https://image.evget.com/Content/images/201908/07/1565169322.png)

现在让我们在CMakeLists.txt中手动声明一个新目标。请注意，CLion将CMake脚本视为常规代码文件，因此我们可以使用代码辅助功能，如语法突出显示，自动完成和导航：

![1565169372.png](https://image.evget.com/Content/images/201908/07/1565169372.png)

我们可以重新加载项目一次（重新加载更改）或启用自动重新加载，让CLion静默应用CMakeLists.txt中的所有更改。启用/禁用自动重新加载的选项也可在“设置/首选项”中使用 构建，执行，部署| CMake。

![Clion教程：创建和开发简单CMake项目](https://image.evget.com/Content/images/201908/07/1565169419.png)

重新加载项目后，CLion为新目标添加了一个Run / Debug配置：

![1565169446.png](https://image.evget.com/Content/images/201908/07/1565169446.png)

**图书馆目标**

到目前为止，我们添加的目标是可执行文件，我们用它add_executable来声明它们。对于库目标，我们需要另一个命令 - add_library。例如，让我们从calc.cpp源文件创建一个静态库：

```
add_library (test_library STATIC calc.cpp)
```

与可执行文件一样，CLion在重新加载项目后为库目标添加了一个Run / Debug配置：

![Clion教程：创建和开发简单CMake项目](https://image.evget.com/Content/images/201908/07/1565169530.png)

但是，这是一个不可执行的配置，因此如果我们尝试运行或调试它，我们将获得![img](https://www.evget.com/static/admin/ueditor/themes/default/images/spacer.gif)Executable未指定的错误消息。

**（四）构建类型和CMake配置文件**

到目前为止创建的所有运行/调试配置都是调试配置，这是为我们的项目自动配置的CMake配置文件的默认构建类型。CMake配置文件是项目构建的一组选项。它指定的工具链，建设型，CMake的标志，用于存储构建工件路径，使编译选项和环境变量。

例如，要分离Debug和Release版本，我们需要![img](https://www.evget.com/static/admin/ueditor/themes/default/images/spacer.gif)在Settings / Preferences |中添加（）一个新的CMake配置文件 构建，执行，部署| CMake并将其构建类型设置为Release：

![Clion教程：创建和开发简单CMake项目](https://image.evget.com/Content/images/201908/07/1565169614.png)

请注意生成路径字段，该字段指定构建结果的位置。默认文件夹是cmake的建造，调试的调试配置文件和cmake的建造释放的释放曲线。您可以随时设置![img](https://www.evget.com/static/admin/ueditor/themes/default/images/spacer.gif)您选择的其他位置。

现在，运行/调试配置切换器显示两个可用的配置文件：

![Clion教程：创建和开发简单CMake项目](https://image.evget.com/Content/images/201908/07/1565169666.png)

切换配置或CMake配置文件可能会影响解析代码时使用的预处理器定义：例如，当Debug和Release版本有单独的标志或某些变量根据构建类型采用不同的值时。这称为解决上下文 ; 它定义了CLion如何执行语法突出显示以及其他代码洞察，如查找用法，重构和代码完成。在配置之间切换时，将自动更改当前文件的解析上下文。此外，您可以在上下文切换器中手动选择它（

![Clion教程：创建和开发简单CMake项目](https://image.evget.com/Content/images/201908/07/1565169694.png)

**（五）添加包含目录**

为了使用位于不同目录中的其他标头，我们需要将它们添加到所有目标或某些特定目标。例如，让我们在项目根目录下创建三个目录，包括，includes / general，includes / math，并在CMakeLists.txt中编写以下内容：

```
include_directories(includes/general)
```

 \- 包括所有目标的一般内容 ;

```
target_include_directories (cmake_testapp_calc PUBLIC includes/math)
```

 仅包含cmake_testapp_calc目标的数学运算。

请注意，target_include_directories应放在add_executable（或add_library）之后，目标名称已经可用。

现在，包含/ general或includes / math的标题可以直接包含在源代码中，例如：

![Clion教程：创建和开发简单CMake项目](https://image.evget.com/Content/images/201908/07/1565169922.png)

只有在CMakeLists.txt中明确包含它们或者将它们包含在已属于项目的其他文件中时，才能正确解析添加到项目中的标题和源。

**（六）链接库**

**静态库**

在第3步，我们创建了一个名为test_library的静态库。让我们从默认位置（即cmake-build-debug）将其放在项目根目录下的lib目录中，并将其链接到cmake_testapp目标。

我们将使用两个命令来链接静态库：find_library提供完整路径，然后我们通过变量将其直接传递给target_link_libraries命令${TEST_LIBRARY}。

![Clion教程：创建和开发简单CMake项目](https://image.evget.com/Content/images/201908/07/1565169967.png)

注：请确保放置target_link_libraries后add_executable的命令，从而使C进行库链接之前实际编制目标。

**动态库（Boost示例）**

为了说明链接动态库，我们将举例说明如何使用Boost.Test框架。

让我们int add_values (int a, int b) { return a+b;} 在calc.cpp中编写一个简单的函数 ，并使用函数声明创建一个关联的头文件calc.h。我们将在Boost.Test框架的帮助下测试这个函数。

随着我们的项目变得更加复杂，根CMakeLists.txt文件可能变得难以维护。为避免这种情况并构建透明的项目结构，我们将测试提取到子项目中。为此，我们将创建一个名为test的单独目录，并为其提供自己的CMakeLists.txt文件（在Project树中右键单击test并选择New | CMakeLists.txt）：

![Clion教程：创建和开发简单CMake项目](https://image.evget.com/Content/images/201908/07/1565170028.png)

子目录test / CMakeLists.txt脚本最初为空。让我们通过为libs插入Boost的实时模板来开始填充它。按或单击代码| 插入实时模板，然后选择： Ctrl+Jboost_with_libs

![Clion教程：创建和开发简单CMake项目](https://image.evget.com/Content/images/201908/07/1565170071.png)

让我们调整插入的代码，如下所示：

```
set (Boost_USE_STATIC_LIBS OFF) #enable dynamic linking#search for unit_test_framework
find_package (Boost REQUIRED COMPONENTS unit_test_framework)#create a cmake_testapp_boost target from test.cpp
add_executable (cmake_testapp_boost tests.cpp)#link Boost libraries to the new target
target_link_libraries (cmake_testapp_boost ${Boost_LIBRARIES})
```

此外，我们需要将add_subdirectory(test)命令放在根 CMakeLists.txt中，以使我们的测试目标cmake_testapp_boost可用于主构建。此命令放置在根CMake脚本中时，声明具有自己的CMakeLists.txt的子项目测试。 

重新加载两个CMakeLists.txt文件中的更改后，CLion将为cmake_testapp_boost目标创建运行/调试配置。这是我们可以立即运行/调试的常规CMake应用程序配置。但是，为了能够使用内置的测试运行器，让我们从Boost.Test模板创建另一个配置：

![Clion教程：创建和开发简单CMake项目](https://image.evget.com/Content/images/201908/07/1565170115.png)

现在让我们运行此配置并获取测试结果。测试运行器显示套件中的测试树，它们的输出，状态和持续时间：

![Clion教程：创建和开发简单CMake项目](https://image.evget.com/Content/images/201908/07/1565170153.png)


  