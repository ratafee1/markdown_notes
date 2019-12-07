### Jquery属性操作，设置或获取元素属性

固有属性prop()，自定义属性attr()，

data()数据缓存，可以在指定的元素上存取数据，不会修改DOM元素结构。一旦页面刷新，之前存放的数据都会被移除

~~~html
<body>
    <a href="www.biying.com" title="必应网点">必应</a>
    <input type="checkbox" name="" id="" checked>
    <div index='1' data-index="3"></div>
    <span>123</span>
    <script>
        $(function() {
            console.log($('a').prop('href'))
            $('a').prop('title', '必应11')
            $('input').change(function() {
                console.log($(this).prop('checked'))
            })
            console.log( $('div').attr('index'))
            console.log( $('div').attr('data-index'))
            $('span').data('uname','andy')
            console.log( $('span').data('uname'))
            console.log( $('div').data('index'))

        })
    </script>
</body>
~~~



### Jquery文本值

主要针对元素内容和表单值的操作

1.普通元素内容html()	(相当于innerHTML)

2.普通元素文本内容text()	(相当于原生innerText)

3.表单的值val()	(相当于原生value)



### Jquery元素操作

遍历、创建、添加、删除元素

~~~html
<body>
    <div>1</div>
    <div>2</div>
    <div>3</div>
    <script>
        $(function(){
            var arr = ['red', 'yellow', 'blue']
            var sum = 0
            $('div').css('color','red')
         $('div').each((number, Element)=>{
            console.log(number)
            console.log(Element)
            $(Element).css('color',arr[number])
            sum += parseInt( $(Element).text())
            console.log(sum)
        })
        // $each
            $.each($('div'),function(number,Element){
                console.log(number)
                console.log(Element)
            })
            $.each(arr,function(number,Element){
                console.log(number)
                console.log(Element)
            })
            $.each({name:'andy',age:18},function(number,Element){
                console.log(number)
                console.log(Element)
            })
        })
        
    </script>
</body>
~~~



### 创建元素

~~~html
$('<li></li>')
~~~

### Jquery添加移除类

~~~
$('.cart-item').addClass('check-cart-item')
$('.cart-item').removeClass('check-cart-item')
~~~

### Jquery事件

4种常见的注册事件

on绑定事件的优势

Jquery事件委派的优点以及方式

绑定事件与解绑事件



### Jquery事件注册	事件处理	事件对象

### 单个事件注册

element.事件(function(){

})

$('div').click(function(){ 事件处理程序 })

其他事件基本和原生一致	如：mouseover、mouseout、blur、focus、change、keydown、keyup、resize、scroll