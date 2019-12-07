# [JavaScript ES6 module 模块](https://www.cnblogs.com/polk6/p/js-ES6-module.html)

在使用JavaScript开发大型项目时，模块开发概念是一个必须考虑的问题。其目的就是通过命名空间对各类业务对象进行一定的封装，防止命名冲突。

本篇着重介绍ES6 module中的export和import概念。

 

# 1. ES5的模块支持方案

在ES6之前，JavaScript本身没有模块支持，但社区创造了令人印象深刻的解决方案。两个最重要的（也是不相容的）标准是：**AMD** 和 **CommonJS**。

## 1.1 AMD

**说明**：AMD，全称为Asynchronous Module Definition，即异步模块定义。

**特点**：其模块和依赖都可以进行异步加载。

```
`// 定义AMD模块``define(``'User/UserGrid'``, ``// 模块ID``    ``[``'UserM'``], ``// 依赖文件``    ``function``(userM) { ``// 初始化函数，依赖文件以参数形式加入``    ``}``);` `// 使用AMD模块``require([``'User/UserGrid'``],``    ``function``(userGrid) {``    ``}``);`
```

 

## 1.2 CommonJS

**说明**：CommonJS模块规范初衷是用于node.js服务器端，以提供额外的功能，如：IO、文件系统等功能。

**特点**：

①同步加载；只有加载完成，才能执行后面的操作。

②缓存加载；第一次加载时会把内容存入缓存，以后的加载都是从缓存获取。

**示例**：

```
`// math.js(定义模块)``exports.add = ``function``(a, b) {``    ``return` `a + b;``};` `// app.js(使用模块)``var` `math = require(``'./math'``);` `var` `rs = math.add(1, 2);``console.log(rs);`
```

了解更多AMD 与 CommonJS 知识可参考此文章：[Writing Modular JavaScript With AMD, CommonJS & ES Harmony](https://addyosmani.com/writing-modular-js/)

 

# 2. ES6 module

ES6 module 结合了CommonJS和AMD的优点：类似CommonJS，具有简洁的语法，对循环依赖的支持；类似AMD，支持异步加载和有条件的模块加载。

ES6 module 使用 export 导出模块的内容，并使用 import 导入模块的内容。

## 2.1 浏览器原声支持

使用之前，先看下各浏览器对原生ES6 module的支持情况：Chrome61及61+、Edge16及16+版本都已支持

![img](https://images2017.cnblogs.com/blog/153475/201801/153475-20180105151759815-580610057.png)

### 使用方式：

以Chrome为例，在引入ES6 module 的JS文件时，使用属性 type="module" 即可：

```
`<``script` `type="module" src="js/math.js"></``script``>``<``script` `type="module" src="js/app.js"></``script``>`
```

## 2.2 export 导出（定义模块）

创建ES6模块时，可使用**export**关键字导出(对外提供)模块的内容，如函数、对象以及原始变量等等。

export 导出方案有2种：Named exports（命名导出；每个模块可有多个）和 Default exports（默认导出；每个模块只能一个）。

### 1) Named exports 命名导出

**说明**：使用 **export + 名称** 的形式导出模块的内容。

**注意**：在 import 导入过程中，需指定这些名称。

**语法**：

```
`// 1)声明时导出``export` `var` `myVar1 = ``'a'``;``export` `let` `myVar2 = ``'b'``;``export` `const MY_CONST = ``'c'``;``export` `function` `myFunc() {}` `// 2)声明后导出``var` `myVar3 = ``'a'``;``export` `{ myVar3 };` `// 3)别名导出``var` `myVar4 = ``'a'``;``export` `{ myVar4 as myVar };`
```

**示例**：

```
`// math.js``export` `function` `add(a, b) {``    ``return` `a + b;``}` `// app.js：导入含有命名导出的模块时，需要指定成员名称``import` `{ add } from ``'./math.js'``;``console.log(add(1, 2)); ``// => 3` `// demo.html``<script type=``"module"` `src=``"js/math.js"``></script>``<script type=``"module"` `src=``"js/app.js"``></script>`
```

 

### 2) Default exports 默认导出

**说明**：使用 **export default** 导出模块默认的内容，每个模块只能有一个 export default。

**语法**：

```
`// 1)声明时导出``export` `default` `expression;``export` `default` `function` `() {}` `// 2)别名设置为default导出``export` `default` `function` `name1() {}``export` `{ name1 as ``default` `};`
```

**示例**：默认导出声明的是一个表达式，通常没有名字，导入时需指定模块名称。

```
`// math.js``export` `function` `add(a, b) {``    ``return` `a + b;``}``export` `default` `function` `cube(x) {``    ``return` `x * x * x;``}` `// app.js：导入默认导出的模块时，需要指定模块名称``import` `cube from ``'./math.js'``;``console.log(cube(3)); ``// => 27``// 若想同时导入含有默认导出、命名导出的模块，只需要导入时用','隔开``// import cube, { add } from './math.js';` `// demo.html``<script type=``"module"` `src=``"js/math.js"``></script>``<script type=``"module"` `src=``"js/app.js"``></script>`
```

 

## 2.3 import 导入模块

使用 import 可导入创建的模块。

**语法**：

```
`// 1)导入模块的默认导出内容``import` `defaultExport from ``'module-name'``;` `// 2)导入模块的命名导出内容``import` `{ export1, export2 } from ``'module-name'``;``import` `{ ``export` `as alias } from ``'module-name'``; ``// 修改别名``import` `* as name from ``'module-name'``; ``// 导入模块内的所有命名导出内容` `// 3)导入模块的默认导出、命名导出``import` `defaultExport, { export1, export2 } from ``'module-name'``;``import` `defaultExport, * as name from ``'module-name'``;`
```

 

### 1) 导入默认导出

**说明**：导入默认导出的模块时，需要指定模块名称

**示例**：

```
`// math.js``export` `default` `function` `cube(x) {``    ``return` `x * x * x;``}` `// app.js：导入默认导出的模块时，需要指定模块名称``import` `cube from ``'./math.js'``;``console.log(cube(3)); ``// => 27`
```

 

### 2) 导入命名导出

**说明**：导入模块时可使用**大括号包含指定命名成员**；也可以用  *** as moduleName** 的形式把此模块的所有命名导出作为某个对象的成员。

**示例**：

```
`// math.js``export` `function` `add(a, b) {``    ``return` `a + b;``}` `// app.js：指定使用math模块的add命名导出``import` `{ add } from ``'./math.js'``;``console.log(add(1, 2)); ``// => 3` `// 导入所有的命名导出作为math对象的成员``import` `* as math from ``'./math.js'``;``console.log(math.add(1, 2)); ``// => 3`
```

 

### 3) 仅导入模块

**说明**：仅导入模块时，只会执行模块的全局函数，不会导入任何成员。

**示例**：

```
`// math.js``export` `function` `add(a, b) {``    ``return` `a + b;``}``(``function``() {``    ``console.log(``'hello math.js'``);``})();` `// app.js``import` `{ add } from ``'./math.js'``; ``// => hello math.js`
```