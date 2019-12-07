



# 年轻人的第一篇OpenGL ES 2.0教程





## Before we go

在高性能graphics领域，特别是3D graphics领域，[OpenGL](https://www.khronos.org/opengl/)无疑是目前的最佳选择，虽然，现在有很多集成度高的三方的库或者SDK，但是学习一下OpenGL仍然是非常有好处的，你可以了解基本的computer graphics的概念，这会让你在使用它们的时候更加的从容。

OpenGL是一个跨平台的高性能3D渲染API，[OpenGL ES](https://www.khronos.org/opengles/)是它的嵌入式平台版本。



![img](https:////upload-images.jianshu.io/upload_images/324257-0d8929408471e947.jpg?imageMogr2/auto-orient/strip|imageView2/2/w/690/format/webp)

OpenGL ES

我们即将踏上学习OpenGL ES 2.0之旅，主要针对于Android平台，会有一系列文章来分享学习OpenGL ES的总结。

主要编程语言将使用Kotlin，对于Kotlin还不熟悉的同学可以先看前面的[介绍](http://toughcoder.net/blog/2018/05/17/introduction-to-kotlin-programming-language/)和[实例](http://toughcoder.net/blog/2018/06/09/kotlin-exercise-programmer-calendar/)来快速的熟悉一下。

Android上面的OpenGL ES一共有三个版本，1.0，2.0以及现在的3.x(3.1, 3.2)，其中1.0是旧式的API，与桌面版本的OpenGL非常接近，但是却不太好用。从2.0开始，API有较大变化，具体的渲染相关使用专门的着色语言来表达
 矩阵的处理放到一个单独的类Matrix中，这样解耦后，学习起来和理解起来相对容易，API也不会依赖于具体的对象，直接使用static式的GLES20或者GLES30就好了。3.0是向后兼容的，它完全兼容2.0。所以，从2.0开始学习，是一个
 比较好的选择，而且2.0被Android 2.3以后的SDK支持，应该说目前所有的设备API上面都是支持OpenGL ES 2.0的（当然，具体的支持情况还看硬件GPU）。

为了方便，在此系列文章中，OpenGL，或者OpenGL ES或者GL，都是指OpenGL ES 2.0。

 关于平台，虽然我们是基于Android平台来学习，但是OpenGL是跨平台的，所有平台的GL的API（OpenGL, ES，或者WebGL，或者水果平台）长的都类似，方法名字，以及参数都差不多。虽然不可以直接使用，但是当作参考都没有问题。

## 开发环境搭建

首先是Android app的开发环境搭建，这个不多说了，大家自行Google。SDK版本最好高一点，至少要是5.0 (API 20)以上吧。

 其次是Kotlin语言的支持，如是是Android Studio 3.0以上的版本，自带支持，不用折腾。否则可以参考[官方网站的指导](https://kotlinlang.org/)。

 涉及到SDK相关的东西就是Activity，我们是有页面显示的，所以必须要有一个Activity，这个都懂得。主要是widget就是[android.oepngl.GLSurfaceView](https://developer.android.com/reference/android/opengl/GLSurfaceView)，
 以及[android.opengl.GLSurfaceView.Renderer](https://developer.android.com/reference/android/opengl/GLSurfaceView.Renderer)。GLSurfaceView是Android平台专门用于OpenGL绘制的组件，我们只需要创建一个
 实例，然后做一些基本的配置就好了，每个例子的配置都是很类似。重点就是要实现一个GLSurfaceView.Renderer，这个是OpenGL开发的重点。

### Step by step guide

首先，新建一个Android app项目，注意带上Kotlin支持，默认是钩上的。名字随意，比如叫EffectiveGL。

 然后，在项目新建一个空白Activity，不用钩选backward compat和创建layout，因为我们只用一个GLSurfaceView，用不着layout文件，另外，我们是用Kotlin，Kotlin是用Anko来用代码写布局。

 再有，在Activity里面，创建一个GLSurfaceView对象，然后当作Activity的布局。

 最后，实现一个Renderer接口，塞给GLSurfaceView，并对其做简单的配置。

 最终，一个准备好开发OpenGL的基本代码是这样子的，这些基础的准备工作，后面的示例中会略掉。

```kotlin
class HelloPoints : Activity() {
    private lateinit var glSurfaceView: GLSurfaceView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        title = "Play with Points"

        glSurfaceView = GLSurfaceView(this)
        setContentView(glSurfaceView)

        glSurfaceView.setEGLContextClientVersion(2)
        glSurfaceView.setRenderer(PointsRender)
        glSurfaceView.renderMode = GLSurfaceView.RENDERMODE_CONTINUOUSLY
    }

    override fun onResume() {
        super.onResume()
        glSurfaceView.onResume()
    }

    override fun onPause() {
        super.onPause()
        glSurfaceView.onPause()
    }

    companion object PointsRender : GLSurfaceView.Renderer {
        override fun onDrawFrame(p0: GL10?) {
        }

        override fun onSurfaceChanged(p0: GL10?, p1: Int, p2: Int) {
        }

        override fun onSurfaceCreated(p0: GL10?, p1: EGLConfig?) {
        }
    }
}
```

## 基础概念理解

有一些基础中的基础的概念需要理解一下，才能开始码代码。刚接触这么多概念，可能还没有理解它们，没有关系，先建立一个大概印象，随着学习的深入，就慢慢理解它们了。

### GL context

GL API的调用，虽然都是static形式的，没有限制，在哪里都能直接call，但是实际上它是有一个上下文环境的，叫GL context（目前阶段先这么叫着吧，不是太严谨哈）。这有点听不懂，用人话说，
 就是所有的GL API的调用都要在GLSurfaceView.Renderer的三个方法里面来call，就是方法的调用栈必须从这几个方法开始。在其他地方call是没有效果的：

 onSurfaceCreated

 onSurfaceChanged

 onDrawFrame

### GL的坐标系

OpenGL的坐标系是所谓的右手坐标系。

 



![img](https:////upload-images.jianshu.io/upload_images/324257-423f61fddb032f87.jpg?imageMogr2/auto-orient/strip|imageView2/2/w/690/format/webp)

右手坐标系

 首先它是三维的笛卡尔坐标系：原点在屏幕正中，x轴从屏幕左向右，最左是-1，最右是1；y轴从屏幕下向上，最下是-1，最上是1；z轴从屏幕里面向外，最里面是-1，最外面是1。



![img](https:////upload-images.jianshu.io/upload_images/324257-df5d4fb831562dce.jpg?imageMogr2/auto-orient/strip|imageView2/2/w/500/format/webp)

右手坐标系示意



### shader

GL ES 2.0与1.0版本最大的区别在于，把渲染相关的操作用一个专门的叫作着色语言的程序来表达，全名叫作[OpenGL ES Shading language](https://de.wikipedia.org/wiki/OpenGL_ES_Shading_Language)，它是一个编程语言，与C语言非常类似，能够直接操作矩阵和向量，运行在GPU之上
 专门用于图形渲染。它又分为两种，一个叫做顶点着色器（vertex shader），另一个叫做片元着色器（fragment shader）。前者用来指定几何形状的顶点；后者用于指定每个顶点的着色。
 每个GL程序必须要有一个vertex shader和一个fragment shader，且它们是相互对应的。（相互对应，意思是vertex shader必须要有一个fragment shader，反之亦然，但并不一定是一一对应）。当然，也是可以复用的，
 比如同一个vertex shader，可能会多个fragment shader来表达不同的着色方案。

### 坐标值和颜色值

坐标正常的取值范围都是-1到1，且是float类型。
 颜色值是0到1，也是float类型，0是空（无的意思，比如黑色，或者全透明），1是有（全的意思，比如白色，或者不透明），有些API是使用0～255，这时就需要转换一下。
 其实呢，写成超过此范围的值也是可以的，比如坐标传2，或者颜色写成5，OpenGL会处理成为它的合理的取值之内，用clamp的方式，超过的会被砍掉，如传5，相当于传1。

好了，准备工作差不多了，我们来撸代码吧。

## 年轻人的第一个OpenGL程序

我们的目标是画一个红色的点，就是这个样子的：
 



![img](https:////upload-images.jianshu.io/upload_images/324257-e3cfac98ea9af7d9.jpg?imageMogr2/auto-orient/strip|imageView2/2/w/690/format/webp)

画一红色的点



**注意**: 鉴于方便理解，我们暂时只做一些2D的渲染，也不调整view port，因为这会涉及比较复杂的Model View Projection矩阵的设置。

最终的代码就是这个样子的，重点看一下Renderer的实现，后面详细讲解：

```kotlin
const val TAG = "HelloPoints"

class HelloPoints : Activity() {
    private lateinit var glSurfaceView: GLSurfaceView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        title = "Play with Points"

        glSurfaceView = GLSurfaceView(this)
        setContentView(glSurfaceView)

        glSurfaceView.setEGLContextClientVersion(2)
        glSurfaceView.setRenderer(PointsRender)
        glSurfaceView.renderMode = GLSurfaceView.RENDERMODE_CONTINUOUSLY
    }

    override fun onResume() {
        super.onResume()
        glSurfaceView.onResume()
    }

    override fun onPause() {
        super.onPause()
        glSurfaceView.onPause()
    }

    companion object PointsRender : GLSurfaceView.Renderer {
        private const val VERTEX_SHADER =
                "void main() {\n" +
                        "gl_Position = vec4(0.0, 0.0, 0.0, 1.0);\n" +
                        "gl_PointSize = 20.0;\n" +
                        "}\n"
        private const val FRAGMENT_SHADER =
                "void main() {\n" +
                        "gl_FragColor = vec4(1., 0., 0.0, 1.0);\n" +
                        "}\n"
        private var mGLProgram: Int = -1

        override fun onDrawFrame(p0: GL10?) {
            GLES20.glClear(GLES20.GL_COLOR_BUFFER_BIT)
            GLES20.glUseProgram(mGLProgram)

            GLES20.glDrawArrays(GLES20.GL_POINTS, 0, 1)
        }

        override fun onSurfaceChanged(p0: GL10?, p1: Int, p2: Int) {
            GLES20.glViewport(0, 0, p1, p2)
        }

        override fun onSurfaceCreated(p0: GL10?, p1: EGLConfig?) {
            GLES20.glClearColor(0f, 0f, 0f, 1f)

            val vsh = GLES20.glCreateShader(GLES20.GL_VERTEX_SHADER)
            GLES20.glShaderSource(vsh, VERTEX_SHADER)
            GLES20.glCompileShader(vsh)

            val fsh = GLES20.glCreateShader(GLES20.GL_FRAGMENT_SHADER)
            GLES20.glShaderSource(fsh, FRAGMENT_SHADER)
            GLES20.glCompileShader(fsh)

            mGLProgram = GLES20.glCreateProgram()
            GLES20.glAttachShader(mGLProgram, vsh)
            GLES20.glAttachShader(mGLProgram, fsh)
            GLES20.glLinkProgram(mGLProgram)

            GLES20.glValidateProgram(mGLProgram)

            val status = IntArray(1)
            GLES20.glGetProgramiv(mGLProgram, GLES20.GL_VALIDATE_STATUS, status, 0)
            Log.d(TAG, "validate shader program: " + GLES20.glGetProgramInfoLog(mGLProgram))
        }
    }
}
```

## 示例代码讲解

### 基础设施

先来看一下Activity的onCreate/onResume和onPause这三个方法。先是在onCreate里面创建一个GLSurfaceView实例，设置为content view，因为我们要使用OpenGL ES 2.0，所以要setEGLContextClientVersion(2)。然后，再
 设置一个Renderer实例，渲染模式(render mode)分为两种，一个是GLSurfaceView主动刷新(continuously)，不停的回调Renderer的onDrawFrame，另外一种叫做被动刷新（when dirty），就是当请求刷新时才调一次onDrawFrame。

 这里我们用continuously的方式。
 

 至于onResume/onPause，API要求是要调用一下GLSurfaceView的onResume和onPause，照做就好，对于我们的示例来说，其实调与不调看不出区别。这只是影响离开Activity页面时的性能，我们学习初期，可以不予关注。

### Renderer之onSurfaceCreated

这个是最先被回调到的方法，告诉你系统层面，已经ready了，你可以开始做你的事情了。一般我们会在此方法里面做一些初始化工作，比如编译链接shader程序，初始化buffer等。我们一行一行的来分析：

```kotlin
GLES20.glClearColor(0f, 0f, 0f, 1f) // 参数顺序 r, g, b, a
```

这句是告诉OpenGL，给我把背景，或者叫作画布，画成黑色，不透明。比较绕人的说法是用参数指定的(r, g, b, a)这个颜色来初始化颜色缓冲区（color buffer）。目前就理解成为画面背景色就可以了。

接下来的这一坨是编译和链接shader程序：

```kotlin
val vsh = GLES20.glCreateShader(GLES20.GL_VERTEX_SHADER)
```

创建一个vertex shader程序，返回的是它的句柄，此返回值会用在后续操作的参数，所以，要用变量记录下来。

```kotlin
GLES20.glShaderSource(vsh, VERTEX_SHADER) // 告诉OpenGL，这一坨字串里面是vertex shader的源码。
GLES20.glCompileShader(vsh) // 编译vertex shader
```

接下来的三行，是编译fragment shader，跟vertex shader是一样的。
 然后是创建shader program并把shader链到上头去。同样的，先创建一个shader program句柄，后面要用，所以要记录一下，因为要在此方法外使用program句柄，所以要用全局变量来记录。

```kotlin
mGLProgram = GLES20.glCreateProgram() // 创建shader program句柄
GLES20.glAttachShader(mGLProgram, vsh) // 把vertex shader添加到program
GLES20.glAttachShader(mGLProgram, fsh) // 把fragment shader添加到program
GLES20.glLinkProgram(mGLProgram) // 做链接，可以理解为把两种shader进行融合，做好投入使用的最后准备工作
```

到此，其实shader program的准备工作已经做完了，但是如果shader编译或者链接过程出错了怎么办呢？能不能提早发现呢？当然，有办法检查一下，就是用接下来的这几句：

```kotlin
GLES20.glValidateProgram(mGLProgram) // 让OpenGL来验证一下我们的shader program，并获取验证的状态
val status = IntArray(1)
GLES20.glGetProgramiv(mGLProgram, GLES20.GL_VALIDATE_STATUS, status, 0) // 获取验证的状态
Log.d(TAG, "validate shader program: " + GLES20.glGetProgramInfoLog(mGLProgram))
```

如果有语法错误，编译错误，或者状态出错，这一步是能够检查出来的。如果一切正常，则取出来的status[0]为0。

### Renderer之onSurfaceChanged

此回调，会在surface发生改变时，通常是size发生变化。这里我们改变一下视角。

```kotlin
GLES20.glViewport(0, 0, p1, p2) // 参数是left, top, width, height
```

就是要指定OpenGL的可视区域(view port)，（0, 0）是左上角，然后是width和height。
 我们目前只学习2D绘制，所以，先不管三维视角的处理。

### Renderer之onDrawFrame

这个是最重要的方法，没有之一。前面两个，只会在surface created时调一次。而此方法是用来绘制每帧的，所以每次刷新都会被调一次，所有的绘制都发生在这里。

```kotlin
GLES20.glClear(GLES20.GL_COLOR_BUFFER_BIT) // 清除颜色缓冲区，因为我们要开始新一帧的绘制了，所以先清理，以免有脏数据。
GLES20.glUseProgram(mGLProgram) // 告诉OpenGL，使用我们在onSurfaceCreated里面准备好了的shader program来渲染
GLES20.glDrawArrays(GLES20.GL_POINTS, 0, 1) // 开始渲染，发送渲染点的指令， 第二个参数是offset，第三个参数是点的个数。目前只有一个点，所以是1。
```

### vertex shader

```kotlin
private const val VERTEX_SHADER =
                "void main() {\n" +
                        "gl_Position = vec4(0.0, 0.0, 0.0, 1.0);\n" +
                        "gl_PointSize = 20.0;\n" +
                        "}\n"
```

shader语言跟C语言很像，它有一个主函数，也叫void main(){}。

 gl_Position是一个内置变量，用于指定顶点，它是一个点，三维空间的点，所以用一个四维向量来赋值。vec4是四维向量的类型，vec4()是它的构造方法。等等，三维空间，不是（x, y, z）三个吗？咋用vec4呢？
 四维是叫做[齐次坐标](https://en.wikipedia.org/wiki/Homogeneous_coordinates)，它的几何意义仍是三维，先了解这么多，记得对于2D的话，第四位永远传1.0就可以了。这里，是指定原点(0, 0, 0)作为顶点，就是说想在原点位置画一个点。gl_PointSize是另外一个内置变量，用于指定点的大小。

 这个shader就是想在原点画一个尺寸为20的点。

### fragment shader

```kotlin
private const val FRAGMENT_SHADER =
                "void main() {\n" +
                        "gl_FragColor = vec4(1., 0., 0.0, 1.0);\n" +
                        "}\n"
```

gl_FragColor是fragment shader的内置变量，用于指定当前顶点的颜色，四个分量（r, g, b, a）。这里是想指定为红色，不透明。

## Fun time

更改一些参数，看看会发生什么:

1. 改变onSurfaceCreated中的glClearColor的颜色值
2. 改变gl_Position
3. 改变gl_PointSize
4. 改变gl_FragColor

## One more thing

此系列教程会共存在同一个Android app项目里面，所以我们会随着代码的增加而进行一系列的重构，但是这与我们的主题OpenGL无关，如果是单纯学习OpenGL，可以略过此节。

因为，每个教程会讲解不同的点，对Activity可能有不同的需求，所以，一个教程对应着一个Activity，这样就需要一个列表来作为路由目录页面：

```kotlin
class HomeActivity : Activity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        title = "Learn OpenGL ES Effectively"

        verticalLayout {
            textView("Welcome to the world of OpenGL ES") {
                gravity = Gravity.CENTER
            }.onClick { startActivity<HelloPoints>() }
        }
    }
}
```

## 参考资料

-  [《WebGL Programming Guide》](https://sites.google.com/site/webglbook/) 

   WebGL跟OpenGL ES 2.0相差无几，可以直接参考。这本书最大好处是讲解比较清晰，层次递进，代码完整，非常适合初学者上手。

-  [《OpenGL® ES 2.0 Programming Guide》](http://opengles-book.com/es2/index.html) 

   这本书比较啰嗦和枯燥，它更接近于规范，非常详尽严谨的讲述，但是讲解过少，示例也少。所以，它更适合于有一定基础，想要更深入的全面的理解某一概念时看，不适合入门。

   所以，这两本书加起来看效果最佳，先入门，理解基本概念，然后再通过后者全面理解，巩固加强。

