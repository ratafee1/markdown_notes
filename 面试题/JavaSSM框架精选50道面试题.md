# JavaSSM框架精选50道面试题



1.什么是MVC框架？传统MVC框架存在的问题是什么？
MVC框架是为了解决传统MVC模式(Jsp + Servlet + JavaBean)的一些问题而出现的框架。

传统MVC模式存在问题：
1.所有的Servlet和Servlet映射都要配置在web.xml中，如果项目太大，web.xml就太庞大，并且不能实现模块化管理。
2.Servlet的主要功能就是接受参数、调用逻辑、跳转页面，比如像其他字符编码、文件上传等功能也要写在Servlet中，不能让Servlet主要功能而需要做处理一下特例。
3、接受参数比较麻烦(String name = request.getParameter(“name”),User user=new User user.setName(name))，不能通过model接收，只能单个接收，接收完成后转换封装model.
4、跳转页面方式比较单一(forword,redirect),并且当我的页面名称发生改变时需要修改Servlet源代码.

2简单介绍下你对springMVC特点的理解?
Spring MVC Framework有这样一些特点:
1.它是基于组件技术的.全部的应用对象,无论控制器和视图,还是业务对象之类的都是java组件.并且和Spring提供的其他基础结构紧密集成.
2.不依赖于Servlet API(目标虽是如此,但是在实现的时候确实是依赖于S.ervlet的)
3.可以任意使用各种视图技术,而不仅仅局限于JSP
4.支持各种请求资源的映射策略
5.它应是易于扩展的

3.简单的谈一下SpringMVC的工作流程？★★★★★
流程
1、用户发送请求至前端控制器DispatcherServlet
2、DispatcherServlet收到请求调用HandlerMapping处理器映射器。
3、处理器映射器找到具体的处理器，生成处理器对象及处理器拦截器(如果有则生成)一并返回给DispatcherServlet。
4、DispatcherServlet调用HandlerAdapter处理器适配器
5、HandlerAdapter经过适配调用具体的处理器(Controller，也叫后端控制器)。
6、Controller执行完成返回ModelAndView
7、HandlerAdapter将controller执行结果ModelAndView返回给DispatcherServlet
8、DispatcherServlet将ModelAndView传给ViewReslover视图解析器
9、ViewReslover解析后返回具体View
10、DispatcherServlet根据View进行渲染视图（即将模型数据填充至视图中）。
11、DispatcherServlet响应用户

4.SpringMVC与Struts2的主要区别？
目前企业中使用SpringMvc的比例已经远远超过Struts2,那么两者到底有什么区别，是很多初学者比较关注的问题，下面我们就来对SpringMvc和Struts2进行各方面的比较:

核心控制器（前端控制器、预处理控制器）：对于使用过mvc框架的人来说这个词应该不会陌生，核心控制器的主要用途是处理所有的请求，然后对那些特殊的请求 （控制器）统一的进行处理(字符编码、文件上传、参数接受、异常处理等等),spring mvc核心控制器是Servlet，而Struts2是Filter。
2.控制器实例：Spring Mvc会比Struts快一些（理论上）。Spring Mvc是基于方法设计，而Sturts是基于对象，每次发一次请求都会实例一个action，每个action都会被注入 属性，而Spring更像Servlet一样，只有一个实例，每次请求执行对应的方法即可(注意：由于是单例实例，所以应当避免全局变量的修改，这样会产生线程安全问题)。
3. 管理方式：大部分的公司的核心架构中，就会使用到spring,而spring mvc又是spring中的一个模块，所以spring对于spring mvc的控制器管理更加简单方便，而且提供了全 注解方式进行管理，各种功能的注解都比较全面，使用简单，而struts2需要采用XML很多的配置参数来管理（虽然也可以采用注解，但是几乎没有公司那 样使用）。
  4.参数传递：Struts2中自身提供多种参数接受，其实都是通过（ValueStack）进行传递和赋值，而SpringMvc是通过方法的参数进行接收。
  5.学习难度：Struts更加很多新的技术点，比如拦截器、值栈及OGNL表达式，学习成本较高，springmvc 比较简单，很较少的时间都能上手。
  6.intercepter 的实现机制：struts有以自己的interceptor机制，spring mvc用的是独立的AOP方式。这样导致struts的配置文件量还是比spring mvc大，虽然struts的配置能继承，所以我觉得论使用上来讲，spring mvc使用更加简洁，开发效率Spring MVC确实比struts2高。spring mvc是方法级别的拦截，一个方法对应一个request上下文，而方法同时又跟一个url对应，所以说从架构本身上spring3 mvc就容易实现restful url。struts2是类级别的拦截，一个类对应一个request上下文；实现restful url要费劲，因为struts2 action的一个方法可以对应一个url；而其类属性却被所有方法共享，这也就无法用注解或其他方式标识其所属方法了。spring3 mvc的方法之间基本上独立的，独享request response数据，请求数据通过参数获取，处理结果通过ModelMap交回给框架方法之间不共享变量，而struts2搞的就比较乱，虽然方法之间 也是独立的，但其所有Action变量是共享的，这不会影响程序运行，却给我们编码，读程序时带来麻烦。

