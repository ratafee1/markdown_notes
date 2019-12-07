# Windows右键新建MarkDown文件



Windows右键新建MarkDown文件
在桌面新建一个txt，输入一下内容

Windows Registry Editor Version 5.00
[HKEY_CLASSES_ROOT\.md\ShellNew]
"NullFile"=""
"FileName"="template.md"

另存为，加后缀.reg，保存类型为.txt，编码为Unicode

双击运行，确定，重启电脑，此时在桌面右键就有了新建md文件



