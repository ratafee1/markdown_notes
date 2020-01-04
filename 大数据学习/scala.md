![image-20191216101623309](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191216101623309.png)

![image-20191216101756624](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191216101756624.png)

![image-20191216102201901](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191216102201901.png)



其中
val 定义的是不可重新赋值的变量
var 定义的是可重新赋值的变量



当有一些变量保存的数据较大时，但是不需要马上加载到JVM内存。可以使用惰性赋值来提高效
率。

lazy val/var 变量名 = 表达式



使用双引号

~~~scala
scala> println(name + name.length)
hadoop6
~~~







使用插值表达式

~~~scala
scala> val name = "zhangsan"
name: String = zhangsan
scala> val age = 30
age: Int = 30
scala> val sex = "male"
sex: String = male
scala> val info = s"name=${name}, age=${age}, sex=${sex}"
info: String = name=zhangsan, age=30, sex=male
scala> println(info)
name=zhangsan, age=30, sex=male
~~~



使用三引号

~~~
val sql = """select
| *
| from
| t_user
| where
| name = "zhangsan""""
println(sql)
~~~





注意下 scala类型与Java的区别
[!NOTE]
1. scala中所有的类型都使用大写字母开头
2. 整形使用 Int 而不是Integer
3. scala中定义变量可以不写类型，让scala编译器自动推断





scala中没有，++、--运算符
与Java不一样，在scala中，可以直接使用 == 、 != 进行比较，它们与 equals 方法表示一
致。而比较两个对象的引用值，使用 eq



scala类型层次结构

![image-20191216105806073](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191216105806073.png)

![image-20191216105823832](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191216105823832.png)



有返回值的if
与Java不一样的是，
[!NOTE]
在scala中，条件表达式也是有返回值的
在scala中，没有三元表达式，可以使用if表达式替代三元表达式



~~~
scala> val sex = "male"
sex: String = male
scala> val result = if(sex == "male") 1 else 0
result: Int = 1
~~~



~~~
scala> val a = {
| println("1 + 1")
| 1 + 1
| }


~~~



