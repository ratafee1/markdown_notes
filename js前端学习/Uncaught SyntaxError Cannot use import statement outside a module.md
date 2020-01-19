# Uncaught SyntaxError: Cannot use import statement outside a module



# [ES6模块化使用遇到的问题](https://www.cnblogs.com/sherryStudy/p/es6_module.html)

# 前言

最近在学习ES6模块化时，遇到了一些问题，通过查询相关资料得以解决，本篇随笔详细记录了解决方法。

# 具体内容

以下定义一个模块common.js

![img](https://img2018.cnblogs.com/i-beta/1647663/201911/1647663-20191112104157139-270092749.png)

在test.html中引入上述定义的模块

 ![img](https://img2018.cnblogs.com/i-beta/1647663/201911/1647663-20191129141535784-2001356323.png)

运行上述test.html文件时，浏览器控制台如下错误

“**Uncaught SyntaxError: Cannot use import statement outside a module**”

 ![img](https://img2018.cnblogs.com/i-beta/1647663/201911/1647663-20191112104223896-734495032.png)

错误原因：浏览器还没有完全支持ES6模块，所以需要在导入模块时，在script标签中加“type = module”,如下图所示：

 ![img](https://img2018.cnblogs.com/i-beta/1647663/201911/1647663-20191129142234456-1388185542.png)

但是，解决完上述问题之后，新的问题又出现了，浏览器控制台报如下报错：

 ![img](https://img2018.cnblogs.com/i-beta/1647663/201911/1647663-20191112104255843-1659311619.png)

以上问题表示出现的**跨域**问题，可是**为什么会出现跨域呢**？

　　首先，script标签是自带跨域功能的，这也就是我们在某些场合会通过jsonp并结合script来请求资源的原因。

　　其次，导致跨域的原因是协议、域名、端口号只要有一个不同就会导致跨域，而这里的协议通常是指http协议、https等协议，也就是说http、data、chrome、chrome-extension、https这些协议是支持跨域请求的，而file协议并不支持。

　　file协议：本地文件传输协议，主要目的就是用于访问本地计算机中的文件，好比通过Windows的资源管理器去打开文件或者通过右键单击打开一样，然后通过“file:文件路径”这样的形式去访问。

　　浏览器通过file协议和http协议去访问文件（**file:///**文件路径和http://访问路径）的区别：

- file协议用于访问本地计算机的文件，好比通过资源管理器打开文件一样，需要注意的是它是针对本地的，即file协议是访问本机的文件资源。
- http协议访问本地的html文件，相当于将本机作为一台http服务器，然后通过localhost访问的是本地服务器，再通过http服务器去访问本机的文件资源。
- 通俗说，file协议只是简单请求本地文件，将其作为一个服务器未解析的静态文件打开；而http是在本地搭建一个服务器再通过服务器解析打开文件。

　　当在本机直接打开一个网页（例如本例的test.html），该网页通过script标签引入了common.js，则在浏览器地址栏呈现的地址是“file:///C:/Users/wangqin/Desktop/test.html”,这样会出现跨域问题。而http、https等协议支持跨域请求，所以解决办法可以**通过在本地搭建一个服务器去进行资源的访问来解决跨域问题**。

　　搭建本地服务器，可以使用Apache Tomcat；亦可以使用vue-cli或webpack-cli脚手架搭建。具体操作方法此处不再赘述。

