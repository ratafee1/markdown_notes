### Node.js中通过babel体验ES6模块化

1.npm install --save-dev @babel/core @babel/cli @babel/preset-env @babel/node

2.npm install --save @babel/polyfill

3.项目根目录创建文件	babel.config.js

4.babel.config.js文件内容

const presets = [

  ["@babel/env",{

​    targets:{

​      edge:"17",

​      firefox:"60",

​      chrome:"67",

​      safari:"11.1"

​    }

  }]

]

module.exports ={presets}

5.npx babel-node ./index.js 

### ES6默认导出与默认导入

1.默认导出语法 export default {

}

2.默认导入语法 import 接收名称 from '模块标识符'

import m1 from './m1.js'

注意：每个模块中，只允许使用一次export default，否则会报错

### ES6按需导出与按需导入

1.按需导出export let s1 = 'aaa'

export function say = function(){

}

2.按需导入import {s1, s2 as ss2, say} from './m1.js'

### 直接导入并执行模块代码

有时候，我们只想单纯执行某个模块中的代码，并不需要得到模块中向外暴露的成员，此时，可以直接导入并执行模块代码

### 当前WEB开发面临的困境

文件依赖关系错综复杂

静态资源请求效率低

模块化支持不友好

浏览器对高级Javascript特性兼容程度低

etc……

### webpack概述

webpack是一个流行的前端项目构建工具（打包工具），可以解决当前web开发中所面临的困境

webpack提供了友好的模块化支持，以及代码压缩混淆、处理js兼容问题、性能优化等强大的功能，从而让程序员把工作的重心放到具体的功能实现上，提高了开发效率和项目的可维护性

绝大多数企业中的前端项目，都是基于webpack进行打包构建的

### 创建列表隔行变色项目

1. 新建空白项目 npm init -y，初始化包管理文件package.json
2. 新建src源代码目录
3. 新建src -> index.html首页
4. 运行npm install jquery -S 命令，安装jquery
5. 通过模块化的形式，实现列表隔行变色效果

### 在项目中安装和配置webpack

1. 运行 npm install webpack webpack-cli -D命令，安装webpack相关的包

2. 在项目根目录中，创建名为webpack.config.js的webpack配置文件

3. 在webpack.config.js中初始化如下基本配置：

   module.exports = {

   ​	mode: 'development'	// mode 用来指定构建模式

   }

4. 在package.json 配置文件中的scripts节点下，新增dev脚本如下：

   "scripts":{

   ​	"dev": "webpack"		// script 节点下的脚本，可以通过npm run 执行

   }

5. 在终端中运行npm run dev 命令，启动webpack进行项目打包

### 配置webpack打包的入口与出口

1. 打包的入口文件为src -> index.js

2. 打包的出口文件为dist -> main.js

3. 如果要修改打包的入口与出口，可以在webpack.config.js中新增如下配置信息：

   const path = require('path')	//导入node.js中专门操作路径的模块

   module.exports = {

   ​	entry: path.join(__dirname, './src/index.js'),	//打包入口文件的路径

   ​	output: {

   ​		path: path.join(__dirname, './dist'),	//输出文件的存放路径

   ​		filename: 'bundle.js'	//输出文件的名称

   }

   }

### 配置webpack的自动打包功能

1.运行 npm install webpack-dev-server -D,安装自动打包工具

2.修改package.json->scripts 中的dev命令如下:

​	"scripts":{

​		"dev": "webpack-dev-server"		//script 节点下的脚本,可以通过npm run 执行	

​	}

3. 将src-index.html中,script脚本的引用路径,修改为"/bundle.js"
4. 运行npm run dev命令,重新进行打包
5. 在浏览器中访问 http://localhost:8080地址,查看自动打包效果

注意:webpack-dev-server 会启动一个实时打包的 http 服务器

​		webpack-dev-server 打包生成的输出文件,默认放到了项目根目录中,而且是虚拟的、看不见的

### 配置html-webpack-plugin生成预览页面

