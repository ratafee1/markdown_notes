# HTML5 Web Workers



web worker 是运行在后台的 JavaScript，不会影响页面的性能。

------

## 什么是 Web Worker？

当在 HTML 页面中执行脚本时，页面的状态是不可响应的，直到脚本已完成。

web worker 是运行在后台的 JavaScript，独立于其他脚本，不会影响页面的性能。您可以继续做任何愿意做的事情：点击、选取内容等等，而此时 web worker 在后台运行。

------

## 浏览器支持

![Internet Explorer](https://www.runoob.com/images/compatible_ie.gif)![Firefox](https://www.runoob.com/images/compatible_firefox.gif)![Opera](https://www.runoob.com/images/compatible_opera.gif)![Google Chrome](https://www.runoob.com/images/compatible_chrome.gif)![Safari](https://www.runoob.com/images/compatible_safari.gif)

Internet Explorer 10, Firefox, Chrome, Safari 和 Opera 都支持Web workers.

------

## HTML5 Web Workers 实例

下面的例子创建了一个简单的 web worker，在后台计数：

## 实例

计数:



开始 Worker 停止 Worker




[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_webworker)

demo_workers.js 文件代码：

var i=0;

function timedCount()
{
  i=i+1;
  postMessage(i);
  setTimeout("timedCount()",500);
}

timedCount();



------

## 检测浏览器是否支持 Web Worker

在创建 web worker 之前，请检测用户的浏览器是否支持它：

if(typeof(Worker)!=="undefined")
{
  // 是的! Web worker 支持!
  // *一些代码.....*
}
else
{
  //抱歉! Web Worker 不支持
}



------

## 创建 web worker 文件

现在，让我们在一个外部 JavaScript 中创建我们的 web worker。

在这里，我们创建了计数脚本。该脚本存储于 "demo_workers.js" 文件中：

var i=0;

function timedCount()
{
  i=i+1;
  postMessage(i);
  setTimeout("timedCount()",500);
}

timedCount();

以上代码中重要的部分是 postMessage() 方法 - 它用于向 HTML 页面传回一段消息。

**注意:** web worker 通常不用于如此简单的脚本，而是用于更耗费 CPU 资源的任务。

------

## 创建 Web Worker 对象

我们已经有了 web worker 文件，现在我们需要从 HTML 页面调用它。

下面的代码检测是否存在 worker，如果不存在，- 它会创建一个新的 web worker 对象，然后运行 "demo_workers.js" 中的代码：

if(typeof(w)=="undefined")
{
  w=new Worker("demo_workers.js");
}

然后我们就可以从 web worker 发生和接收消息了。

向 web worker 添加一个 "onmessage" 事件监听器：

w.onmessage=function(event){
  document.getElementById("result").innerHTML=event.data;
};

------

## 终止 Web Worker

当我们创建 web worker 对象后，它会继续监听消息（即使在外部脚本完成之后）直到其被终止为止。

如需终止 web worker，并释放浏览器/计算机资源，请使用 terminate() 方法：

w.terminate();



------

## 完整的 Web Worker 实例代码

我们已经看到了 .js 文件中的 Worker 代码。下面是 HTML 页面的代码：

## 实例

<!DOCTYPE html> <html> <head>  <meta charset="utf-8">  <title>菜鸟教程(runoob.com)</title>  </head> <body>   <p>计数： <output id="result"></output></p> <button onclick="startWorker()">开始工作</button>  <button onclick="stopWorker()">停止工作</button>   <p><strong>注意：</strong> Internet Explorer 9 及更早 IE 版本浏览器不支持 Web Workers.</p>   <script>

var w;  function startWorker() {    if(typeof(Worker) !== "undefined") {        if(typeof(w) == "undefined") {            w = new Worker("demo_workers.js");        }        w.onmessage = function(event) {            document.getElementById("result").innerHTML = event.data;        };    } else {        document.getElementById("result").innerHTML = "抱歉，你的浏览器不支持 Web Workers...";    } }  function stopWorker()  {     w.terminate();    w = undefined; }

</script>  </body> </html>


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_webworker)



------

## Web Workers 和 DOM

由于 web worker 位于外部文件中，它们无法访问下列 JavaScript 对象：

- window 对象
- document 对象
- parent 对象