# [Windows 10 右键 在此处打开 CMD](https://www.cnblogs.com/dream4567/p/10693588.html)

## 1. 打开注册表

```
# 1. 使用快捷键打开 “运行”``#  win + r` `# 2. 在 “运行” 中输入``#  regedit` `# 3. 回车
```

## 2. 创建与设置 OpenCMDHere

```
# 1. 切换到``#   HKEY_CLASSES_ROOT\Directory\Background\shell\` `# 2. 创建``#   右击 shell ，新建项 “OpenCMDHere”``#   并在该项下，右击新建项 “command”` `# 3. 将 OpenCMDHere 默认改为 在此处打开命令窗口``#   1). 直接点击 OpenCMDHere``#   2). OpenCMDHere 的默认值数据改为 在此处打开命令窗口` `# 4. 创建 OpenCMDHere 的图片``#   1). 右键 新建字符串名， 名字为   Icon``#   2). 将值改为   cmd.exe
```

![img](https://img2018.cnblogs.com/blog/992770/201904/992770-20190412004304753-1698420250.png)

## 3. 设置 command

```
# 1. 直接改默认值就行``#   右键修改默认值，在键内填写下面的值即可``#     cmd.exe /s /k pushd \"%V\"
```

![img](https://img2018.cnblogs.com/blog/992770/201904/992770-20190412004318213-55089156.png)

## 4. 效果

- 右键任意文件夹就会出现

 ![img](https://img2018.cnblogs.com/blog/992770/201904/992770-20190412005833726-728397490.png)