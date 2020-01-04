# python3中替换python2中cmp函数





python 3.4.3 的版本中已经没有cmp函数，被operator模块代替，在交互模式下使用时，需要导入模块。

在没有导入模块情况下，会出现

![img](https://img-blog.csdn.net/20160810203900772?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

提示找不到cmp函数了，那么在python3中该如何使用这个函数呢？
所以要导入模块

![img](https://img-blog.csdn.net/20160810203944757?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

看下面给的内置函数

~~~
<span style="font-size:18px;">operator.lt(a, b)   
operator.le(a, b)   
operator.eq(a, b)   
operator.ne(a, b)   
operator.ge(a, b)   
operator.gt(a, b)   
operator.__lt__(a, b)   
operator.__le__(a, b)   
operator.__eq__(a, b)   
operator.__ne__(a, b)   
operator.__ge__(a, b)   
operator.__gt__(a, b) </span>
~~~



这几个函数就是用来替换之前的cmp的，之前使用cmp的同胞们，咱们以后就换上面这些函数咯。
先简单说下这几个函数的意思吧。

lt(a,b) 相当于 a<b     从第一个数字或字母（ASCII）比大小 

le(a,b)相当于a<=b

eq(a,b)相当于a==b     字母完全一样，返回True,

ne(a,b)相当于a!=b

gt(a,b)相当于a>b

ge(a,b)相当于 a>=b
函数的返回值是布尔哦