~~~scala
scala> val nums = 1.to(10)
nums: scala.collection.immutable.Range.Inclusive = Range(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

scala> for(i <- nums) println(i)
~~~



~~~scala
// 中缀调用法
scala> for(i <- 1 to 10) println(i)
~~~



~~~
for(i <- 1 to 3; j <- 1 to 5) {print("*");if(j == 5) println("")}
~~~



~~~
// 添加守卫，打印能够整除3的数字
for(i <- 1 to 10 if i % 3 == 0) println(i)
~~~



~~~
scala> var i = 1
i: Int = 1
scala> while(i <= 10) {
| println(i)
| i = i+1
| }
~~~





~~~
def methodName (参数名:参数类型, 参数名:参数类型) : [return type] = {
// 方法体：一系列的代码
}
~~~

[!NOTE]
参数列表的参数类型不能省略
返回值类型可以省略
返回值可以不写return，默认就是{}块表达式的值



![image-20191216121924054](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191216121924054.png)





~~~scala
import scala.util.control.Breaks._
breakable{for(i <- 1 to 100) if(i >=50) break() else println(i)}
~~~



~~~scala
for(i <- 1 to 100) breakable{
      if(i %10 == 0)break()
      else println(i)
      }
~~~



![image-20191216123729092](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191216123729092.png)



方法参数
scala中的方法参数，使用比较灵活。它支持以下几种类型的参数：
默认参数
带名参数
变长参数



~~~
// x，y带有默认值为0
def add(x:Int = 0, y:Int = 0) = x + y
add()
~~~



带名参数

~~~
def add(x:Int = 0, y:Int = 0) = x + y
add(x=1)
~~~



变长参数

~~~
scala> def add(num:Int*) = num.sum
add: (num: Int*)Int
scala> add(1,2,3,4,5)
res1: Int = 15
~~~





![image-20191216124912208](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191216124912208.png)





方法调用方式
在scala中，有以下几种方法调用方式，
后缀调用法
中缀调用法
花括号调用法
无括号调用法



![image-20191216125707272](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191216125707272.png)



![image-20191216130416768](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191216130416768.png)



花括号调用法
语法
Math.abs{
// 表达式1
// 表达式2
}

方法只有一个参数，才能使用花括号调用法



无括号调用法

如果方法没有参数，可以省略方法名后面的括号

~~~
def m3()=println("hello")
m3()
~~~







# 函数

scala支持函数式编程，将来编写Spark/Flink程序中，会大量使用到函数



## 定义函数

**语法**

```scala
val 函数变量名 = (参数名:参数类型, 参数名:参数类型....) => 函数体
```

Tip

- 函数是一个**对象**（变量）
- 类似于方法，函数也有输入参数和返回值
- 函数定义不需要使用`def`定义
- 无需指定返回值类型

~~~
scala> val add = (x:Int, y:Int) => x + y
add: (Int, Int) => Int = <function2>

scala> add(1,2)
res3: Int = 3
~~~





## 方法和函数的区别

- 方法是隶属于类或者对象的，在运行时，它是加载到JVM的方法区中
- 可以将函数对象赋值给一个变量，在运行时，它是加载到JVM的堆内存中
- 函数是一个对象，继承自FunctionN，函数对象有apply，curried，toString，tupled这些方法。方法则没有



## 方法转换为函数

- 有时候需要将方法转换为函数，作为变量传递，就需要将方法转换为函数
- 使用`_`即可将方法转换为函数

~~~
scala> def add(x:Int,y:Int)=x+y
add: (x: Int, y: Int)Int

scala> val a = add _
a: (Int, Int) => Int = <function2>
~~~





Note



- 在scala中，数组的泛型使用`[]`来指定
- 使用`()`来获取元素





## 定义变长数组

创建变长数组，需要提前导入ArrayBuffer类`import scala.collection.mutable.ArrayBuffer`

```scala
val a = ArrayBuffer[Int]()
```



```scala
scala> val a = ArrayBuffer("hadoop", "storm", "spark")
a: scala.collection.mutable.ArrayBuffer[String] = ArrayBuffer(hadoop, storm, spark)
```

##  添加/修改/删除元素

- 使用`+=`添加元素
- 使用`-=`删除元素
- 使用`++=`追加一个数组到变长数组



~~~scala
// 定义变长数组
scala> val a = ArrayBuffer("hadoop", "spark", "flink")
a: scala.collection.mutable.ArrayBuffer[String] = ArrayBuffer(hadoop, spark, flink)

// 追加一个元素
scala> a += "flume"
res10: a.type = ArrayBuffer(hadoop, spark, flink, flume)

// 删除一个元素
scala> a -= "hadoop"
res11: a.type = ArrayBuffer(spark, flink, flume)

// 追加一个数组
scala> a ++= Array("hive", "sqoop")
res12: a.type = ArrayBuffer(spark, flink, flume, hive, sqoop)

~~~





# 遍历数组

可以使用以下两种方式来遍历数组：

- 使用`for表达式`直接遍历数组中的元素
- 使用`索引`遍历数组中的元素

~~~
scala> val a = Array(1,2,3,4,5)
a: Array[Int] = Array(1, 2, 3, 4, 5)

scala> for(i<-a) println(i)
1
2
3
4
5

~~~



~~~
scala> val a = Array(1,2,3,4,5)
a: Array[Int] = Array(1, 2, 3, 4, 5)

scala> for(i <- 0 to a.length - 1) println(a(i))
1
2
3
4
5

scala> for(i <- 0 until a.length) println(a(i))
1
2
3
4
5

~~~



 Note



0 until n——生成一系列的数字，包含0，不包含n

0 to n ——包含0，也包含n



# 数组常用算法

scala中的数组封装了一些常用的计算操作，将来在对数据处理的时候，不需要我们自己再重新实现。以下为常用的几个算法：

- 求和——sum方法
- 求最大值——max方法
- 求最小值——min方法
- 排序——sorted方法





## 定义元组

**语法**

使用括号来定义元组

```scala
val/var 元组 = (元素1, 元素2, 元素3....)
Copy
```



使用箭头来定义元组（元组只有两个元素）

```scala
val/var 元组 = 元素1->元素2
```





## 访问元组

使用\_1、\_2、\_3....来访问元组中的元素，_1表示访问第一个元素，依次类推







# 列表

列表是scala中最重要的、也是最常用的数据结构。List具备以下性质：

- 可以保存重复的值
- 有先后顺序



在scala中，也有两种列表，一种是不可变列表、另一种是可变列表



**语法**

使用`List(元素1, 元素2, 元素3, ...)`来创建一个不可变列表，语法格式：

```scala
val/var 变量名 = List(元素1, 元素2, 元素3...)
Copy
```



使用`Nil`创建一个不可变的空列表

```scala
val/var 变量名 = Nil
Copy
```



使用`::`方法创建一个不可变列表

```scala
val/var 变量名 = 元素1 :: 元素2 :: Nil
Copy
```



 Tip



使用**::**拼接方式来创建列表，必须在最后添加一个**Nil**







# 可变列表

可变列表就是列表的元素、长度都是可变的。

要使用可变列表，先要导入`import scala.collection.mutable.ListBuffer`





 Note



- 可变集合都在`mutable`包中
- 不可变集合都在`immutable`包中（默认导入）



## 定义

使用ListBuffer[元素类型]()创建空的可变列表，语法结构：

```scala
val/var 变量名 = ListBuffer[Int]()
Copy
```



使用ListBuffer(元素1, 元素2, 元素3...)创建可变列表，语法结构：

```scala
val/var 变量名 = ListBuffer(元素1，元素2，元素3...)
```





## 可变列表操作

- 获取元素（使用括号访问`(索引值)`）
- 添加元素（`+=`）
- 追加一个列表（`++=`）
- 更改元素（`使用括号获取元素，然后进行赋值`）
- 删除元素（`-=`）
- 转换为List（`toList`）
- 转换为Array（`toArray`）



# 列表常用操作

以下是列表常用的操作

- 判断列表是否为空（`isEmpty`）
- 拼接两个列表（`++`）
- 获取列表的首个元素（`head`）和剩余部分(`tail`)
- 反转列表（`reverse`）
- 获取前缀（`take`）、获取后缀（`drop`）
- 扁平化（`flaten`）
- 拉链（`zip`）和拉开（`unzip`）
- 转换字符串（`toString`）
- 生成字符串（`mkString`）
- 并集（`union`）
- 交集（`intersect`）
- 差集（`diff`）





# Set

Set(集)是代表没有重复元素的集合。Set具备以下性质：

1. 元素不重复
2. 不保证插入顺序



scala中的集也分为两种，一种是不可变集，另一种是可变集。





## 不可变集



### 定义

**语法**

创建一个空的不可变集，语法格式：

```scala
val/var 变量名 = Set[类型]()
Copy
```



给定元素来创建一个不可变集，语法格式：

```scala
val/var 变量名 = Set(元素1, 元素2, 元素3...)
```





### 基本操作

- 获取集的大小（`size`）
- 遍历集（`和遍历数组一致`）
- 添加一个元素，生成一个Set（`+`）
- 拼接两个集，生成一个Set（`++`）
- 拼接集和列表，生成一个Set（`++`）





~~~scala
// 创建集
scala> val a = Set(1,1,2,3,4,5)
a: scala.collection.immutable.Set[Int] = Set(5, 1, 2, 3, 4)

// 获取集的大小
scala> a.size
res0: Int = 5

// 遍历集
scala> for(i <- a) println(i)

// 删除一个元素
scala> a - 1
res5: scala.collection.immutable.Set[Int] = Set(5, 2, 3, 4)

// 拼接两个集
scala> a ++ Set(6,7,8)
res2: scala.collection.immutable.Set[Int] = Set(5, 1, 6, 2, 7, 3, 8, 4)

// 拼接集和列表
scala> a ++ List(6,7,8,9)
res6: scala.collection.immutable.Set[Int] = Set(5, 1, 6, 9, 2, 7, 3, 8, 4)

~~~





# 映射

Map可以称之为映射。它是由键值对组成的集合。在scala中，Map也分为不可变Map和可变Map。







## 不可变Map

### 定义

**语法**

```scala
val/var map = Map(键->值, 键->值, 键->值...)    // 推荐，可读性更好
val/var map = Map((键, 值), (键, 值), (键, 值), (键, 值)...)
```



## 可变Map

### 定义

定义语法与不可变Map一致。但定义可变Map需要手动导入`import scala.collection.mutable.Map`



# iterator迭代器

scala针对每一类集合都提供了一个迭代器（iterator）用来迭代访问集合



## 使用迭代器遍历集合

- 使用`iterator`方法可以从集合获取一个迭代器
- 迭代器的两个基本操作
  - hasNext——查询容器中是否有下一个元素
  - next——返回迭代器的下一个元素，如果没有，抛出NoSuchElementException
- 每一个迭代器都是有状态的
  - 迭代完后保留在最后一个元素的位置
  - 再次使用则抛出NoSuchElementException
- 可以使用while或者for来逐个返回元素





# 函数式编程

我们将来使用Spark/Flink的大量业务代码都会使用到函数式编程。下面的这些操作是学习的重点。

- 遍历（`foreach`）
- 映射（`map`）
- 映射扁平化（`flatmap`）
- 过滤（`filter`）
- 是否存在（`exists`）
- 排序（`sorted`、`sortBy`、`sortWith`）
- 分组（`groupBy`）
- 聚合计算（`reduce`）
- 折叠（`fold`）





## 遍历 | foreach

之前，学习过了使用for表达式来遍历集合。我们接下来将学习scala的函数式编程，使用`foreach`方法来进行遍历、迭代。它可以让代码更加简洁。

## 使用下划线来简化函数定义

当函数参数，只在函数体中出现一次，而且函数体没有嵌套调用时，可以使用下划线来简化函数定义

- 如果方法参数是函数，如果出现了下划线，scala编译器会自动将代码封装到一个函数中
- 参数列表也是由scala编译器自动处理



# 映射 | map

集合的映射操作是将来在编写Spark/Flink用得最多的操作，是我们必须要掌握的。因为进行数据计算的时候，就是一个将一种数据类型转换为另外一种数据类型的过程。



map方法接收一个函数，将这个函数应用到每一个元素，返回一个新的列表





# 扁平化映射 | flatMap

扁平化映射也是将来用得非常多的操作，也是必须要掌握的。

## 定义

可以把flatMap，理解为先map，然后再flatten



# 过滤 | filter

过滤符合一定条件的元素



# 排序

在scala集合中，可以使用以下几种方式来进行排序

- sorted默认排序
- sortBy指定字段排序
- sortWith自定义排序



# 分组 | groupBy

。我们如果要将数据按照分组来进行统计分析，就需要使用到分组方法

~~~scala
scala> val a = List("张三"->"男", "李四"->"女", "王五"->"男")
a: List[(String, String)] = List((张三,男), (李四,女), (王五,男))

// 按照性别分组
scala> a.groupBy(_._2)
res0: scala.collection.immutable.Map[String,List[(String, String)]] = Map(男 -> List((张三,男), (王五,男)),
女 -> List((李四,女)))

// 将分组后的映射转换为性别/人数元组列表
scala> res0.map(x => x._1 -> x._2.size)
res3: scala.collection.immutable.Map[String,Int] = Map(男 -> 2, 女 -> 1)

~~~



# 聚合操作

聚合操作，可以将一个列表中的数据合并为一个。这种操作经常用来统计分析中



## 聚合 | reduce

reduce表示将列表，传入一个函数进行聚合计算



## 折叠 | fold

fold与reduce很像，但是多了一个指定初始值参数







# scala第二天

**学习目标**

- 掌握scala类与object的用法
- 掌握继承的用法
- 掌握trait（特质）的用法



![image-20191216204241410](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191216204241410.png)



![image-20191216204723794](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191216204723794.png)



![image-20191216205310760](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191216205310760.png)



## 定义

Java中的访问控制，同样适用于scala，可以在成员前面添加private/protected关键字来控制成员的可见性。但在scala中，**`没有public关键字`**，任何没有被标为private或protected的成员都是公共的



![image-20191216212122107](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191216212122107.png)



![image-20191216213218082](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191216213218082.png)



## 定义伴生对象

一个class和object具有同样的名字。这个object称为**伴生对象**，这个class称为**伴生类**

- 伴生对象必须要和伴生类一样的名字
- 伴生对象和伴生类在同一个scala源文件中
- 伴生对象和伴生类可以互相访问private属性





## 定义

**定义apply方法**

```scala
object 伴生对象名 {
    def apply(参数名:参数类型, 参数名:参数类型...) = new 类(...)
}

```

**创建对象**

```scala
伴生对象名(参数1, 参数2...)
```





## 定义语法

- scala和Java一样，使用**extends**关键字来实现继承
- 可以在子类中定义父类中没有的字段和方法，或者重写父类的方法
- 类和单例对象都可以从某个父类继承

**语法**

```scala
class/object 子类 extends 父类 {
    ..
}
```







~~~
class Person {
  val name = "super"

  def getName = name
}

class Student extends Person {
  // 重写val字段
  override val name: String = "child"

  // 重写getName方法
  override def getName: String = "hello, " + super.getName
}

object Main13 {
  def main(args: Array[String]): Unit = {
    println(new Student().getName)
  }
}

~~~





scala中对象提供isInstanceOf和asInstanceOf方法。

- isInstanceOf判断对象是否为指定类的对象
- asInstanceOf将对象转换为指定类型





# getClass和classOf

isInstanceOf 只能判断对象是否为**指定类以及其子类**的对象，而不能精确的判断出，对象就是指定类的对象。如果要求精确地判断出对象就是指定类的对象，那么就只能使用 getClass 和 classOf 。

## 用法

- p.getClass可以精确获取对象的类型
- classOf[x]可以精确获取类型
- 使用==操作符可以直接比较类型





# 抽象类

和Java语言一样，scala中也可以定义抽象类

## 定义

如果类的某个成员在当前类中的定义是不包含完整的，它就是一个**抽象类**

不完整定义有两种情况：

1. 方法没有方法体（**抽象方法**）
2. 变量没有初始化（**抽象字段**）





# 抽象字段

在scala中，也可以定义抽象的字段。如果一个成员变量是没有初始化，我们就认为它是抽象的。

## 定义

**语法**

```scala
abstract class 抽象类 {
    val/var 抽象字段:类型
}
```





# 匿名内部类

匿名内部类是没有名称的子类，直接用来创建实例对象。Spark的源代码中有大量使用到匿名内部类。

scala中的匿名内部类使用与Java一致。

## 定义

**语法**

```scala
val/var 变量名 = new 类/抽象类 {
    // 重写方法
}
```



# 特质(trait)

scala中没有Java中的接口（interface），替代的概念是——特质

## 定义

- 特质是scala中代码复用的基础单元
- 它可以将方法和字段定义封装起来，然后添加到类中
- 与类继承不一样的是，类继承要求每个类都只能继承`一个`超类，而一个类可以添加`任意数量`的特质。
- 特质的定义和抽象类的定义很像，但它是使用`trait`关键字



# 特质 | 定义具体的方法

和类一样，trait中还可以定义具体的方法

## 示例

**示例说明**

1. 定义一个Logger特质，添加log实现方法
2. 定义一个UserService类，实现Logger特质
   - 添加add方法，打印"添加用户"
3. 添加main方法
   - 创建UserService对象实例
   - 调用add方法



# trait中定义具体的字段和抽象的字段

## 定义

- 在trait中可以定义具体字段和抽象字段
- 继承trait的子类自动拥有trait中定义的字段
- 字段直接被添加到子类中





# 使用trait实现模板模式

要实现以下需求：

- 实现一个输出日志的功能
- 目前要求输出到控制台
- 将来可能会输出到文件、输出到Redis、或者更多的需求

如何实现将来不修改之前的代码，来扩展现有功能呢？

![image-20191217020418436](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191217020418436.png)





# 对象混入trait

scala中可以将trait混入到对象中，就是将trait中定义的方法、字段添加到一个对象中



# trait实现调用链模式

我们如果要开发一个支付功能，往往需要执行一系列的验证才能完成支付。例如：

1. 进行支付签名校验
2. 数据合法性校验
3. ...

如果将来因为第三方接口支付的调整，需要增加更多的校验规则，此时如何不修改之前的校验代码，来实现扩展呢？





# trait的构造机制

如果一个类实现了多个trait，那这些trait是如何构造的呢？

## 定义

- trait也有构造代码，但和类不一样，特质不能有构造器参数
- 每个特质只有**`一个无参数`**的构造器。
- 一个类继承另一个类、以及多个trait，当创建该类的实例时，它的构造顺序如下：
  1. 执行父类的构造器
  2. `从左到右`依次执行trait的构造器
  3. 如果trait有父trait，先构造父trait，如果多个trait有同样的父trait，则只初始化一次
  4. 执行子类构造器





#  trait继承class

## 定义

trait也可以继承class的。特质会将class中的成员都继承下来。





# 样例类

样例类是一种特殊类，它可以用来快速定义一个用于**保存数据**的类（类似于Java POJO类），在后续要学习并发编程和spark、flink这些框架也都会经常使用它。

## 定义样例类

**语法格式**

```scala
case class 样例类名([var/val] 成员变量名1:类型1, 成员变量名2:类型2, 成员变量名3:类型3)
Copy
```

- 如果要实现某个成员变量可以被修改，可以添加var
- 默认为val，可以省略



# 样例类的方法

当我们定义一个样例类，编译器自动帮助我们实现了以下几个有用的方法：

- apply方法
- toString方法
- equals方法
- hashCode方法
- copy方法



# 样例对象

它主要用在两个地方：

1. 定义枚举
2. 作为没有任何参数的消息传递（后面Akka编程会讲到）





## 定义

使用case object可以创建样例对象。样例对象是单例的，而且它**没有主构造器**

**语法格式**

```scala
case object 样例对象名
```





# 模式匹配

scala中有一个非常强大的模式匹配机制，可以应用在很多场景：

- switch语句
- 类型查询
- 使用模式匹配快速获取数据

## 简单模式匹配

在Java中，有switch关键字，可以简化if条件判断语句。在scala中，可以使用match表达式替代。

~~~
println("请输出一个词：")
// StdIn.readLine表示从控制台读取一行文本
val name = StdIn.readLine()

val result = name match {
    case "hadoop" => "大数据分布式存储和计算框架"
    case "zookeeper" => "大数据分布式协调服务框架"
    case "spark" => "大数据分布式内存计算框架"
    case _ => "未匹配"
}

println(result)

~~~



# 匹配类型

除了像Java中的switch匹配数据之外，match表达式还可以进行类型匹配。如果我们要根据不同的数据类型，来执行不同的逻辑，也可以使用match表达式来实现。



 Note

如果case表达式中无需使用到匹配到的变量，可以使用下划线代代替

~~~
val a:Any = "hadoop"

val result = a match {
    case _:String => "String"
    case _:Int => "Int"
    case _:Double => "Double"
}

println(result)

~~~

 

# 守卫

在scala中，可以使用守卫来简化上述代码——也就是在**case语句中添加if条件判断**。



~~~
val a = StdIn.readInt()

a match {
    case _ if a >= 0 && a <= 3 => println("[0-3]")
    case _ if a >= 4 && a <= 8 => println("[3-8]")
    case _ => println("未匹配")
}

~~~



# 匹配样例类

scala可以使用模式匹配来匹配样例类，从而可以快速获取样例类中的成员数据。后续，我们在开发Akka案例时，还会用到。

~~~
// 1. 创建两个样例类
case class Person(name:String, age:Int)
case class Order(id:String)

def main(args: Array[String]): Unit = {
    // 2. 创建样例类对象，并赋值为Any类型
    val zhangsan:Any = Person("张三", 20)
    val order1:Any = Order("001")

    // 3. 使用match...case表达式来进行模式匹配
    // 获取样例类中成员变量
    order1 match {
        case Person(name, age) => println(s"姓名：${name} 年龄：${age}")
        case Order(id1) => println(s"ID为：${id1}")
        case _ => println("未匹配")
    }
}

~~~





# 匹配集合

scala中的模式匹配，还能用来匹配集合。



## 匹配数组

~~~
val arr = Array(1, 3, 5)
arr match {
    case Array(1, x, y) => println(x + " " + y)
    case Array(0) => println("only 0")
    case Array(0, _*) => println("0 ...")
    case _ => println("something else")
}

~~~



## 匹配列表

~~~
val list = List(0, 1, 2)

list match {
    case 0 :: Nil => println("只有0的列表")
    case 0 :: tail => println("0开头的列表")
    case x :: y :: Nil => println(s"只有另两个元素${x}, ${y}的列表")
    case _ => println("未匹配")
}

~~~



## 匹配元组

~~~
val tuple = (2, 2, 5)

tuple match {
    case (1, x, y) => println(s"三个元素，1开头的元组：1, ${x}, ${y}")
    case (x, y, 5) => println(s"三个元素，5结尾的元组：${x}, ${y}, 5")
    case _ => println("未匹配")
}

~~~





# 变量声明中的模式匹配

在定义变量的时候，可以使用模式匹配快速获取数据



## 示例 | 获取数组中的元素

## 示例 | 获取List中的数据



# Option类型

使用Option类型，可以用来有效避免空引用(null)异常。也就是说，将来我们返回某些数据时，可以返回一个Option类型来替代。



![image-20191217151640347](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191217151640347.png)



# 偏函数

偏函数可以提供了简洁的语法，可以简化函数的定义。配合集合的函数式编程，可以让代码更加优雅。

## 定义

- 偏函数被包在花括号内没有match的一组case语句是一个偏函数
- 偏函数是PartialFunction[A, B]的一个实例
  - A代表输入参数类型
  - B代表返回结果类型



# 正则表达式

在scala中，可以很方便地使用正则表达式来匹配数据。



## 定义

**Regex类**

- scala中提供了Regex类来定义正则表达式

- 要构造一个RegEx对象，直接使用String类的r方法即可

- 建议使用三个双引号来表示正则表达式，不然就得对正则中的反斜杠来进行转义

  ```scala
    val regEx = """正则表达式""".r
  Copy
  ```



**findAllMatchIn方法**

- 使用findAllMatchIn方法可以获取到所有正则匹配到的字符串





## 捕获异常

**语法格式**

```scala
try {
    // 代码
}
catch {
    case ex:异常类型1 => // 代码
    case ex:异常类型2 => // 代码
}
finally {
    // 代码
}
Copy
```

- try中的代码是我们编写的业务处理代码
- 在catch中表示当出现某个异常时，需要执行的代码
- 在finally中，是不管是否出现异常都会执行的代码



# 抛出异常

我们也可以在一个方法中，抛出异常。语法格式和Java类似，使用`throw new Exception...`



scala不需要在方法上声明要抛出的异常，它已经解决了再Java中被认为是设计失败的检查型异常。





# 提取器(Extractor)

那是不是所有的类都可以进行这样的模式匹配呢？答案是：

`不可以`的。要支持模式匹配，必须要实现一个**提取器**。



 Note



样例类自动实现了apply、unapply方法









# 协变、逆变、非变

spark的源代码中大量使用到了协变、逆变、非变，学习该知识点对我们将来阅读spark源代码很有帮助。



来看一个类型转换的问题：

```scala
class Pair[T]

object Pair {
  def main(args: Array[String]): Unit = {
    val p1 = Pair("hello")
    // 编译报错，无法将p1转换为p2
    val p2:Pair[AnyRef] = p1

    println(p2)
  }
}
Copy
```

如何让带有泛型的类支持类型转换呢？





## 非变

**语法格式**

```scala
class Pair[T]{}
Copy
```

- 默认泛型类是非变的
- 类型B是A的子类型，Pair[A]和Pair[B]没有任何从属关系
- Java是一样的

[![1558064807949](assets/1558064807949.png)](assets/1558064807949.png)





## 协变

**语法格式**

```scala
class Pair[+T]
Copy
```

- 类型B是A的子类型，Pair[B]可以认为是Pair[A]的子类型
- 参数化类型的方向和类型的方向是一致的。





## 逆变

**语法格式**

```scala
class Pair[-T]
Copy
```

- 类型B是A的子类型，Pair[A]反过来可以认为是Pair[B]的子类型
- 参数化类型的方向和类型的方向是相反的





## 示例

**示例说明**

- 定义一个Super类、以及一个Sub类继承自Super类
- 使用协变、逆变、非变分别定义三个泛型类
- 分别创建泛型类来演示协变、逆变、非变

**参考代码**

```scala
class Super
class Sub extends Super

class Temp1[T]
class Temp2[+T]
class Temp3[-T]

def main(args: Array[String]): Unit = {
    val a:Temp1[Sub] = new Temp1[Sub]
    // 编译报错
    // 非变
    //val b:Temp1[Super] = a

    // 协变
    val c: Temp2[Sub] = new Temp2[Sub]
    val d: Temp2[Super] = c

    // 逆变
    val e: Temp3[Super] = new Temp3[Super]
    val f: Temp3[Sub] = e
}
```







# Actor介绍

scala的Actor并发编程模型可以用来开发比Java线程效率更高的并发程序。我们学习scala Actor的目的主要是为后续学习Akka做准备。







## Java并发编程的问题

在Java并发编程中，每个对象都有一个逻辑监视器（monitor），可以用来控制对象的多线程访问。我们添加sychronized关键字来标记，需要进行同步加锁访问。这样，通过加锁的机制来确保同一时间只有一个线程访问共享数据。但这种方式存在资源争夺、以及死锁问题，程序越大问题越麻烦。

[![1552787178794](assets/1552787178794.png)](assets/1552787178794.png)

**线程死锁**

[![1552788042478](assets/1552788042478.png)](assets/1552788042478.png)





## Actor并发编程模型

Actor并发编程模型，是scala提供给程序员的一种与Java并发编程完全不一样的并发编程模型，是一种基于事件模型的并发机制。Actor并发编程模型是一种不共享数据，依赖消息传递的一种并发编程模式，有效避免资源争夺、死锁等情况。

[![1552787528554](assets/1552787528554.png)](assets/1552787528554.png)



## Java并发编程对比Actor并发编程

| Java内置线程模型                                  | scala Actor模型                      |
| :------------------------------------------------ | :----------------------------------- |
| "共享数据-锁"模型 (share data and lock)           | share nothing                        |
| 每个object有一个monitor，监视线程对共享数据的访问 | 不共享数据，Actor之间通过Message通讯 |
| 加锁代码使用synchronized标识                      |                                      |
| 死锁问题                                          |                                      |
| 每个线程内部是顺序执行的                          | 每个Actor内部是顺序执行的            |



 Note



scala在2.11.x版本中加入了Akka并发编程框架，老版本已经废弃。Actor的编程模型和Akka很像，我们这里学习Actor的目的是为学习Akka做准备。







# 发送消息/接收消息

我们之前介绍Actor的时候，说过Actor是基于事件（消息）的并发编程模型，那么Actor是如何发送消息和接收消息的呢？





## 使用方式

**发送消息**

我们可以使用三种方式来发送消息：

| **！** | **发送异步消息，没有返回值**          |
| :----- | :------------------------------------ |
| **!?** | **发送同步消息，等待返回值**          |
| **!!** | **发送异步消息，返回值是Future[Any]** |

例如：

要给actor1发送一个异步字符串消息，使用以下代码：

```scala
actor1 ! "你好!"
Copy
```



**接收消息**

Actor中使用receive方法来接收消息，需要给receive方法传入一个偏函数

```scala
{
    case 变量名1:消息类型1 => 业务处理1,
    case 变量名2:消息类型2 => 业务处理2,
    ...
}
Copy
```





 Note



receive方法只接收一次消息，接收完后继续执行act方法





我们希望ActorReceiver能够一直接收消息，怎么实现呢？

——我们只需要使用一个while(true)循环，不停地调用receive来接收消息就可以啦。





## 使用loop和react优化接收消息

上述代码，使用while循环来不断接收消息。

- 如果当前Actor没有接收到消息，线程就会处于阻塞状态
- 如果有很多的Actor，就有可能会导致很多线程都是处于阻塞状态
- 每次有新的消息来时，重新创建线程来处理
- 频繁的线程创建、销毁和切换，会影响运行效率

在scala中，可以使用loop + react来复用线程。比while + receive更高效





## 示例

**示例说明**

使用loop + react重写上述案例

**参考代码**

```scala
// 持续接收消息
loop {
    react {
        case msg:String => println("接收到消息：" + msg)
    }
}
```





# 发送和接收自定义消息

我们前面发送的消息是字符串类型，Actor中也支持发送自定义消息，常见的如：使用样例类封装消息，然后进行发送处理。

## 示例一

**示例说明**

- 创建一个MsgActor，并向它发送一个同步消息，该消息包含两个字段（id、message）
- MsgActor回复一个消息，该消息包含两个字段（message、name）
- 打印回复消息



 Tip



- 使用`!?`来发送同步消息
- 在Actor的act方法中，可以使用sender获取发送者的Actor引用

**参考代码**

```scala
  case class Message(id:Int, msg:String)
  case class ReplyMessage(msg:String, name:String)

  object MsgActor extends Actor {
    override def act(): Unit = {
      loop {
        react {
          case Message(id, msg) => {
            println(s"接收到消息:${id}/${msg}")
            sender ! ReplyMessage("不太好", "Tom")
          }
        }
      }
    }
  }

  def main(args: Array[String]): Unit = {
    MsgActor.start()

    val replyMessage: Any = MsgActor !? Message(1, "你好")
    println("回复消息:" + replyMessage.asInstanceOf[ReplyMessage])
  }
Copy
```

## 示例二

**示例说明**

- 创建一个MsgActor，并向它发送一个异步无返回消息，该消息包含两个字段（message, company）





 Tip



使用`!`发送异步无返回消息



**参考代码**

```scala
case class Mesasge(message:String, company:String)

object MsgActor extends Actor {
    override def act(): Unit = {
        loop {
            react {
                case Mesasge(message, company) =>
                println(s"MsgActor接收到消息:${message}/${company}")
            }
        }
    }
}

def main(args: Array[String]): Unit = {
    MsgActor.start()

    MsgActor ! Mesasge("中国联通", "大爷，快交话费！")
}
Copy
```

## 示例三

**示例说明**

- 创建一个MsgActor，并向它发送一个异步有返回消息，该消息包含两个字段（id、message）
- MsgActor回复一个消息，该消息包含两个字段（message、name）
- 打印回复消息





 Tip



- 使用`!!`发送异步有返回消息
- 发送后，返回类型为Future[Any]的对象
- Future表示异步返回数据的封装，虽获取到Future的返回值，但不一定有值，可能在将来某一时刻才会返回消息
- Future的isSet()可检查是否已经收到返回消息，apply()方法可获取返回数据

**参考代码**

```scala
case class Message(id:Int, message:String)
case class ReplyMessage(message:String, name:String)

object MsgActor extends Actor {
    override def act(): Unit = {
        loop {
            react {
                case Message(id, message) =>
                println(s"MsgActor接收到消息：${id}/${message}")
                sender ! ReplyMessage("收到消息！", "JIm")
            }
        }
    }
}

def main(args: Array[String]): Unit = {
    MsgActor.start()

    val future: Future[Any] = MsgActor !! Message(1, "你好！")

    while(!future.isSet) {}

    val replyMessage = future.apply().asInstanceOf[ReplyMessage]
    println(replyMessage)
}
```



# 高阶函数

scala 混合了面向对象和函数式的特性，在函数式编程语言中，函数是“头等公民”，它和Int、String、Class等其他类型处于同等的地位，可以像其他类型的变量一样被传递和操作。

高阶函数包含

- 作为值的函数
- 匿名函数
- 闭包
- 柯里化等等



# 隐式转换和隐式参数

隐式转换和隐式参数是scala非常有特色的功能，也是Java等其他编程语言没有的功能。我们可以很方便地利用隐式转换来丰富现有类的功能。后面在编写Akka并发编程、Spark SQL、Flink都会看到隐式转换和隐式参数的身影。



# 自动导入隐式转换方法

前面，我们手动使用了import来导入隐式转换。是否可以不手动import呢？

在scala中，如果在当前作用域中有隐式转换方法，会自动导入隐式转换。

示例：将隐式转换方法定义在main所在的object中

```scala
class RichFile(val f:File) {
  // 将文件中内容读取成字符串
  def read() = Source.fromFile(f).mkString
}

object ImplicitConvertDemo {
  // 定义隐式转换方法
  implicit def file2RichFile(f:File) = new RichFile(f)

  def main(args: Array[String]): Unit = {
    val f = new File("./data/textfiles/1.txt")

    // 调用的其实是RichFile的read方法
    println(f.read())
  }
}
```



# 隐式参数

方法可以带有一个标记为implicit的参数列表。这种情况，编译器会查找缺省值，提供给该方法。

 Note



1. 和隐式转换一样，可以使用import手动导入隐式参数
2. 如果在当前作用域定义了隐式值，会自动进行导入