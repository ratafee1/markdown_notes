# [Java 动态代理 两种实现方法](https://www.cnblogs.com/socketqiang/p/11212029.html)







**AOP的拦截功能是由java中的动态代理来实现的。说白了，就是在目标类的基础上增加切面逻辑，生成增强的目标类（该切面逻辑或者在目标类函数执行之前，或者目标类函数执行之后，或者在目标类函数抛出异常时候执行。不同的切入时机对应不同的Interceptor的种类，如BeforeAdviseInterceptor，AfterAdviseInterceptor以及ThrowsAdviseInterceptor等）。那么动态代理是如何实现将切面逻辑（advise）织入到目标类方法中去的呢？下面我们就来详细介绍并实现AOP中用到的两种动态代理。AOP的源码中用到了两种动态代理来实现拦截切入功能：jdk动态代理和cglib动态代理。两种方法同时存在，各有优劣。jdk动态代理是由java内部的反射机制来实现的，cglib动态代理底层则是借助asm来实现的。总的来说，反射机制在生成类的过程中比较高效，而asm在生成类之后的相关执行过程中比较高效（可以通过将asm生成的类进行缓存，这样解决asm生成类过程低效问题）。还有一点必须注意：jdk动态代理的应用前提，必须是目标类基于统一的接口。如果没有上述前提，jdk动态代理不能应用。由此可以看出，jdk动态代理有一定的局限性，cglib这种第三方类库实现的动态代理应用更加广泛，且在效率上更有优势。**







**1.定义接口和实现接口**

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
package com.xiaoqiang.design;

public interface Person {

      public void buy();

    public void buy1();
}
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
package com.xiaoqiang.design;

public class xiaoQiang implements  Person {
    private String name;
    private String house;

    public xiaoQiang(String name, String house) {
        this.name = name;
        this.house = house;
    }

    @Override
    public void buy() {
        System.out.println(name+"买了"+house);
    }

    @Override
    public void buy1() {
        System.out.println("我是你爸爸");
    }
}
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

​         **2.jdk动态代理的实现**

**jdk动态代理是jdk原生就支持的一种代理方式，它的实现原理，就是通过让target类和代理类实现同一接口，代理类持有target对象，来达到方法拦截的作用，这样通过接口的方式有两个弊端，一个是必须保证target类有接口，第二个是如果想要对target类的方法进行代理拦截，那么就要保证这些方法都要在接口中声明，实现上略微有点限制。**

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
package com.xiaoqiang.design;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;

public class ProxySaler implements InvocationHandler {

    public Person person;

    public Object newInstall(Person person)
    {
        this.person=person;
        return  Proxy.newProxyInstance(person.getClass().getClassLoader(),person.getClass().getInterfaces(),this);
    }
    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        System.out.println("执行方法前的操作");
        if(method.getName().equals("buy")) {
            person.buy();
        }
        if(method.getName().equals("buy1"))
        {
            person.buy1();
        }
        System.out.println("执行方法后的操作");
        return null;
    }
}
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

​           **3.运行类**

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
package com.xiaoqiang.design;

import sun.misc.ProxyGenerator;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Proxy;

public class TestMain {

    public static void main(String[] args) {
        ProxySaler proxySaler=new ProxySaler();
        Person object= (Person) proxySaler.newInstall(new xiaoQiang("黄豪强","南山区"));
        object.buy1();
        object.buy();




       /* byte[] bytes=ProxyGenerator.generateProxyClass("$Proxy0",new Class[]{object.getClass()});
        try {
            OutputStream outputStream=new FileOutputStream("$abc.txt");
            outputStream.write(bytes);
            outputStream.flush();
            outputStream.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }*/
        /* System.out.println(aa);*/
      /*try{
          System.out.println(object.getClass().getMethod("buy",Person.class));
      }
      catch (Exception e)
      {
          System.out.println("异常");
      }*/
    /*    object.buy1();*/
    }
}
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

​        **Cglib方法的动态代理：**

​        **需要导入Cglib的jar包：**

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.xiaoqiang</groupId>
    <artifactId>cglibproxy</artifactId>
    <version>1.0-SNAPSHOT</version>

    <dependencies>
        <!-- https://mvnrepository.com/artifact/cglib/cglib -->
        <dependency>
            <groupId>cglib</groupId>
            <artifactId>cglib</artifactId>
            <version>3.2.12</version>
        </dependency>

    </dependencies>

</project>
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 

​        **1.定义被代理的方法:**

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
/**
 * @author 黄豪强
 * @create 2019/7/24 8:51
 */
public class PlayGame {

    public void play()
    {
        System.out.println("打篮球很厉害");
    }
}
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

​         **2.代理类**

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
import net.sf.cglib.proxy.Callback;
import net.sf.cglib.proxy.Enhancer;
import net.sf.cglib.proxy.MethodInterceptor;
import net.sf.cglib.proxy.MethodProxy;

import java.lang.reflect.Method;

/**
 * @author 黄豪强
 * @create 2019/7/24 8:51
 */
public class CglibProxy implements MethodInterceptor {

    public Object newInstall(Object object) {

        return Enhancer.create(object.getClass(), this);
    }


    public Object intercept(Object o, Method method, Object[] objects, MethodProxy methodProxy) throws Throwable {
        System.out.println("先热身一会");
        methodProxy.invokeSuper(o,objects);
        System.out.println("打完了");
        return null;
    }


}
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

​          **3.运行类**

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
/**
 * @author 黄豪强
 * @create 2019/7/24 9:09
 */
public class ProxyTeest {
    public static void main(String[] args) {
           CglibProxy cglibProxy=new CglibProxy();
            PlayGame playGame= (PlayGame) cglibProxy.newInstall(new PlayGame());
            playGame.play();
    }
}
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

​          4.运行结果



![img](https://img2018.cnblogs.com/blog/1453517/201907/1453517-20190724092929640-49392774.png)















