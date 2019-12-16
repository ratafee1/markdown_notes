# Angular 5.x 学习笔记（15）——<router-outlet> 干什么用的？





### 序言

> 在 Angular 5.X 中，有一个特别的标签： <router-outlet>  ， 其实，同样的，甚至同名的标签，在 React 中也有。 可见 Angular 与 React 的相似性有多高！

在 app.module.ts 路由文件中，有这么一段代码：



```javascript
imports: [
     BrowserModule,
     RouterModule.forRoot(
       [
         {
          path: '',
          redirectTo:'/home',
          pathMatch: 'full'
         },

         { path: 'home', 
          component: HomeComponent 
         },
         {
          path: 'about',
          component: AboutComponent
         },
         {
          path: 'dashboard',
          component: DashboardComponent
         }
       ]
     )
   ],
```

这段代码，意在配置路由， 根据不同的 URL， 跳转到不同的页面。 注意： 这是单页面应用（SPA），只是局部的内容变化，不需要整个页面跳转。 不会出现加载的进度条。

讲述了路由配置文件，再来看页面：

index.html   是整个APP的页面入口。 代码如下：



```javascript
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>HelloWorld</title>
  <base href="/">

  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" type="image/x-icon" href="favicon.ico">
</head>
<body>
  <app-root></app-root>
</body>
</html>
```

关键的一行代码是：

> <app-root></app-root>

这里 `` 相当于是局部页面的占位符。 这个区域是动态加载的，运行时，会被 app.component.html 替换掉。具体来说，就是被以下页面替换掉。

`app.component.html` 文件代码如下：



```javascript
<div style="text-align:center">
    <h1>
     {{title}}!!
    </h1>
    <nav>
      <a routerLink="home" routerLinkActive="active">Home</a>
      <a routerLink="about">About</a>
      <a routerLink="dashboard">Dashboard</a>
    </nav>
    <router-outlet></router-outlet>
  </div>
```

**代码解读：**  关键的代码是：

> <router-outlet></router-outlet>

可以简单把它理解为： 页面的占位符，动态加载，会被替换掉的。
 当点击 home、about、 dashboard 时， 在导航栏的下方，会被对应的 XX.component.html 替换掉。 这就是单页面路由的原理。

#### 深度理解 <router-outlet>

Routers 参数是一个有路由定义组成的一个数组。路由定义分如下两部分：
 Path：这个是用来匹配浏览器地址中的URL。
 Component：路由对应的组件。

**让路由可用**

引入 RouterModule，即把 RouterModule 添加到 AppModule 的imports 数组中。

> import { RouterModule }   from '@angular/router';

****

如果没有 <router-outlet>， 又会怎样呢？

如果在浏览器的地址栏中添加 /about ，比如： [http://localhost:4200/about](https://link.jianshu.com?t=http%3A%2F%2Flocalhost%3A4200%2Fabout)
 路由本应该会匹配地址，并显示 AboutComponent 。然而事实并非如此。我们需要告诉路由要在哪里显示这个AboutComponent组件。为了实现这个，需要在  about.component.html 的最后添加 <router-outlet> 元素，<router-outlet> 是 RouterModule 中的其中一个指令。

当然，在实际应用中，我们不会手动在地址栏中输入/about的， 而是通过 <a> 标签来实现。



```javascript
<nav>
      <a routerLink="home" routerLinkActive="active">Home</a>
      <a routerLink="about">About</a>
      <a routerLink="dashboard">Dashboard</a>
    </nav>
```

##### 再来看个例子



```html
<nav class="navbar navbar-default">
  <div class="container-fluid">
    <ul class="nav navbar-nav">
      <li class="active">
        <a routerLink="create" routerLinkActive="active">
          Add coins
        </a>
      </li>    
    </ul>
  </div>
</nav>

<div class="container">
  <router-outlet></router-outlet>
</div>
```

> <router-outlet></router-outlet> 到底是怎么占位的呢？

当点击 Add coins 这个 <a> 标签时，会激活 <router-outlet>

> <a routerLink="create" routerLinkActive="active"> Add coins </a>

这个时候， 以下的 div 区域会被替换：

<div class="container"> <router-outlet></router-outlet> </div>

这就是说， 如果想在哪个区域显示 create.component.html 这个子网页，只需要添加 <router-outlet> 就可以了。

