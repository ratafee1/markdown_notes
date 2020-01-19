# [Spring与SpringMVC的区别](https://www.cnblogs.com/rainbow70626/p/9784938.html)



Spring是IOC和AOP的容器框架，SpringMVC是基于Spring功能之上添加的Web框架，想用SpringMVC必须先依赖Spring。
简单点的话可以将SpringMVC类比于Struts。
Spring是IOC和AOP的容器框架，SpringMVC是基于Spring功能之上添加的Web框架，想用SpringMVC必须先依赖Spring。
Spring可以说是一个管理bean的容器，也可以说是包括很多开源项目的总称，spring mvc是其中一个开源项目，所以简单走个流程的话，http请求一到，由容器（如：tomact）解析http搞成一个request，通过映射关系（路径，方法，参数啊）被spring mvc一个分发器去找到可以处理这个请求的bean，那tomcat里面就由spring管理bean的一个池子（bean容器）里面找到，处理完了就把响应返回回去。

SpringMVC是一个MVC模式的WEB开发框架;

Spring是一个通用解决方案, 最大的用处就是通过Ioc/AOP解耦, 降低软件复杂性, 所以Spring可以结合SpringMVC等很多其他解决方案一起使用, 不仅仅只适用于WEB开发

SSH:
SSH 为 struts+spring+hibernate 的一个集成框架，是目前较流行的一种JAVA Web应用程序开源框架。

　Struts

　　Struts是一个基于Sun J2EE平台的MVC框架，主要是采用Servlet和JSP技术来实现的。由于Struts能充分满足应用开发的需求，简单易用，敏捷迅速，在过去的一年中颇受关注。Struts把Servlet、JSP、自定义标签和信息资源(message resources)整合到一个统一的框架中，开发人员利用其进行开发时不用再自己编码实现全套MVC模式，极大的节省了时间，所以说Struts是一个非常不错的应用框架。

　　官方地址：http://struts.apache.org

　Spring

　　Spring是一个解决了许多在J2EE开发中常见的问题的强大框架。 Spring提供了管理业务对象的一致方法并且鼓励了注入对接口编程而不是对类编程的良好习惯。Spring的架构基础是基于使用JavaBean属性的Inversion of Control容器。然而，这仅仅是完整图景中的一部分：Spring在使用IOC容器作为构建完关注所有架构层的完整解决方案方面是独一无二的。 Spring提供了唯一的数据访问抽象，包括简单和有效率的JDBC框架，极大的改进了效率并且减少了可能的错误。Spring的数据访问架构还集成了Hibernate和其他O/R mapping解决方案。Spring还提供了唯一的事务管理抽象，它能够在各种底层事务管理技术，例如JTA或者JDBC事务提供一个一致的编程模型。Spring提供了一个用标准Java语言编写的AOP框架，它给POJOs提供了声明式的事务管理和其他企业事务–如果你需要–还能实现你自己的aspects。这个框架足够强大，使得应用程序能够抛开EJB的复杂性，同时享受着和传统EJB相关的关键服务。Spring还提供了可以和IoC容器集成的强大而灵活的MVC Web框架。

　　官方地址：spring: http://www.springsource.org

　Hibernate

　　Hibernate是一个开放源代码的对象关系映射框架，它对JDBC进行了非常轻量级的对象封装，使得Java程序员可以随心所欲的使用对象编程思维来操纵数据库。 Hibernate可以应用在任何使用JDBC的场合，既可以在Java的客户端程序实用，也可以在Servlet/JSP的Web应用中使用，最具革命意义的是，Hibernate可以在应用EJB的J2EE架构中取代CMP，完成数据持久化的重任。



