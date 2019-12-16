# 异常:This application has no explicit mapping for /error, so you are seeing this as a fallback.



抛出此异常表示访问的页面url没有匹配到对应的值，原因有如下三点：

Application启动类的位置不对：要将Application类放在最外侧，即包含所有子包 ，spring-boot会自动加载启动类所在包下及其子包下的所有组件。如下图所示：

![img](https://img-blog.csdnimg.cn/20190704075841702.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3F1c2hhbWluZw==,size_16,color_FFFFFF,t_70)

springboot的配置文件有误：关于application.yml或application.properties文件中视图解析器的配置问题。在pom文件下的spring-boot-starter-paren版本较高时使用以下配置：spring.mvc.view.prefix/spring.mvc.view.suffix，当pom文件下的spring-boot-starter-paren版本较低时使用以下配置：spring.view.prefix/spring.view.suffix。
控制器的url访问路径与注解@GetMapping（"/xxxx"）不匹配，如下图所示：



![img](https://img-blog.csdnimg.cn/20190704080626808.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3F1c2hhbWluZw==,size_16,color_FFFFFF,t_70)



![img](https://img-blog.csdnimg.cn/20190704080655743.png)





# No Identifier specified for entity的解决办法

问题：在springboot中整合JPA可能会遇到“No Identifier specified for entity”即没有标识实体类的错误
解决办法：

①，检查自己是否在实体类红写以下注解：

![img](https://img-blog.csdnimg.cn/20181227115325983.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NTg0MjYy,size_16,color_FFFFFF,t_70)

 ②，注意以上的注解所依赖的包必须为：（可能自己手快，直接alt+ctrl,例如Id注解在spring framake中也有）

            import javax.persistence.*;
③，如果上述都没有问题，很有可能这个是被导致的错误，根源不在这里，所以要继续追根溯源，多看控制台给出的错误信息