spring mvc处理ajax请求,直接通过返回数据，方法中使用注解@ResponseBody，spring mvc自动帮我们对象转换为JSON数据。而struts2是通过插件的方式进行处理

在SpringMVC流行起来之前，Struts2在MVC框架中占核心地位，随着SpringMVC的出现，SpringMVC慢慢的取代struts2,但是很多企业都是原来搭建的框架，使用Struts2较多。

5.如何解决POST请求中文乱码问题，GET的又如何处理呢？
在web.xml中加入：
.
. CharacterEncodingFilter
. org.springframework.web.filter.CharacterEncodingFilter
.
. encoding
. utf-8
.
.
.
. CharacterEncodingFilter
. /*
.
以上可以解决post请求乱码问题。
对于get请求中文参数出现乱码解决方法有两个：
修改tomcat配置文件添加编码与工程编码一致，如下：
.
另外一种方法对参数进行重新编码：
. String userName = new String(request.getParamter(“userName”).getBytes(“ISO8859-1”),“utf-8”)
ISO8859-1是tomcat默认编码，需要将tomcat编码后的内容按utf-8编码

6.说出SpringMVC常用的5个注解？如何使用 SpringMVC完成JSON操作？：
常用的 5 个注解
@RequestMapping 、 @PathVariable 、 @RequestParam 、 @RequestBoy 、
@ResponseBody
如何使用 SpringMVC 完成 JSON 操作：
①. 配置 MappingJacksonHttpMessageConverter
②. 使用 @RequestBody 注解或 ResponseEntity 作为返回值

7. Spring 支持的事务管理类型有哪些？你在项目中使用哪种方式？怎么理解全局事务和局部事务？
  Spring 支持编程式事务管理和声明式事务管理。许多 Spring 框架的用户选择声明式事务管理，因为这种方式和应用程序的关联较少，因此更加符合轻量级容器的概念。声明式事务管理要优于编程式事务管理，尽管在灵活性方面它弱于编程式事务管理，因为编程式事务允许你通过代码控制业务。声明式事务又分为两种： a、基于XML的声明式事务 b、基于注解的声明式事务

事务分为全局事务和局部事务。全局事务由应用服务器管理，需要底层服务器 JTA 支持（如 WebLogic、 WildFly等）。局部事务和底层采用的持久化方案有关，例如使用 JDBC 进行持久化时，需要使用 Connetion 对象来操作事务；而采用 Hibernate 进行持久化时，需要使用 Session 对象来操作事务

8.Spring 提供的事务管理器都有哪些？他们共同实现的父接口是什么？Spring 的事务管理机制体现了什么设计模式，请简单说说
Spring 提供了如下所示的事务管理器。

这些事务的父接口都是 PlatformTransactionManager。 Spring 的事务管理机制是一种典型的策略模式，PlatformTransactionManager 代表事务管理接口，该接口定义了三个方法，该接口并不知道底层如何管理事务，但是它的实现类必须提供 getTransaction()方法（开启事务）、 commit()方法（提交事务）、 rollback()方法（回滚事务）的多态实现，这样就可以用不同的实现类代表不同的事务管理策略。使用 JTA 全局事务策略时，需要底层应用服务器支持，而不同的应用服务器所提供的 JTA 全局事务可能存在细节上的差异，因此实际配置全局事务管理器是可能需要使用 JtaTransactionManager 的子类，如： WebLogicJtaTransactionManager（ Oracle 的 WebLogic 服务器提供）、 UowJtaTransactionManager（ IBM 的 WebSphere 服务器提供）等。

9.Spring为什么要结合使用HandlerMapping以及HandlerAdapter来处理Handler?
符合面向对象中的单一职责原则，代码架构清晰，便于维护，最重要的是代码可复用性高。如HandlerAdapter可能会被用于处理多种Handler。

10.简单介绍下你对mybatis的理解？
1. mybatis配置    
2. SqlMapConfig.xml，此文件作为mybatis的全局配置文件，配置了mybatis的运行环境等信息。
3. mapper.xml文件即sql映射文件，文件中配置了操作数据库的sql语句。此文件需要在SqlMapConfig.xml中加载。
4. 通过mybatis环境等配置信息构造SqlSessionFactory即会话工厂
5. 由会话工厂创建sqlSession即会话，操作数据库需要通过sqlSession进行。
6. mybatis底层自定义了Executor执行器接口操作数据库，Executor接口有两个实现，一个是基本执行器、一个是缓存执行器。
7. Mapped Statement也是mybatis一个底层封装对象，它包装了mybatis配置信息及sql映射信息等。mapper.xml文件中一个sql对应一个Mapped Statement对象，sql的id即是Mapped statement的id。
8. Mapped Statement对sql执行输入参数进行定义，包括HashMap、基本类型、pojo，Executor通过Mapped Statement在执行sql前将输入的java对象映射至sql中，输入参数映射就是jdbc编程中对preparedStatement设置参数。
9. Mapped Statement对sql执行输出结果进行定义，包括HashMap、基本类型、pojo，Executor通过Mapped Statement在执行sql后将输出结果映射至java对象中，输出结果映射过程相当于jdbc编程中对结果的解析处理过程。
  1
  2
  3
  4
  5
  6
  7
  8
  9
  11.SpringMvc的控制器是不是单例模式,如果是,有什么问题,怎么解决?
  是单例模式,所以在多线程访问的时候有线程安全问题,不要用同步,会影响性能的,解决方案是在控制器里面不能写字段。

12.SpingMvc中的控制器的注解一般用哪个,有没有别的注解可以替代?
一般用@Conntroller注解,表示是表现层,不能用用别的注解代替

13. （1）@RequestMapping注解用在类上面有什么作用？（2）怎么样把某个请求映射到特定的方法上面？
    （1）@RequestMapping注解用于类上，表示类中的所有响应请求的方法都是以该地址作为父路径。

（2）如何把某个请求映射到特定的方法上面方案：直接在方法上面加上注解@RequestMapping,并且在这个注解里面写上要拦截的路径

14（1）如果在拦截请求中,我想拦截get方式提交的方法,怎么配置？
(2) 如果在拦截请求中,我想拦截提交参数中包含"type=test"字符串,怎么配置?

可以在@RequestMapping注解里面加上method=RequestMethod.GET
可以在@RequestMapping注解里面加上params=“type=test”

15（1）我想在拦截的方法里面得到从前台传入的参数,怎么得到？
（2）如果前台有很多个参数传入,并且这些参数都是一个对象的,那么怎么样快速得到这个对象？

直接在形参里面声明这个参数就可以,但必须名字和传过来的参数一样
直接在方法中声明这个对象,SpringMvc就自动会把属性赋值到这个对象里面

16（1） 怎么样在方法里面得到Request,或者Session？（2）SpringMVC怎么样设定重定向和转发的？
直接在方法的形参中声明request,SpringMvc就自动把request对象传入
在返回值前面加"forward:“就可以让结果转发,譬如"forward:user.do?name=method4” 在返回值前面加"redirect:“就可以让返回值重定向,譬如"redirect:http://www.baidu.com”

17（1）SpringMvc中函数的返回值都有哪些？（2） SpringMvc怎么处理返回值的？
（1）返回值可以有很多类型,有String, ModelAndView,当一般用String比较好
（2） SpringMvc根据配置文件中InternalResourceViewResolver的前缀和后缀,用前缀+返回值+后缀组成完整的返回值

18（1）SpringMvc用什么对象从后台向前台传递数据的？（2）SpringMvc中有个类把视图和数据都合并的一起的,叫什么？
通过ModelMap对象,可以在这个对象里面用put方法,把对象加到里面,前台就可以通过el表达式拿到
SpringMvc中有个类把视图和数据都合并的一起的叫ModelAndView

19（1）怎么样把ModelMap里面的数据放入Session里面？（2）SpringMvc怎么和AJAX相互调用的？
可以在类上面加上@SessionAttributes注解,里面包含的字符串就是要放入session里面的key
通过Jackson框架就可以把Java里面的对象直接转化成Js可以识别的Json对象
具体步骤如下
1.加入Jackson.jar
2.在配置文件中配置json的映射
3.在接受Ajax方法里面可以直接返回Object,List等,但方法前面要加上@ResponseBody注解

                  MyBatis部分    
1
20 谈一下使用MyBatis(IBatis)的好处是什么？
ibatis把sql语句从Java源程序中独立出来，放在单独的XML文件中编写，给程序的维护带来了很大便利。
ibatis封装了底层JDBC API的调用细节，并能自动将结果集转换成Java Bean对象，大大简化了Java数据库编程的重复工作。
因为Ibatis需要程序员自己去编写sql语句，程序员可以结合数据库自身的特点灵活控制sql语句，
因此能够实现比hibernate等全自动orm框架更高的查询效率，能够完成复杂查询。

21讲下对MyBatis的缓存的理解？
MyBatis的缓存分为一级缓存和二级缓存,一级缓存放在session里面,默认就有,二级缓存放在它的命名空间里,默认是打开的,使用二级缓存属性类需要实现Serializable序列化接口(可用来保存对象的状态),可在它的映射文件中配置

22（1）IBatis和MyBatis在核心处理类分别叫什么？（2）IBatis和MyBatis在细节上的不同有哪些？【扩展】
（1）IBatis里面的核心处理类交SqlMapClient,MyBatis里面的核心处理类叫做SqlSession
（2）细节上的不同：在sql里面变量命名有原来的#变量# 变成了#{变量} 原来的变量变量变量变成了${变量},
原来在sql节点里面的class都换名字交type
原来的queryForObject queryForList 变成了selectOne selectList
原来的别名设置在映射文件里面放在了核心配置文件里

23 MyBatis里面的动态Sql是怎么设定的?用什么语法?
MyBatis里面的动态Sql一般是通过if节点来实现,通过OGNL语法来实现,但是如果要写的完整,必须配合where,trim节点,where节点是判断包含节点有内容就插入where,否则不插入,trim节点是用来判断如果动态语句是以and 或or开始,那么会自动把这个and或者or取掉

24 MyBatis实现一对多有几种方式？怎么操作的？
有联合查询和嵌套查询,
联合查询是几个表联合查询,只查询一次,通过在resultMap里面配置collection节点配置一对多的类就可以完成;
嵌套查询是先查一个表,根据这个表里面的结果的外键id,去再另外一个表里面查询数据,也是通过配置collection,但另外一个表的查询通过select节点配置

可以参考以下代码理解：

25 MyBatis实现一对一有几种方式?具体怎么操作的？
有联合查询和嵌套查询,
联合查询是几个表联合查询,只查询一次,通过在resultMap里面配置association节点配置一对一的类就可以完成;
嵌套查询是先查一个表,根据这个表里面的结果的外键id,去再另外一个表里面查询数据,也是通过association配置,但另外一个表的查询通过select属性配置

26什么是MyBatis的接口绑定？有什么好处？
接口映射就是在IBatis中任意定义接口,然后把接口里面的方法和SQL语句绑定,我们直接调用接口方法就可以,这样比起原来了SqlSession提供的方法我们可以有更加灵活的选择和设置.

27（1）接口绑定有几种实现方式,分别是怎么实现的? （2）什么情况下用注解绑定,什么情况下用xml绑定
（1）接口绑定有两种实现方式,一种是通过注解绑定,就是在接口的方法上面加上@Select @Update等注解里面包含Sql语句来绑定,另外一种就是通过xml里面写SQL来绑定,在这种情况下,要指定xml映射文件里面的namespace必须为接口的全路径名.

（2）当Sql语句比较简单时候,用注解绑定,当SQL语句比较复杂时候,用xml绑定,一般用xml绑定的比较多

28说一下orm与jdbc的区别？
jdbc只是一个java操作数据库的规范接口而已
orm不过是一种思想，对象关系映射。
ORM：是对象关系模型，如hibernate,让你以面向对象的方式去编程。封装了JDBC.
JDBC：是从底层访问数据库服务器。一般银行，金融行业为了安全起见，直接用JDBC访问

29传统mvc模式存在什么问题？或者说为何要使用框架？
传统MVC模式存在问题
(1)所有的Servlet和Servlet映射都要配置在web.xml中，如果项目太大，web.xml就太庞大，并且不能实现模块化管理。
(2)Servlet的主要功能就是接受参数、调用逻辑、跳转页面，比如像其他字符编码、文件上传等功能也要写在Servlet中，不能让Servlet主要功能而需要做处理一下特例。
(3)接受参数比较麻烦(String name = request.getParameter(“name”),User user=new User user.setName(name))，不能通过model接收，只能单个接收，接收完成后转换封装model.
(4)跳转页面方式比较单一(forword,redirect),并且当我的页面名称发生改变时需要修改Servlet源代码.

是为了解决传统MVC模式(Jsp + Servlet + JavaBean)的一些问题，才出现了后来的MVC框架。

30 mybatis与Hibernate有什么不同?
相同点：都是java中orm框架、屏蔽jdbc api的底层访问细节，使用我们不用与jdbc api打交道，就可以完成对数据库的持久化操作。jdbc api编程流程固定，还将sql语句与java代码混杂在了一起，经常需要拼凑sql语句，细节很繁琐。
ibatis的好处：屏蔽jdbc api的底层访问细节；将sql语句与java代码进行分离;提供了将结果集自动封装称为实体对象和对象的集合的功能.queryForList返回对象集合，用queryForObject返回单个对象；提供了自动将实体对象的属性传递给sql语句的参数。

Hibername的好处：Hibernate是一个全自动的orm映射工具，它可以自动生成sql语句，并执行并返回java结果。

不同点：
1、hibernate要比ibatis功能强大很多。因为hibernate自动生成sql语句。
2、ibatis需要我们自己在xml配置文件中写sql语句，hibernate我们无法直接控制该语句，我们就无法去写特定的高效率的sql。对于一些不太复杂的sql查询，hibernate可以很好帮我们完成，但是，对于特别复杂的查询，hibernate就很难适应了，这时候用ibatis就是不错的选择，因为ibatis还是由我们自己写sql语句。
ibatis可以出来复杂语句，而hibernate不能。
3、ibatis要比hibernate简单的多。ibatis是面向sql的，不同考虑对象间一些复杂的映射关系。

31 解释下MyBatis 中的动态SQL的理解？
对于一些复杂的查询，我们可能会指定多个查询条件，但是这些条件可能存在也可能不存在，例如在58同城上面找房子，我们可能会指定面积、楼层和所在位置来查找房源，也可能会指定面积、价格、户型和所在位置来查找房源，此时就需要根据用户指定的条件动态生成 SQL 语句。如果不使用持久层框架我们可能需要自己拼装 SQL 语句，还好 MyBatis 提供了动态 SQL 的功能来解决这个问题。 MyBatis 中用于实现动态 SQL 的元素主要有：

if
choose / when / otherwise
trim
where
set
foreach
其中
If标签: 多个条件查询时候用到
Where标签:可以自动处理第一个and
Foreach:应用场景 在多个ID查询时 传递的是集合或者是数组时候
Foreach的属性:
Collection: Java对象的属性名
Open:sql拼接开始的语句
Close: 结束时的SQL语句
Item:查询SQL中的字段名
Separator:语句拼接时候用什么进行分割

可以参考如下代码理解：

select * from t_blog where 1 = 1

and title = #{title}


and content = #{content}


and owner = #{owner}

当然也可以像下面这些书写。

select * from t_blog where 1 = 1

and title = #{title}


and content = #{content}


and owner = “owner1”


再看看下面这个例子。

select * from t_blog where id in

#{item}

32.JDBC编程有哪些不足之处，MyBatis是如何解决这些问题的？
① 数据库链接创建、释放频繁造成系统资源浪费从而影响系统性能，如果使用数据库链接池可解决此问题。
解决：在SqlMapConfig.xml中配置数据链接池，使用连接池管理数据库链接。
② Sql语句写在代码中造成代码不易维护，实际应用sql变化的可能较大，sql变动需要改变java代码。
解决：将Sql语句配置在XXXXmapper.xml文件中与java代码分离。
③ 向sql语句传参数麻烦，因为sql语句的where条件不一定，可能多也可能少，占位符需要和参数一一对应。
解决： Mybatis自动将java对象映射至sql语句。
④ 对结果集解析麻烦，sql变化导致解析代码变化，且解析前需要遍历，如果能将数据库记录封装成pojo对象解析比较方便。
解决：Mybatis自动将sql执行结果映射至java对象。

另外的参考回答
频繁的创建数据连接,关闭资源,造成性能的下降,使用数据文库连接池 解决这个问题用数据库连接池.在SqlMapConfig.xml 配置数据库连接池 c3p0 DBCP
Jdbc 编程sql 的可维护性不高. Mybatis采用配置文件的方式解决sql可维护的问题
在mapper.xml中配置 ,是sql与代码分离 可维护行变高
Jdbc 传入参数比较麻烦. 参数有时候多,参数要和占位符一一对应.
Mybatis 使用statement 的 paremterType 定义输入的参数类型
对结果解析比较麻烦. Mybatis 使用resultType 自动映射到pojo中解决了jdbc解析结果的麻烦

33.MyBatis编程步骤是什么样的？
① 创建SqlSessionFactory
② 通过SqlSessionFactory创建SqlSession
③ 通过sqlsession执行数据库操作
④ 调用session.commit()提交事务
⑤ 调用session.close()关闭会话

34.使用MyBatis的mapper接口调用时有哪些要求？
① Mapper接口方法名和mapper.xml中定义的每个sql的id相同
② Mapper接口方法的输入参数类型和mapper.xml中定义的每个sql 的parameterType的类型相同
③ Mapper接口方法的输出参数类型和mapper.xml中定义的每个sql的resultType的类型相同
④ Mapper.xml文件中的namespace即是mapper接口的类路径。

35.SqlMapConfig.xml中配置有哪些内容？
SqlMapConfig.xml中配置的内容和顺序如下：
properties（属性）
settings（配置）
typeAliases（类型别名）
typeHandlers（类型处理器）
objectFactory（对象工厂）
plugins（插件）
environments（环境集合属性对象）
environment（环境子属性对象）
transactionManager（事务管理）
dataSource（数据源）
mappers（映射器）

36.简单的说一下MyBatis的一级缓存和二级缓存？
Mybatis首先去缓存中查询结果集，如果没有则查询数据库，如果有则从缓存取出返回结果集就不走数据库。Mybatis内部存储缓存使用一个HashMap，key为hashCode+sqlId+Sql语句。value为从查询出来映射生成的java对象
Mybatis的二级缓存即查询缓存，它的作用域是一个mapper的namespace，即在同一个namespace中查询sql可以从缓存中获取数据。二级缓存是可以跨SqlSession的。

37.Mapper编写有哪几种方式？
①接口实现类继承SqlSessionDaoSupport
使用此种方法需要编写mapper接口，mapper接口实现类、mapper.xml文件
1、在sqlMapConfig.xml中配置mapper.xml的位置
.
.
.
.
2、定义mapper接口
3、实现类集成SqlSessionDaoSupport
mapper方法中可以this.getSqlSession()进行数据增删改查。
4、spring 配置
.
.
.
②使用org.mybatis.spring.mapper.MapperFactoryBean
1、在sqlMapConfig.xml中配置mapper.xml的位置
如果mapper.xml和mappre接口的名称相同且在同一个目录，这里可以不用配置
.
.
.
.
2、定义mapper接口
注意
1、mapper.xml中的namespace为mapper接口的地址
2、mapper接口中的方法名和mapper.xml中的定义的statement的id保持一致
3、 Spring中定义
.
.
.
.
③使用mapper扫描器
1、mapper.xml文件编写，
注意：
mapper.xml中的namespace为mapper接口的地址
mapper接口中的方法名和mapper.xml中的定义的statement的id保持一致
如果将mapper.xml和mapper接口的名称保持一致则不用在sqlMapConfig.xml中进行配置
2、定义mapper接口
注意mapper.xml的文件名和mapper的接口名称保持一致，且放在同一个目录
3、配置mapper扫描器
.
.
.
.
4、使用扫描器后从spring容器中获取mapper的实现对象
扫描器将接口通过代理方法生成实现对象，要spring容器中自动注册，名称为mapper 接口的名称。

38 mybatis中${value}与#{} 的区别是什么？
#{} 表示占位符.可以实现preparedStatement 向占位符中设置值,#{}可以接受简单类型,pojo属性值, #{}可以防止sql注入.如果preparedStatement 中传入简单类型 #{value} 可以随意写但是不可以不写
valueSQL语句的拼接.可以接收pojo属性值和简单数类型,如果preparedStatemet传入简单数据类型,{value} SQL 语句的拼接.可以接收pojo属性值和简单数类型,如果preparedStatemet 传入简单数据类型,valueSQL语句的拼接.可以接收pojo属性值和简单数类型,如果preparedStatemet传入简单数据类型,{value} 只能是value 不能改变

另外一种参考答案：
#{}是预编译处理，KaTeX parse error: Expected 'EOF', got '#' at position 21: …串替换。 Mybatis在处理#̲{}时，会将sql中的#{}替…{}时，就是把${}替换成变量的值。
使用#{}可以有效的防止SQL注入，提高系统安全性。

39 JDBC 与数据库交互的流程是什么?
加载数据库驱动
获取数据库连接
创建statement 对象
设置SQL语句
设置SQL语句参数
使用Sstatement对象执行SQL语句
获取结果集 解析结果集
关闭资源

40 谈谈对mybatis中的sqlSession、sqlSessionFactoryBuild和sqlSessionFactory的理解。
sqlSession:封装了对数据 增删改查的方法
sqlSession是通过sqlSessionFactory创建的
.sqlSessionFactory是通过sqlSessionFactoryBuild创建的

sqlSessionFactoryBuild 是创建sqlSessionFactory时使用的.一旦创建成功后就不需要sqlSessionFactoryBuild的,因为sqlSession是通过sqlSessionFactory创建的,可以可以当做工具类使用

sqlSessionFactory是一个接口, 类里重载了opensession的不同的方法使用范围是在整个运行范围内,一旦创建可以重复使用.可以当做单实例对象来管理

sqlSession是面向用户的一个操作数据库的接口 每个线程都应该有自己的sqlSession 并且sqlSession不可以共享. 线程是不安全的,打开一个sqlSession用完之后就要关闭

41 谈下对mybatis中Sql片段的理解
使用sql标签 属性 id 作为SQL标签的唯一标识
可以把条件和查询结果的字段抽取出来
引用的时候 使用include标签引用
注意：如果引用其它mapper.xml的sql片段，则在引用时需要加上namespace，如下：
<include refid="namespace.sql片段”/>

42 通常一个xml映射文件，都会写一个Dao接口与之对应，请问这个Dao接口的工作原理是什么？Dao接口里的方法，参数不同时，方法可以重载吗？为啥？
Dao接口，就是人们常说的Mapper接口，接口的全限名，就是映射文件中的namespace的值，接口的方法名，就是映射文件中MappedStatement的id值，接口方法内的参数，就是传递给sql的参数。Mapper接口是没有实现类的，当调用接口方法时，接口全限名+方法名拼接字符串作为key值，可唯一定位一个MappedStatement，举例：com.mybatis3.mappers.StudentDao.findStudentById，可以唯一找到namespace为com.mybatis3.mappers.StudentDao下面id = findStudentById的MappedStatement。在Mybatis中，每一个、、、标签，都会被解析为一个MappedStatement对象。

Dao接口里的方法，是不能重载的，因为是全限名+方法名的保存和寻找策略。

Dao接口的工作原理是JDK动态代理，Mybatis运行时会使用JDK动态代理为Dao接口生成代理proxy对象，代理对象proxy会拦截接口方法，转而执行MappedStatement所代表的sql，然后将sql执行结果返回。

43 mybatis是如何进行分页的？分页插件的原理是什么？
Mybatis使用RowBounds对象进行分页，它是针对ResultSet结果集执行的内存分页，而非物理分页，可以在sql内直接书写带有物理分页的参数来完成物理分页功能，也可以使用分页插件来完成物理分页。

分页插件的基本原理是使用Mybatis提供的插件接口，实现自定义插件，在插件的拦截方法内拦截待执行的sql，然后重写sql，根据dialect方言，添加对应的物理分页语句和物理分页参数。

44.Mybatis是如何将sql执行结果封装为目标对象并返回的？都有哪些映射形式？
第一种是使用标签，逐一定义列名和对象属性名之间的映射关系。第二种是使用sql列的别名功能，将列别名书写为对象属性名，比如T_NAME AS NAME，对象属性名一般是name，小写，但是列名不区分大小写，Mybatis会忽略列名大小写，智能找到与之对应对象属性名，你甚至可以写成T_NAME AS NaMe，Mybatis一样可以正常工作。

有了列名与属性名的映射关系后，Mybatis通过反射创建对象，同时使用反射给对象的属性逐一赋值并返回，那些找不到映射关系的属性，是无法完成赋值的。

45. Xml映射文件中，除了常见的select|insert|update|delete标签之外，还有哪些标签？
    还有很多其他的标签，加上动态sql的9个标签，trim|where|set|foreach|if|choose|when|otherwise|bind等，其中为sql片段标签，通过标签引入sql片段，为不支持自增的主键生成策略标签。

46. 简述Mybatis的插件运行原理，以及如何编写一个插件
    Mybatis仅可以编写针对ParameterHandler、ResultSetHandler、StatementHandler、Executor这4种接口的插件，Mybatis使用JDK的动态代理，为需要拦截的接口生成代理对象以实现接口方法拦截功能，每当执行这4种接口对象的方法时，就会进入拦截方法，具体就是InvocationHandler的invoke()方法，当然，只会拦截那些你指定需要拦截的方法。实现Mybatis的Interceptor接口并复写intercept()方法，然后在给插件编写注解，指定要拦截哪一个接口的哪些方法即可，记住，还需要在配置文件中配置你编写的插件。

47. 简述Mybatis一级、二级缓存
    1）一级缓存: 基于 PerpetualCache 的 HashMap 本地缓存，其存储作用域为 Session，当 Session flush 或 close 之后，该 Session 中的所有 Cache 就将清空。

2）二级缓存与一级缓存其机制相同，默认也是采用 PerpetualCache，HashMap 存储，不同在于其存储作用域为 Mapper(Namespace)，并且可自定义存储源，如 Ehcache。要开启二级缓存，你需要在你的 SQL 映射文件中添加一行：

3）对于缓存数据更新机制，当某一个作用域(一级缓存 Session/二级缓存Namespaces)的进行了C/U/D 操作后，默认该作用域下所有 select 中的缓存将被 clear。

48. Mybatis是否支持延迟加载？如果支持，它的实现原理是什么？
    Mybatis仅支持association关联对象和collection关联集合对象的延迟加载，association指的就是一对一，collection指的就是一对多查询。在Mybatis配置文件中，可以配置是否启用延迟加载lazyLoadingEnabled=true|false。

它的原理是，使用CGLIB创建目标对象的代理对象，当调用目标方法时，进入拦截器方法，比如调用a.getB().getName()，拦截器invoke()方法发现a.getB()是null值，那么就会单独发送事先保存好的查询关联B对象的sql，把B查询上来，然后调用a.setB(b)，于是a的对象b属性就有值了，接着完成a.getB().getName()方法的调用。这就是延迟加载的基本原理。

49. Mybatis映射文件中，如果A标签通过include引用了B标签的内容，请问，B标签能否定义在A标签的后面，还是说必须定义在A标签的前面？
    虽然Mybatis解析Xml映射文件是按照顺序解析的，但是，被引用的B标签依然可以定义在任何地方，Mybatis都可以正确识别。

原理是，Mybatis解析A标签，发现A标签引用了B标签，但是B标签尚未解析到，尚不存在，此时，Mybatis会将A标签标记为未解析状态，然后继续解析余下的标签，包含B标签，待所有标签解析完毕，Mybatis会重新解析那些被标记为未解析的标签，此时再解析A标签时，B标签已经存在，A标签也就可以正常解析完成了。

50. 简述Mybatis的Xml映射文件和Mybatis内部数据结构之间的映射关系？
    Mybatis将所有Xml配置信息都封装到All-In-One重量级对象Configuration内部。在Xml映射文件中，标签会被解析为ParameterMap对象，其每个子元素会被解析为ParameterMapping对象。标签会被解析为ResultMap对象，其每个子元素会被解析为ResultMapping对象。每一个、、、标签均会被解析为MappedStatement对象，标签内的sql会被解析为BoundSql对象。