1.运行 npm install html-webpack-plugin -D命令,安装生成预览页面的插件

2.修改webpack.config.js 文件头部区域,添加如下配置信息:

​	const HtmlWebpackPlugin = require('html-webpack-plugin')

​	const htmlPlugin = new HtmlWebpackPlugin ({	//创建插件的实例对象

​		template: './src/index.html',	//指定要用到的模板文件

​		filename: 'index.html'	//指定生成的文件名称

​	})

3.修改 webpack.config.js 文件中向外暴露的配置对象,新增如下配置节点:

​	module.exports = {

​		plugins: [htmlPlugin]	//plugins数组是webpack打包期间会用到的一些插件列表

​	}

### 配置自动打包的相关参数

在package.json中的配置

"scripts":{

​	"dev": "webpack-dev-server  --open  --host  127.0.0.1  --port  8888"

}

### webpack中的加载器

1.通过loader打包非js模块

loader加载器可以协助webpack打包处理特定的文件模块,比如:

less-loader可以打包处理.less相关的文件

sass-loader可以打包处理.scss相关的文件

url-loader可以打包处理css中与url路径相关的文件

![image-20191203120251267](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191203120251267.png)

### webpack中加载器的基本使用

1.打包处理css文件

运行 npm i style-loader css-loader -D 命令，安装处理css文件的loader

在webpack.config.js的module->rules数组中，添加loader规则如下：

//所有第三方文件模块的匹配规则

module:{

​	rules:[

​		{ test: /\\.css$/, use:['style-loader', 'css-loader']}

​	]

}

test表示匹配的文件类型，use表示对应要调用的loader

注意：use数组中指定的loader顺序是固定的，多个loader的调用顺序是：从后往前调用

### 打包处理less文件

1. 运行 npm i less-loader less -D命令

2. 在webpack.config.js的module->rules数组中，添加loader规则如下：

   module:{

   ​	rules:[

   ​		{test: /\\.less$/, use:['style-loader','css-loader','less-loader']}

   ​	]

   }

### 打包处理scss文件

1. 运行npm i sass-loader node-sass -D命令

2. 在webpack.config.js的module->rules数组中，添加loader规则如下：

   module:{

   ​	rules:[

   ​		{test: /\\.scss$/, use:['style-loader','css-loader','sass-loader']}

   ​	]

   }

### postCSS自动添加css的兼容前缀

1. 运行npm i postcss-loader autoprefixer -D命令

2. 在项目根目录中创建postcss的配置文件postcss.config.js,并初始化如下配置：

   const autoprefixer = require('autoprefixer')	//导入自动添加前缀的插件

   module.exports = {

   ​	plugins: [autoprefixer]	//挂载插件

   }

3. 在webpack.config.js的module->rules数组中,修改css的loader规则如下:

   module:{

   ​	rules:[

   ​		{test: /\\.css$/, use:['style-loader','css-loader','postcss-loader']}

   ​	]

   }

### 打包样式表中的图片和字体文件

1. 运行npm i url-loader file-loader -D命令

2. 在webpack.config.js的module->rules数组中,添加规则如下;

   module:{

   ​	rules:[

   ​		{

   ​			test:/\\.jpg|png|gif|bmp|ttf|eot|svg|woff|woff2$/,

   ​			use:'url-loader?limit=16940'

   ​		}

   ​	]

   }

limit用来指定图片的大小,单位是字节,只有小于limit大小的图片,才会被转为base64图片

### 打包处理js文件中的高级语法

1. 安装babel转换器相关的包:npm i babel-loader @babel/core @babel/runtime -D

2. 安装babel语法插件相关的包:npm i @babel/preset-env @babel/plugin-transform-runtime @babel/plugin-proposal-class-properties -D

3. 在项目根目录中,创建babel配置文件babel.config.js并初始化基本配置如下:

   module.exports = {

    presets: ['@babel/preset-env'],

    plugins: ['@babel/plugin-transform-runtime', '@babel/plugin-proposal-class-properties']

   }

