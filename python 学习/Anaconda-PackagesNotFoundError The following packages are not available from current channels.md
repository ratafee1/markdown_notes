# [PackagesNotFoundError: The following packages are not available from current channels](https://www.cnblogs.com/hellojiaojiao/p/10790273.html)



一、Anaconda作为一个工具包集成管理工具,下载python工具包是很方便的,直接敲:



conda install package_name



但是有时候安装一个工具包(如xmltodict)的时候,在当前的channels中找不到这个包,会提示:

接着根据提示 输入 anaconda search -t conda xmltodict搜索结果:

现在就选择一个合适的版本进行安装,如我选择这个:



conda-forge/xmltodict | 0.10.2 | conda | linux-64, win-32, win-64, osx-64



那么执行下面命令进行安装即可:



conda install -c https://conda.anaconda.org/conda-forge xmltodict



二、直接使用pip install package_name命令并本地的工具库中加载安装



















因为要用到lifelines 包，在cmd中使用conda install lifelines ,显示如下错误：

**PackagesNotFoundError: The following packages are not available from current channels:**

**- lifelines**

**Current channels:**

**- https://conda.anaconda.org/derickl/win-64**
**- https://conda.anaconda.org/derickl/noarch**
**- https://repo.anaconda.com/pkgs/main/win-64**
**- https://repo.anaconda.com/pkgs/main/noarch**
**- https://repo.anaconda.com/pkgs/free/win-64**
**- https://repo.anaconda.com/pkgs/free/noarch**
**- https://repo.anaconda.com/pkgs/r/win-64**
**- https://repo.anaconda.com/pkgs/r/noarch**
**- https://repo.anaconda.com/pkgs/msys2/win-64**
**- https://repo.anaconda.com/pkgs/msys2/noarch**

**To search for alternate channels that may provide the conda package you're**
**looking for, navigate to**

**https://anaconda.org**

**and use the search bar at the top of the page.**

解决办法：

首先输入 **anaconda search -t conda lifelines,**这样子就会显示可用的版本 ，我的显示效果如下所示：

![img](https://img2018.cnblogs.com/blog/1135237/201904/1135237-20190429143940009-211201405.png)

选择适合自己的版本，比如，我选择的就是conda-forge/lifelines,在命令行中输入：

**conda install -c https://conda.anaconda.org/conda-forge lifelines, 注意\**conda-forge和\*\*lifelines之间没有“/”。\*\**\***

