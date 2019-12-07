# uml类图中的几种关系总结



**UML类图**，描写叙述对象和类之间相互关系的方式包含：依赖（Dependency）、关联（Association）、聚合（Aggregation）、组合（Composition）、泛化（Generalization）、实现（Realization）等。

## 依赖（Dependency）

**A依赖B,表示A会使用B的行为或属性，但B不能使用A的行为、属性，那么A和B的关系是依赖关系。**

**uml中用**带箭头的虚线**表示Dependency关系，箭头指向被依赖元素。**





![img](http://img.blog.csdn.net/20140425105730437?%3C/p%3E%3Cp%3Ewatermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvYmJveWZlaXl1/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

演示样例代码 : 



```
class B {
	public void doSth() {
		System.out.println("do sth in class b.");
	}
}

//
class A {
	public void doSthInA(B b) {
		b.doSth();
		// others
	}
}
```

## 泛化（Generalization）

**就是通常所说的继承关系，不必多解释了。uml中用带**空心箭头的实线线表示Generalization关系，箭头指向被继承的类。

  



![img](http://img.blog.csdn.net/20140429172620078?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvYmJveWZlaXl1/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

![img](https://www.cnblogs.com/claireyuancy/p/6962240.html)

![img](https://www.cnblogs.com/claireyuancy/p/6962240.html)



```
// 形状
class Shape {
	
}

// 方形继承自Shape
class Square extends Shape{
	
}
```

## 实现（Realize）

**A定义一个约定，B实现这个约定，则B和A的关系是实现，B实现A。这个关系最经常使用于接口。因此A代表接口，**

**B代表实现接口A的详细类。uml中用**空心箭头和虚线表示Realize关系。箭头指向定义约定(A)的元素。

![img](http://img.blog.csdn.net/20140429172646281?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvYmJveWZlaXl1/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

![img](https://www.cnblogs.com/claireyuancy/p/6962240.html)

![img](https://www.cnblogs.com/claireyuancy/p/6962240.html)

演示样例代码  :



```
public interface Runnable {
    public abstract void run();
}

// 实现Runnable接口
public class Thread implements Runnable {
        @Override
    public void run() {
        // do sth
    }
}
```

## 关联（Association）

**元素间的结构化关系，是一种弱关系，被关联的元素间通常能够独立存在。uml中用**实线（单向关联带箭头）

表示Association关系。箭头指向被依赖元素。







![img](https://www.cnblogs.com/claireyuancy/p/6962240.html)

![img](http://img.blog.csdn.net/20140429172713921?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvYmJveWZlaXl1/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

![img](https://www.cnblogs.com/claireyuancy/p/6962240.html)



   每一个人都能够有书籍。可是书籍与人之间并不存在强关系，两者能够各自独立。





演示样例代码 : 





```
class Book {
	
}

// 
class People {
	// 学生能够独立于老师而存在
	List<Book> mBooks = new ArrayList<Book>();
}
```

## 聚合（Aggregation）

**聚合是关联关系的一种特例，是强的关联关系；关联和聚会在语义上无法区分，仅仅能依据考察详细的逻辑来加以区分。**

**聚合关系表示部分和总体的关系** 

(  关联仅仅是表示单纯的依赖 )

，部分能够独立于总体而存在。



UML中用带空心菱形头的实线

表示Aggregation关系，

菱形头指向总体

。







![img](https://www.cnblogs.com/claireyuancy/p/6962240.html)

![img](https://www.cnblogs.com/claireyuancy/p/6962240.html)

![img](http://img.blog.csdn.net/20140429172737343?%3C/p%3E%3Cp%3Ewatermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvYmJveWZlaXl1/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

​    车轮属于车的一部分。但车轮能够独立于车存在。





代码演示样例 :



```
class Wheel {
}

class Car {
	List<Wheel> mWheels = new ArrayList<Wheel>();
}
```

## 组合（Composition）

组合是聚合关系的变种，表示元两者之间具有更强的聚合关系，它通常要求总体代表部分的生命周期。



假设是组合关系，部分(个体)不能独立于总体而存在。

UML中用带实心菱形头的实线表示Composition关系。

菱形头指向总体。





![img](https://www.cnblogs.com/claireyuancy/p/6962240.html)

![img](https://www.cnblogs.com/claireyuancy/p/6962240.html)

   ![img](http://img.blog.csdn.net/20140429172841546?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvYmJveWZlaXl1/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

   手是人体的一部分，可是手不能独立于人体而存在。



```
class Hand {

}

class People {
	List<Hand> mHands = new ArrayList<Hand>();
}
```

​    当中依赖（Dependency）的关系最弱，而关联（Association）。聚合（Aggregation），组合（Composition）表示的关系依次增强。换言之关联，聚合，组合都是依赖关系的一种，聚合是表明对象之间的总体与部分关系的关联。而组合是表明总体与部分之间有同样生命周期关系的聚合。



**各种关系的强弱顺序：**

​        泛化 = 实现 > 组合 > 聚合 > 关联 > 依赖 