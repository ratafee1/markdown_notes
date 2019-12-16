### 项目优化策略



![image-20191209121159325](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191209121159325.png)



![image-20191209121730996](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191209121730996.png)



![image-20191209121844255](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191209121844255.png)





![image-20191209121940573](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191209121940573.png)
![image-20191209122039078](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191209122039078.png)



### 5.通过chainWebpack自定义打包入口

~~~js
module.exports = {
  lintOnSave: false,
  chainWebpack:config=>{
    config.when(process.env.NODE_ENV === 'production', config =>{
      config.entry('app').clear().add('./src/main-prod.js')
    })
    config.when(process.env.NODE_ENV === 'development', config =>{
      config.entry('app').clear().add('./src/main-dev.js')
    })
  }
}
~~~



![image-20191209123121472](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191209123121472.png)



![image-20191209123500732](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191209123500732.png)

![image-20191209124200758](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191209124200758.png)



![image-20191209124608225](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191209124608225.png)



![image-20191209124720153](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191209124720153.png)



![image-20191209125438035](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191209125438035.png)



### 8.首页内容定制

不同的打包环境下，首页内容可能会有所不同。我们可以通过插件的方式进行定制



![image-20191209132518137](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191209132518137.png)



# 项目上线

![image-20191209133823533](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191209133823533.png)



![image-20191209134105345](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191209134105345.png)



![image-20191209134435460](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191209134435460.png)

![image-20191209134940047](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191209134940047.png)



![image-20191209135255301](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191209135255301.png)

![image-20191209135652275](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191209135652275.png)



# Vuex

![image-20191209140401084](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191209140401084.png)



![image-20191209140524987](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191209140524987.png)

![image-20191209140824932](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191209140824932.png)

![image-20191209141035817](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191209141035817.png)

![image-20191209141235658](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191209141235658.png)

![image-20191209141316011](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191209141316011.png)

# Vuex的基本使用

![image-20191209141557691](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191209141557691.png)



![image-20191209141723687](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191209141723687.png)



![image-20191209143405108](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191209143405108.png)
![image-20191209143605276](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191209143605276.png)



![image-20191209143941248](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191209143941248.png)



![image-20191209144335325](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191209144335325.png)

### 可以在触发mutations时传递参数

![image-20191209144805984](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191209144805984.png)

![image-20191209145037234](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191209145037234.png)

