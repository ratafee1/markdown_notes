# [nodemon运行 提示错误：无法加载文件 C:\Users\gxf\AppData\Roaming\npm\nodemon.ps1，因为在此系统上禁止运行脚本。](https://www.cnblogs.com/xiaofenguo/p/11511789.html)



nodemon运行 提示错误：无法加载文件 C:\Users\gxf\AppData\Roaming\npm\nodemon.ps1，因为在此系统上禁止运行脚本。

这是你笔记本禁止运行脚本，解决办法

 

1.管理员身份打开powerShell

2.输入set-ExecutionPolicy RemoteSigned  

![img](https://img2018.cnblogs.com/blog/992473/201909/992473-20190912143440135-985998266.png)

.3 选择Y 或者A ，就好了