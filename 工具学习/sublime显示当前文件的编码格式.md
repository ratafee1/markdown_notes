# [sublime显示当前文件的编码格式](https://www.cnblogs.com/zhq--blog/p/8094003.html)



Sublime Text的默认设置是不开启显示编码的，如果想开启，可通过菜单Perference → Settings – User，在打开的配置文件里 ，在大括号后面，增加以下内容：
// Display file encoding in the status bar
"show_encoding": true,

// Display line endings in the status bar
"show_line_endings": true,

此时保存该配置文件，就能够看到sublime最底下一行会显示文件编码格式了。

以上的配置内容在Perference → Setting─Default都是false的。