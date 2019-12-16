# Intellij IDEA Debug调试技巧





1、这里以一个web工程为例，点击图中按钮开始运行web工程。

![img](https://img-blog.csdn.net/20160827205425445)



2、设置断点

![img](https://img-blog.csdn.net/20160827205906637?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)



3、使用postman发送http请求

![img](https://img-blog.csdn.net/20160827210019528)



4、请求发送之后会自动跳到断点处，并且在断点之前会有数据结果显示![img](https://img-blog.csdn.net/20160827210236904)



5、按F8 在 Debug 模式下，进入下一步，如果当前行断点是一个方法，则不进入当前方法体内，跳到下一条执行语句。

![img](https://img-blog.csdn.net/20160827210522280)



6、按F7在 Debug 模式下，进入下一步，如果当前行断点是一个方法，则进入当前方法体内，如果该方法体还有方法，则会进入该内嵌的方法中 .

![img](https://img-blog.csdn.net/20160827210654687)



7、继续按F7，则跳到StopWatch() 构造方法中。

![img](https://img-blog.csdn.net/20160827210916953)



8、跳出该方法，可以按Shift+F8，在 Debug 模式下，跳回原来地方。

![img](https://img-blog.csdn.net/20160827211143376)



9、这时我们按F8，会继续执行下一条语句。

![img](https://img-blog.csdn.net/20160827211301376)



10、当我们执行到第二个断点处，如果想直接执行到第三个断点处，可以按F9。

![img](https://img-blog.csdn.net/20160827211854941)



补充：Alt+F8 可以通过在 Debug 的状态下，选中对象，弹出可输入计算表达式调试框，查看该输入内容的调试结果 。

第一个红框是我输入的参数，第二个是我执行之后显示得结果。

![img](https://img-blog.csdn.net/20160827212713458)