4. 在webpack.config.js的module->rules数组中,添加loader规则如下:

   //exclude为排除项,表示babel-loader不需要处理node_modules中的js文件

   {test:/\\.js$/, use:'babel-loader', exclude:/node_modules/}

   

   

   

### 传统组件的问题和解决方案

#### 问题

   1.全局定义的组件必须保证组件的名称不重复

   2.字符串模板缺乏语法高亮,在HTML有多行的时候,需要用到丑陋的\

   3.不支持CSS意味着当HTML和JavaScript组件化时,CSS明显被遗漏

   4.没有构建步骤限制,只能使用HTML和ES5 JavaScript,而不能使用预处理器(如:Babel)

#### 解决方案

   针对传统组件的问题,Vue提供了一个解决方案—使用Vue单文件组件

   

### Vue单文件组件的组成结构

   template 组件的模板区域

   script 业务逻辑区域

   style 样式区域

   <template>
       <!-- 这里用于定义Vue组件的模板内容 -->
   </template>

   <script>
       //这里用于定义Vue组件的业务逻辑
       export default{
           data:() {return {}},	//私有数据
           methods: {}	//处理函数
       	//...其他业务逻辑
       }
   </script>

   <style>
       /*这里用于定义组件的样式*/
   </style>

### webpack中配置vue组件的加载器

   1. 运行npm i vue-loader vue-template-compiler -D命令

   2. 在webpack.config.js配置文件中,添加vue-loader的配置项如下:

      const VueLoaderPlugin = require('vue-loader/lib/plugin')

      module.exports = {

      ​	module:{

      ​		rules:[

      ​			{test:/\\.vue$/, loader:'vue-loader'}

      ​		]

      ​	},

      ​	plugins:[

      ​		new VueLoaderPlugin()	//确保引入这个插件

      ​	]

      }

### 在webpack项目中使用Vue

1. 运行npm i vue -S 安装vue

2. 在src->index.js 入口文件中,通过import Vue from 'vue'来导入vue构造函数

3. 创建vue的实例对象,并指定要控制的el区域

4. 通过render函数渲染App根组件

   import Vue from 'vue'

   import App from './components/App.vue'

   const vm = new Vue({

   ​	//指定vm实例要控制的页面区域

   ​	el: '#app',

   ​	//通过render函数,把指定的组件渲染到el区域中

   ​	render: h => h(App)

   })

### webpack 打包发布

//在package.json文件中配置webpack打包命令

//该命令默认加载项目根目录中的webpack.config.js配置文件

"scripts":{

​	//用于打包的命令

​	"build": "webpack -p",

​	//用于开发调试的命令

​	"dev": "webpack-dev-server --open --host 127.0.0.1 --port 3000"

}

### Vue脚手架的基本用法

Vue脚手架用于快速生成Vue项目基础架构,官网地址为:https://cli.vuejs.org/zh/

npm install -g @vue/cli

1.基于交互式命令行的方式,创建新版vue项目

vue create my-project

2.基于图形化界面的方式,创建新版vue项目

vue ui

3.基于2.x的旧模板,创建旧版vue项目

npm install -g @vue/cli-init

vue init webpack my-project

###  

### Vue脚手架的自定义配置
通过package.json配置项目

"vue":{

  "devServer":{

   "port":8888,

   "open":true

  }

 }

推荐将vue脚手架相关的配置，单独定义到vue.config.js配置文件中

1. 在项目根目录创建vue.config.js

2. module.exports = {

   ​	devServer:{

   ​		port:8888

   ​		open:true

   ​	}

   }



### Element-UI的基本使用

Element-UI:一套为开发者、设计师和产品经理准备的基于Vue 2.0的桌面端组件库

官方网址：http://element-cn.eleme.io/#/zh-CN

1.安装依赖包 npm i element-ui -S

2.导入 Element-UI相关资源

//导入组件库

import ElementUI from 'element-ui'

//导入组件相关样式

import 'element-ui/lib/theme-chalk/index.css'

//配置Vue插件

Vue.use(ElementUI)

