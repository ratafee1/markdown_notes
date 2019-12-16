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

