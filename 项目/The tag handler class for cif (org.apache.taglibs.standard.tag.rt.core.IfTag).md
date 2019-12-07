# The tag handler class for "c:if" (org.apache.taglibs.standard.tag.rt.core.IfTag)



问题描述：

JSP页面中的JSTL标签不起作用，报错：The tag handler class for "c:if" (org.apache.taglibs.standard.tag.rt.core.IfTag) was not found on the Java Build Path

 

解决方法：

引入JSTL标签语句前添加代码

```
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8" isELIgnored="false"%>
```


![img](http://dl2.iteye.com/upload/attachment/0106/9132/49ae3727-4d8f-36d9-b748-473d746dc387.png)





# Eclipse中index.jsp文件显示The superclass "javax.servlet.http.HttpServlet" was not found on the Java Build



由错误可知，没有javax.servlet.http.HttpServlet类，此jar包位于Tomact的lib下，如图：

![img](https://img-blog.csdn.net/20180704174359653?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2EyMDEzMTI2Mzcw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)



因此，出现此错误的原因是没有添加Tomact包。右击web工程->属性或Build Path->Java Build Path->Libraries，如图：

![img](https://img-blog.csdn.net/20180704174930349?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2EyMDEzMTI2Mzcw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

可知，Apache Tomcat v9.0 library下并没有相应的jars包文件，因此会出现找不到javax.servlet.http.HttpServlet的错误。因此，要在此library下添加额外的jar包。点击 Add External JAERs，进入Tomcat安装路径lib文件下，ctrl-a选中所有jar包添加即可。

![img](https://img-blog.csdn.net/20180704175352238?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2EyMDEzMTI2Mzcw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)