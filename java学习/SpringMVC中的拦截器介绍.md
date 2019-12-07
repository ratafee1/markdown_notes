# SpringMVC中的拦截器介绍



    SpringMvc中的拦截器：
    
        SpringMvc拦截器帮我们按照一定规则拦截请求，后根据开发人员自定义的拦截逻辑进行处理；
    
        自定义拦截器需要实现HandlerInterceptor接口；
    
        自定义的拦截器实现类需要在SpringMvc配置文件中配置；
    
        可以配置多个拦截器，配置的顺序会影响到拦截器的执行顺序，配置在前的先执行；
    
        HandlerInterceptor有3个方法：
    
            preHandle 预处理：在拦截方法前执行；
    
            postHandle 后处理：在拦截方法后执行；
    
            afterCompletion 渲染后处理：在页面渲染后执行；
    
        拦截器也体现了AOP思想；
    
        拦截器的应用：权限检查，日志记录，性能检测等；
    
    拦截器的执行流程图：

![img](https://img-blog.csdnimg.cn/20190701162842270.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQwMzIzMjU2,size_16,color_FFFFFF,t_70)

 



总结的几条拦截器规则：

1.preHandle 预处理：根据拦截器定义的顺序，正向执行

2.postHandle 后处理：根据拦截器定义的顺序，逆向执行。需要所有的preHandle都返回true时才会调用

3.afterCompletion 渲染后处理：根据拦截器定义的顺序，逆向执行。preHandle返回true就会调用

![img](https://img-blog.csdnimg.cn/20190506095935117.png)



MyInterceptor1.java:

    public class MyInterceptor1 implements HandlerInterceptor {
     
    	@Override
    	public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler)
    			throws Exception {
    		System.out.println("1 PreHandle预处理");
    		return true;
    	}
     
    	@Override
    	public void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler,
    			ModelAndView modelAndView) throws Exception {
    		System.out.println("1 postHandle后处理");
    	}


​     
    	@Override
    	public void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex)
    			throws Exception {
    		System.out.println("1 afterCompletion页面渲染后处理");
    	}
    	
    }

MyInterceptor2.java:

    public class MyInterceptor2 implements HandlerInterceptor {
     
    	@Override
    	public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler)
    			throws Exception {
    		System.out.println("2 PreHandle预处理");
    		return true;
    	}
     
    	@Override
    	public void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler,
    			ModelAndView modelAndView) throws Exception {
    		System.out.println("2 postHandle后处理");
    	}


​     
    	@Override
    	public void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex)
    			throws Exception {
    		System.out.println("2 afterCompletion页面渲染后处理");
    	}
    	
    }

applicationContext.xml:

    		<mvc:interceptors>
    <!-- 			拦截器1 -->
    			<mvc:interceptor>
    				<mvc:mapping path="/**"/>
    				<bean class="com.sikiedu.interceptor.MyInterceptor1"></bean>
    			</mvc:interceptor>
    			
    			<!-- 			拦截器2 -->
    			<mvc:interceptor>
    				<mvc:mapping path="/**"/>
    				<bean class="com.sikiedu.interceptor.MyInterceptor2"></bean>
    			</mvc:interceptor>
    		</mvc:interceptors>
    
    preHandle1返回true，preHandle2返回true：运行结果如下：
    
    
    preHandle1返回true，preHandle2返回false：运行结果如下：
    
    preHandle1返回false，preHandle2返回true：运行结果如下：

![img](https://img-blog.csdnimg.cn/20190506100852938.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQwMzIzMjU2,size_16,color_FFFFFF,t_70)

![img](https://img-blog.csdnimg.cn/20190506101140171.png)

![img](https://img-blog.csdnimg.cn/20190506101301804.png)





## [springmvc拦截器的简单了解](https://www.cnblogs.com/gongchengshixiaobai/p/8039067.html)  		

1、定义一个拦截器

 

![img](https://images2017.cnblogs.com/blog/1282679/201712/1282679-20171214155412873-974505056.png)

2、在springmvc.xml中配置拦截器。

(1)拦截器拦截的请求是建立在前端控制器配置之下的，若DispatcherServlet拦截的是*.action，则拦截器即使配置  /**，则拦截器拦截的也只是所有 *.action的请求。若DispatcherServlet拦截的是 /，则拦截器配置  /**才是拦截所有资源。

(2)前端控制器可以配置多个，名字不相同即可，配置 *.action是正常的使用，配置 / 是springmvc  restful风格的使用方式，不过当前端控制器有配置 / 时，必须再使用一个 <mvc  resource:>标签对静态资源进行排除，否则springmvc的会将静态资源也会当成 Handler的url去找对应的Handler  ，这样静态资源就无法被正常的访问了。

(3)配置拦截器是针对处理器映射器进行配置的，有如下两种方式

　　方式一：针对某种处理器映射器配置拦截器

　　![img](https://images2017.cnblogs.com/blog/1282679/201712/1282679-20171214161517154-1952697571.png)

　　方式二：针对所有mapping配置全局拦截器：*springmvc中没有全局拦截器概念，使用这种配置，springmvc将配置的拦截器分别注入到多个处理器映射器。同样也需要放行静态资源。*

　　*![img](https://images2017.cnblogs.com/blog/1282679/201712/1282679-20171214162522998-397829095.png)*

 

3、拦截器执行的顺序

![img](https://images2017.cnblogs.com/blog/1282679/201712/1282679-20171214180009638-1214179545.png)

![img](https://images2017.cnblogs.com/blog/1282679/201712/1282679-20171214180056467-824124312.png)

4、如使用springmvc拦截器完成简单的认证操作。