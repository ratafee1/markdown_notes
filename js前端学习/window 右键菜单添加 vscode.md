# window 右键菜单添加 vscode



![这里写图片描述](https://img-blog.csdn.net/20180830001158174?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0dyZWVrTXJ6eko=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)







![这里写图片描述](https://img-blog.csdn.net/20180830001257922?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0dyZWVrTXJ6eko=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

![这里写图片描述](https://img-blog.csdn.net/20180830001335376?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0dyZWVrTXJ6eko=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)



我最终想要的效果如上图所示：
- 右键文件夹，可以使用vscode打开
- 右键单文件，可以使用vscode打开
- 右键空白处，可以使用vscode打开

实现
新建一个名为 1.reg 的文件，找一个记事本或者sublime打开，名称无所谓，但是一定需要带上 .reg 后缀。
查看你自己的电脑的vscode安装目录，最简单的方法就是右键桌面的vscode，查看属性就知道了。以我的安装地址为例：C:\\Program Files\\Microsoft VS Code\\Code.exe ， 单反斜杠最好都换成双反斜杠。
复制一下内容到 1.reg 文件中。

~~~
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\*\shell\VSCode]
@="Open with Code"
"Icon"="C:\\Program Files\\Microsoft VS Code\\Code.exe"

[HKEY_CLASSES_ROOT\*\shell\VSCode\command]
@="\"C:\\Program Files\\Microsoft VS Code\\Code.exe\" \"%1\""

Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\Directory\shell\VSCode]
@="Open with Code"
"Icon"="C:\\Program Files\\Microsoft VS Code\\Code.exe"

[HKEY_CLASSES_ROOT\Directory\shell\VSCode\command]
@="\"C:\\Program Files\\Microsoft VS Code\\Code.exe\" \"%V\""

Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\Directory\Background\shell\VSCode]
@="Open with Code"
"Icon"="C:\\Program Files\\Microsoft VS Code\\Code.exe"

[HKEY_CLASSES_ROOT\Directory\Background\shell\VSCode\command]
@="\"C:\\Program Files\\Microsoft VS Code\\Code.exe\" \"%V\""

~~~



替换所有vscode的安装路径。
双击这个文件，之后都选 “是”。
