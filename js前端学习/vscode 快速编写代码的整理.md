# [vscode 快速编写代码的整理](https://www.cnblogs.com/ling-nl/p/10867510.html)

**一、快速编辑HTML代码**

  **1、添加类、id、文本和属性**

输入 .box

	<div class="box"></div>

输入p#text

	<p id="text"></p>

元素和内容一块输出 p{你好}

	<p>你好</p>

输出属性 a[href=#]

~~~
<a href="#"></a>
~~~

**2、嵌套**

　　（1）输入div+p

	<div></div>
	<p></p>
（2）输入ul>li*3>a

~~~
<ul>
    <li><a href=""></a></li>
    <li><a href=""></a></li>
    <li><a href=""></a></li>
</ul>
~~~

(3) >：子元素符号，表示嵌套的元素

​       +：同级标签符号

​		^:代表上级元素

**4、定义多个带属性的元素
**

　　　输入ul>li.item$*3，代码输出

~~~
<ul>
    <li class="item1"></li>
    <li class="item2"></li>
    <li class="item3"></li>
</ul>
~~~

**二、CSS缩写** 

**1. 值** 
　　　　比如要定义元素的宽度，只需输入w100，即可生成 　

~~~
width: 100px; 
~~~

 **2. 附加属性**

　　　可能你之前已经了解了一些缩写，比如 @f，可以生成：

**3. 模糊匹配**

　　　　如果有些缩写你拿不准，Emmet会根据你的输入内容匹配最接近的语法，比如输入ov:h、ov-h、ovh和oh，生成的代码是相同的：

~~~
overflow: hidden; 
~~~



### 示例

p{简写必须写在一行,然后再末尾Tab}+ul>(li.item$>a[target='_blank' href='http://www.baidu.com'].btn.btn-default{百度})*4





