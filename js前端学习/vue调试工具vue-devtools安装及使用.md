# [vue调试工具vue-devtools安装及使用](https://www.cnblogs.com/chenhuichao/p/11039427.html)



本文主要介绍 vue的调试工具 vue-devtools 的安装和使用

工欲善其事, 必先利其器, 快快一起来用vue-devtools来调试开发你的vue项目吧

**安装:** 

1.到github下载：

```
git clone https://github.com/vuejs/vue-devtools
```

2.在vue-devtools目录下安装依赖包

```
cd vue-devtools``cnpm install
```

3.修改manifest.json文件

![img](https://images2017.cnblogs.com/blog/1055753/201708/1055753-20170827152637589-1152375876.png)

把"persistent":false改成true

 ![img](https://images2017.cnblogs.com/blog/1055753/201708/1055753-20170827152825605-2132649031.png)

 4.编译代码

```
npm run build
```

 

5.扩展Chrome插件

Chrome浏览器 >  更多程序 > 拓展程序 

点击加载已解压程序按钮, 选择 vue-devtools > shells > chrome 放入, 安装成功如下图

![img](https://images2017.cnblogs.com/blog/1055753/201708/1055753-20170827153453605-1374332252.png)

 

 \6. vue-devtools使用

vue项目, 打开f12, 选择vue就可以使用了.

vue是数据驱动的, 这样就能看到对应数据了, 方便我们进行调试

![img](https://images2017.cnblogs.com/blog/1055753/201708/1055753-20170827154217839-1267585798.png)

 

 怎么样, 是不是感觉工作效率提高了呢

 

温情提示: 

1.vue必须引入开发版, 使用min压缩版是不能使用devtools进行调试的

2.安装后, 需要关闭浏览器, 再重新打开, 才能使用

