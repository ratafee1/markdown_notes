# SSH 框架整合一：带hibernate配置文件

创建项目，引入jar包

引入配置文件

创建包结构

创建相关类

引入页面

编写Action，配置Action

编写Service，并交给Spring管理

Spring和Struts2的整合方式一：Action由Struts2创建

​	引入一个插件包：struts_spring_plugin.jar

​	Action中提供service的set方法

Spring和Struts2的整合方式二：Action交给Spring创建

​	引入一个插件包

​	将Action配置到Spring中

​	在struts.xml中配置Action的class的时候，class中写的是在Spring的Action的类的id

​	注意：

​			Action多例的

​			手动注入Service

​	

​	Service调用Dao

​	Spring整合Hibernate

​		编写DAO继承HibernateDaoSupport

​		使用Hibernate模板

​	Spring的事务管理







# SSH 框架整合二：不带hibernate配置文件

​		数据库连接

​		Hibernate的相关属性

​		连接池

​		映射

# Hibernate的模板的使用

save（）

update（）

delete（）

get（）

find（）

findByCriteria（）

findByNamedQuery（）



# 延迟加载问题解决

​	将Session在Web层开启和关闭







# CRM综合练习

搭建开发环境

第一步：创建WEB项目，引入jar包

第二步：引入配置文件

​	struts2 的框架

​		web.xml

​			struts2的核心过滤器

​		struts.xml

​	spring的框架

​		jdbc.properties

​		log4j.properties

​		applicationContext.xml

​		web.xml

​	hibernate的框架

​		hibernate.cfg.xml		交给spring管理

创建相关的包结构

创建相关的类

