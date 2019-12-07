# random.shuffle():用于将一个列表中的元素打乱



list = [20,16,10,5];

random.shuffle(list);

print(list)



# pycharm中Alt+6调出所有#TODO事件		#TODO表示未完成事项





# pip show 包名	#pip包安装的位置



# python -m pip install --upgrade pip	#升级pip





# 安装pip	curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

```
python get-pip.py
```





# pip install指定国内源镜像 pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple requests	阿里云：http://mirrors.aliyun.com/pypi/simple/





# 如何解决Python下 pip install module 下载慢解决方法？

对于Python来编程的用户最大的一个痛点就是，下载模块是下载速度特别慢，那么有没有解决方法呢？

换Python的pip下载源

1.首先安装一个模块 pqi，在cmd下

pip install pqi

![img](https://img-blog.csdn.net/20180128153859439?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxMDg5OTk4NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

2.查看pqi,相关命令

![img](https://img-blog.csdn.net/20180128154228401?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxMDg5OTk4NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

3.查看镜像源

![img](https://img-blog.csdn.net/20180128154358292?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxMDg5OTk4NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

可以看出镜像源有 豆瓣的、清华、pypi、阿里云等

4.查看当前源

![img](https://img-blog.csdn.net/20180128154708356?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxMDg5OTk4NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

python默认的pip 源是pypi

5.更换pip源，pip use xxx,可以随意选一个之前查看的源，推荐使用阿里云速度还是可以的。

![img](https://img-blog.csdn.net/20180128154844373?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxMDg5OTk4NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

至此，关于Python解决pip 下载速度慢的问题就解决了！







# Python import和import *的区别

> 导入方法一：

**import numpy**

这是导入了整个numpy模块，需要使用句点表示法访问需要的类。例如

**a = numpy.array([1,1])**

> 导入方法二：

**from numpy import \*** 

这是导入了numpy模块的每个类，可以直接使用类，无需句点表示法。例如：

**a=array([1,1])**

不推荐使用第二种导入方式，其没有明确地指出你使用了模块中的哪些类。

并且，如果导入了一个与程序文件中其他东西同名的类，会引发难以发现的错误。



# python程序休眠函数 time.sleep()





# python lambda函数三个特性四个用法

- lambda x, y: x*y；函数输入是x和y，输出是它们的积x*y
- lambda:None；函数没有输入参数，输出是None
- lambda *args: sum(args); 输入是任意个数的参数，输出是它们的和(隐性要求是输入参数必须能够进行加法运算)
- lambda **kwargs: 1；输入是任意键值对参数，输出是1





部分Python内置函数接收函数作为参数。典型的此类内置函数有这些。

- filter函数。此时lambda函数用于指定过滤列表元素的条件。例如filter(lambda x: x % 3 == 0, [1, 2, 3])指定将列表[1,2,3]中能够被3整除的元素过滤出来，其结果是[3]。
- sorted函数。此时lambda函数用于指定对列表中所有元素进行排序的准则。例如sorted([1, 2, 3, 4, 5, 6, 7, 8, 9], key=lambda x: abs(5-x))将列表[1, 2, 3, 4, 5, 6, 7, 8, 9]按照元素与5距离从小到大进行排序，其结果是[5, 4, 6, 3, 7, 2, 8, 1, 9]。
- map函数。此时lambda函数用于指定对列表中每一个元素的共同操作。例如map(lambda x: x+1, [1, 2,3])将列表[1, 2, 3]中的元素分别加1，其结果[2, 3, 4]。
- reduce函数。此时lambda函数用于指定列表中两两相邻元素的结合条件。例如reduce(lambda a, b: '{}, {}'.format(a, b), [1, 2, 3, 4, 5, 6, 7, 8, 9])将列表 [1, 2, 3, 4, 5, 6, 7, 8, 9]中的元素从左往右两两以逗号分隔的字符的形式依次结合起来，其结果是'1, 2, 3, 4, 5, 6, 7, 8, 9'。

