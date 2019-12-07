### 目标

1.能够基于Vue初始化项目

2.能够基于Vue技术栈进行项目开发

3.能够使用Vue的第三方组件进行项目开发

4.能够说出前后端分离的开发模式

### 目录

1.项目概述

2.项目初始化

3.登录/退出功能

4.主页布局

5.用户管理模块

6.权限管理模块

7.分类管理模块

8.参数管理模块

9.商品管理模块

10.订单管理模块

11.数据统计模块



![image-20191204075726042](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191204075726042.png)

### 电商后台管理系统的功能

电商后台管理系统用于管理用户账号、商品分类、商品信息、订单、数据统计等业务功能。



![image-20191204080240364](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191204080240364.png)

![image-20191204080507969](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191204080507969.png)



![image-20191204080724039](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191204080724039.png)

jwt：状态保持工具，通过jwt可以模拟session登陆纪录功能

sequelize：操作数据库的框架



### windows下查看目录路径的命令chdir



![image-20191204084327210](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191204084327210.png)

1.安装插件 vue-cli-plugin-element

2.安装依赖 axios



### 将本地仓库上传到码云中

![image-20191204100442829](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191204100442829.png)



![image-20191204100747367](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191204100747367.png)



### 登陆退出功能

#### 1.登陆业务流程

1.在登陆页面输入用户名和密码

2.调用后台接口进行验证

3.通过验证之后，根据后台的响应状态跳转到项目主页

#### 2.登陆业务的相关技术点

1.http是无状态的

2.通过cookie在客户端纪录状态

3.通过session在服务器端纪录状态

4.通过token方式维持状态



![image-20191204103647051](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191204103647051.png)



![image-20191204103944082](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191204103944082.png)

git checkout -b login	创建分支

git branch	查看分支



### token

1.将登录成功之后的token，保存到客户端的sessionStorage中

​	1.1项目中除了登录之外的其他API接口，必须在登录之后才能访问

​	1.2token只应在当前网站打开期间生效，所以将token保存在sessionStorage中

windows.sessionStorage.setItem("token", res.data.token)

2.通过编程式导航跳转到后台主页，路由地址是/home

this.$router.push("/home")



### 路由导航守卫控制访问权限

如果用户没有登录，但是直接通过URL访问特定页面，需要重新导航到登录页面

![image-20191204160856194](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191204160856194.png)



![image-20191204161754815](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191204161754815.png)

### github使用

![image-20191204171749260](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191204171749260.png)

git remote -v

git remote rm origin

git push --set-upstream origin master

##### 如何一个本地库既关联GitHub，又关联码云

```
git remote add github git@github.com:ratafee1/learngit.git
```

```
git remote add gitee git@gitee.com:ratafee/learngit.git
```

```
git push github master
```

```
git push gitee master
```

##### 如何参与一个开源项目

- 在GitHub上，可以任意Fork开源仓库；
- 自己拥有Fork后的仓库的读写权限；
- 可以推送pull request给官方仓库来贡献代码。



### git checkout -b user 新建user分支，并切换到user分支

### git commit -m "完成用户列表功能的开发"

### git push -u origin user

### git merge user

### git push





![image-20191206092822778](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191206092822778.png)

