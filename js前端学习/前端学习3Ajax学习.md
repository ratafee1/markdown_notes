# Ajax运行原理

Ajax相当于浏览器发送请求与接收响应的代理人，以实现在不影响用户浏览页面的情况下，局部更新页面数据，从而提高用户体验

### Ajax的实现步骤

创建Ajax对象

告诉Ajax请求地址以及请求方式

发送请求

获取服务器端给与客户端的响应数据

### 服务器端响应的数据格式

在真实的项目中，服务器端大多数情况下会以JSON对象作为响应数据的格式。当客户端拿到响应数据时，要将JSON数据和HTML字符串进行拼接，然后将拼接的结果展示在页面中。

### Ajax状态码

在创建ajax对象，配置ajax对象，发送请求，以及接收完服务器端响应数据，这个过程中的每一个步骤都会对应一个数值，这个数值就是ajax状态码。

0：请求未初始化（还没有调用open（））

1：请求已经建立，但还没有发送（还没有调用send（））

2：请求已经发送

3：请求正在处理中，通常响应中已经有部分数据可以用了

4：响应已经完成，可以获取并使用服务器的响应了

#### onreadystatechange事件，当Ajax状态码发生变化时将自动触发该事件



### Ajax错误处理

1.网络畅通，服务器端能接收到请求，服务器端返回的结果不是预期结果

可以判断服务器端返回的状态码，分别进行处理。xhr.status获取http状态码

2.网络畅通，服务器端没有接收到请求，返回404状态码

3.网络畅通，服务器端能接收到请求，服务器端返回500状态码

4.网络终端，请求无法发送到服务器端

会触发xhr对象下面的onerror事件，在onerror事件处理函数中对错误进行处理

### 低版本IE浏览器的缓存问题

问题：在低版本的IE浏览器中，Ajax请求有严重的缓存问题，即在请求地址不发生变化的情况下，只有第一次请求会真正发送到服务器端，后续的请求都会从浏览器的缓存中获取结果。即使服务器端的数据更新了，客户端依然拿到的是缓存中的旧数据。

解决方案：在请求地址的后面加请求参数，保证每一次请求中的请求参数的值不相同



### 同步异步概述

#### 异步	一个人一件事情做了一半，转而去做其他事情，当其他事情做完以后，再回过头来继续做之前未完成的事情。



### 请求参数要考虑的问题

1.请求参数位置的问题

​	将请求参数传递到ajax函数内部，在函数内部根据请求方式的不同将请求参数放置在不同的位置	get：放在请求地址的后面	post：放在send方法中

2.请求参数格式的问题

​	application/x-www-form-urlencoded	参数名称=参数值&参数名称=参数值	name=zhangsan&age=20

​	application/json	{name:'zhangsan',age:20}

1.传递对象数据类型对于函数的调用者更加友好

2.在函数内部对象数据类型转换为字符串数据类型更加方便





### Express Post

npm install body-parser

//extended:false	方法内部使用querystring模块处理请求参数的格式

//extended:true	方法内部使用第三方模块qs处理请求参数的格式

const bodyParser	=	require('body-parser')

app.use(bodyParser.urlencoded({extended: false}))



### Express路由参数

app.get('/find/:id',(req,res)=>{

})

localhost:3000/find/123

### Express 静态资源的处理

通过Express内置的express.static可以方便地托管静态文件，例如img、CSS、JavaScript文件等。

app.use(express.static('public'))



###	express-art-template模板引擎

#### 模板引擎

使用	npm install art-template express-art-template命令进行安装

//	当渲染后缀为art的模板时	使用express-art-template

app.engine('art',require('express-art-template'))

//	设置模板存放目录

app.set('views',path.join(__dirname, 'views'))

//渲染模板时不写后缀	默认拼接art后缀

app.set('view engine','art')

app.get('/index',(req,res)=>{

​	res.render('index',{

​		msg:	'message'

​	})

})



### app.locals对象

将变量设置到app.locals对象下面，这个数据在所有的模板中都可以获取到

app.locals.users=[{

​	name:	'zhangsan',

​	age:	20

},{

​	name:	'lisi',

​	age:	20

}]

<ul>
    {{each users}}
    <li>
    	{{$value.name}}
        {{$value.age}}
    </li>
    {{/each}}
</ul>





### 模板引擎

作用：使用模板引擎提供的模板语法，可以将数据和HTML拼接起来。

#### 使用步骤

1.下载art-template模板引擎库文件并在HTML页面中引入库文件

2.准备art-template模板

<script id='tpl', type='text/html'>
    <h1>{{username}} {{age}}</h1>
</script>

3.告诉模板引擎将哪一个模板和哪个数据进行拼接

<script>
    var html = template('tpl', {username: 		'zhangsan', age: '20'})
    document.getElementById('container').innerHTML=html
</script>



### 创建formidable表单解析对象

const form = new formidable.IncomingForm()

### 解析客户端传递过来的FormData对象

form.parse(req,(err,fields,files) =>{

​	

})

### 设置客户端上传文件的存储路径

form.uploadDir = path.join(__dirname, 'public', 'uploads')

### 保留上传文件的后缀名字

form.keepExtensions = true

### FormData文件上传进度展示

xhr.upload.onprogress = function (ev){

​	var result = (ev.loaded / ev.total) * 100 + '%'

​	bar.style.width = result

​	bar.innerHTML = result

}

### FormData对象的实例方法

1.获取表单对象中属性的值

formData.get('key')

2.设置表单对象中属性的值

formData.set('key', 'value')

3.删除表单对象中属性的值

formData.delete('key')

4.向表单对象中追加属性值

formData.append('key', 'value')

