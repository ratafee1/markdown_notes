# [gulp遇到错误:The following tasks did not complete: default Did you forget to signal async completion?](https://www.cnblogs.com/chorkiu/p/11435774.html)



运行之后会像下面一样报这个错误,因为事按着一个视频来写的,所以

![img](https://img2018.cnblogs.com/blog/1290097/201908/1290097-20190830163349951-861080877.png)

 

 原本的gulpfile.js如下

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
const gulp = require('gulp')
gulp.task('default',()=>{
    // console.log('default task');
    gulp.src(['src/**/*'])
        .pipe(gulp.dest('build'))
   
})
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

改成如下的形式就可以了

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
const gulp = require('gulp')
gulp.task('default',function(done){
    // console.log('default task');
    gulp.src(['src/**/*'])
        .pipe(gulp.dest('build'))
        done()
})
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

运行之后

![img](https://img2018.cnblogs.com/blog/1290097/201908/1290097-20190830163717201-992130713.png)

 

原因：因为gulp不再支持同步任务．因为同步任务常常会导致难以调试的细微错误，例如忘记从任务（task）中返回 stream。

当你看到 *"Did you forget to signal async completion?"* 警告时，说明你并未使用前面提到的返回方式。你需要使用 callback 或返回 stream、promise、event emitter、child process、observable 来解决此问题。具体详情请看[API的异步执行](https://www.gulpjs.com.cn/docs/getting-started/async-completion/)



















# gulp4.0报错‘The following tasks did not complete: ...’







在使用gulp4.0执行task的时候，使用匿名函数经常出现以下错误：

gulpfile.js



```javascript
var gulp = require('gulp');

gulp.task(server', () => {

  console.log("HTTP Server Started");

});
```

报错信息



```python
[17:33:34] Using gulpfile F:\web\GitLibrary\Management system\gulpfile.js

[17:33:34] Starting 'default'...

[17:33:34] Starting 'server'...

[17:33:34] Finished 'server' after 29 ms

[17:33:34] Starting '<anonymous>'...

[17:33:34] The following tasks did not complete: default, <anonymous>

[17:33:34] Did you forget to signal async completion?
```

解决的方法有五种，这五种除了最后一个都亲测没有问题。

本文翻译原文地址： https://stackoverflow.com/questions/36897877/gulp-error-the-following-tasks-did-not-complete-did-you-forget-to-signal-async



### 1. 返回一个stream

这种操作方式是用来新建task的，和3.x的用法一样。

```javascript
var print = require('gulp-print');



gulp.task('server', () => {
  return gulp.src('package.json')

    .pipe(print(function() { return 'HTTP Server Started'; }));

});
```

### 2. 返回一个Promise

在异步请求机制中，是有一个Promise对象的，它包含了请求的过程中所有内容。如下：

```javascript
gulp.task('server', () => { 

  return new Promise(function(resolve, reject) {
 console.log("HTTP Server Started");
 resolve();

  });

});
```

### 3. 返回一个回调函数

这个是最简单的一种方法，gulp会自动将这个回调函数作为一个参数返回到任务中，在完成的时候一定要调用这个函数。如下：

```javascript
gulp.task('default', gulp.series('server', (done) => done()))
```

### 4. 返回一个子进程child process

当我们只是执行一段纯js代码，没有用到node相关的方法时用这个方法。



```javascript
const spawn = require('child_process').spawn;
gulp.task('server', function() {

  return spawn('echo', ['HTTP', 'Server', 'Started'], { stdio: 'inherit' });

});
```

### 5. 返回一个 RxJS Observable.

这个方法我没有过使用过，但是如果你是用RxJS 的时候，可以用这个方法。



```javascript
const Observable = require('rx').Observable;

gulp.task('server', function() {

  let o = Observable.just('HTTP Server Started');

  o.subscribe(function(str) {

    console.log(str);

  });

  return o;

});
```