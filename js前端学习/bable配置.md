# bable安装

~~~
npm install --save-dev @babel/core @babel/cli @babel/preset-env npm install --save @babel/polyfill
~~~



运行此命令将 `src` 目录下的所有代码编译到 `lib` 目录：

~~~
./node_modules/.bin/babel src --out-dir lib
~~~

