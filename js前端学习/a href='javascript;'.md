

# \<a href='javascript:;'>



执行一段空白的javascript语句，返回空或者false值，从而防止链接跳转。跟当前a标签无关，这段代码始终都会执行。

演示如下：

1、设计一个a链接的代码，让其点击的时候执行一个alert(）函数：

[![img](https://gss0.baidu.com/-vo3dSag_xI4khGko9WTAnF6hhy/zhidao/wh%3D600%2C800/sign=5b7f8ffb47ed2e73fcbc8e2ab7318db3/fd039245d688d43fea91f18d701ed21b0ef43b90.jpg)](https://gss0.baidu.com/-vo3dSag_xI4khGko9WTAnF6hhy/zhidao/pic/item/fd039245d688d43fea91f18d701ed21b0ef43b90.jpg)

2、此时在页面上显示一个a链接效果：

[![img](https://gss0.baidu.com/94o3dSag_xI4khGko9WTAnF6hhy/zhidao/wh%3D600%2C800/sign=8d3f8487aa86c91708565a3ff90d5cf7/2fdda3cc7cd98d10191c6c4e2c3fb80e7aec9080.jpg)](https://gss0.baidu.com/94o3dSag_xI4khGko9WTAnF6hhy/zhidao/pic/item/2fdda3cc7cd98d10191c6c4e2c3fb80e7aec9080.jpg)

3、点击页面上的a链接，执行结果如下：

[![img](https://gss0.baidu.com/9vo3dSag_xI4khGko9WTAnF6hhy/zhidao/wh%3D600%2C800/sign=b99f106c04f79052ef4a4f383cc3fbf2/78310a55b319ebc42e7e15e68f26cffc1e17164e.jpg)](https://gss0.baidu.com/9vo3dSag_xI4khGko9WTAnF6hhy/zhidao/pic/item/78310a55b319ebc42e7e15e68f26cffc1e17164e.jpg)

**扩展资料：**

其他防止页面跳转的实现方式：

1、<a href="#" >test</a>；

点击链接，页面默认上滚到页的顶部， 但可以加上 onclick="return false"，防止上滚到页的顶部。

2、<a href="####" >test</a>；

使用2个到4个#，见的大多是"####"，也有使用"#all"等其他的。一个无意义的标签指定，不做任何处理。

3、<a href="javascript：void(0);" >test</a>； 

javascript:void(0) 表示一个死链接，执行空事件。

