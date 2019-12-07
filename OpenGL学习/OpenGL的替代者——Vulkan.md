# OpenGL的替代者——Vulkan



Vulkan是一个跨平台的2D和3D绘图应用程序接口（API），最早由科纳斯(Khronos)组织在2015年游戏开发者大会（GDC）上发表。旨在替代OpenGL，提高图形性能。

## 基于OpenGL的图形引擎性能瓶颈

基于OpenGL的图形引擎，其渲染过程粗略可分为 主机端资源准备，设备端数据交互与管线准备 及 每帧循环的渲染 三个部分。 
![性能分析](https://img-blog.csdn.net/20161218165510403?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvanh0MTIzNGFuZDIwMTA=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

### 资源加载

这一过程跟GPU没有太大关系，主要是为了进行显示之前的图片解码、字体解析、3D模型解析等等。一般可以放到其他线程中执行，避免影响显示。

### 数据交互与管线准备

![Prepare](https://img-blog.csdn.net/20161219161347185?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvanh0MTIzNGFuZDIwMTA=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
这一过程主要是将必要的数据传到GPU可以读到内存中去，以及准备GPU的指令。 
1､纹理上传 
2､Shader的编译与Program的链接 
3､VBO的数据上传

### 每帧的图形渲染

![OpenGL_Origin](https://img-blog.csdn.net/20161218181133907?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvanh0MTIzNGFuZDIwMTA=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
1､数据交互耗时。 
这里主要需要设常量区的数据。我们绝大部分情况都是在绘制变化的物体，而变化相关的属性主要体现在常量区，因此每帧渲染都需要重新设一遍常量数据。 
2､调用Drawcall耗时。 
DrawCall指真正执行绘制任务的图形API，如glDrawArrays, glDrawElements。调用这些API时，GPU驱动需要产生GPU硬件所能识别的任务，并发送到内核，等待调度执行。

## Vulkan编程

关于Vulkan的详细使用参考这个Demo： 
<https://github.com/SaschaWillems/Vulkan>

Vulkan标准参考Khronos官网： 
<https://www.khronos.org/registry/vulkan/specs/1.0/refguide/Vulkan-1.0-web.pdf>

### 编程流程

基本的Vulkan编程流程： 
![Basic](https://img-blog.csdn.net/20161219170259868?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvanh0MTIzNGFuZDIwMTA=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
这个流程和OpenCL的使用流程很像，就是找到设备——创建上下文——创建命令队列——准备任务——发送执行。

Vulkan的窗口系统(WSI)（与EGL标准类似）： 
![Target](https://img-blog.csdn.net/20161219170423165?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvanh0MTIzNGFuZDIwMTA=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
注意到，在移动设备上使用OpenGL时，我们必须通过egl的API先准备好Surface和Context，而在Vulkan标准里面，WSI只是为Command Buffer 提供了 VkFrameBuffer，这个是图形渲染的输出。

### Pipeline

创建Command Buffer 的三个重要元素分别为 VkDescriptorSet（纹理和常量）、VkPipeline（着色器和状态）和VkBuffer（顶点数组）。 
官网上对Pipeline由下图描述： 
![Pipeline](https://img-blog.csdn.net/20161220000848034?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvanh0MTIzNGFuZDIwMTA=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

以前的GLProgram现在对应于一个VkPipeline，但VkPipeline除了Program之外，还覆盖了 blend，cull face 等状态： 
![VkPipeline](https://img-blog.csdn.net/20161220144309192?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvanh0MTIzNGFuZDIwMTA=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
Vulkan中的Shader只支持spv的标准二进制格式，我们所写的glsl都必须通过官方的一个转换器转换为二进制格式。这样做就不需要GPU驱动去做语法解析等编译前端工作了。

以前在OpenGL中用的Texture 现在由VkImage描述： 
![Texture](https://img-blog.csdn.net/20161220000832023?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvanh0MTIzNGFuZDIwMTA=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

### Command Buffer

一个用于图形渲染的 VkCommandBuffer 制作过程如下图： 
![CMD](https://img-blog.csdn.net/20161219171555875?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvanh0MTIzNGFuZDIwMTA=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
如图所示，Command Buffer 里面设定了图形渲染所需要的视口、裁剪、管线（各种状态配置和着色器）、顶点数组、描述（纹理、程序常量等）这些属性，之后再发送到命令队列(VkQueue)中就可以执行。

## Vulkan的优势

### 效率上的提升

Vulkan在效率上的提升主要是它天然支持多线程：

#### 异步数据交互

使用OpenGL时，如果把数据交互放到另一个独立线程中完成，将会引起冲突，这个原因是上传资源和进行绘制时都需要改变上下文： 
![Conflict](https://img-blog.csdn.net/20161220150917594?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvanh0MTIzNGFuZDIwMTA=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

用Vulkan则没有这个问题： 
![Texture](https://img-blog.csdn.net/20161220154310196?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvanh0MTIzNGFuZDIwMTA=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

#### 并行绘制

由于绘制时要改变上下文，OpenGL的并行绘制无疑也不可能了： 
![DrawConflict](https://img-blog.csdn.net/20161220151307279?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvanh0MTIzNGFuZDIwMTA=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

Vulkan可以并行创建Command Buffer，但由于Command Buffer 提交后就都是GPU驱动怎么执行的事了，执行的过程没必要也没可能用多线程加速。 
![Parallel](https://img-blog.csdn.net/20161220151553705?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvanh0MTIzNGFuZDIwMTA=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

#### 复用Command Buffer

OpenGL 每帧绘制时，都需要在驱动层重新建一个Command Buffer 传递下去，而 Vulkan 是在应用层建好 Command Buffer，每帧绘制时Sub上去。

### 便于模块化

虽然初看上去Vulkan比OpenGL复杂了许多，需要多写不少代码，但真正到软件开发时，由于Vulkan、OpenGL大部分情况都是用来写引擎，中间件的，维护代码的时间会远大于开发代码的时间，多写那几行代码根本不算啥。 
Vulkan更容易封装，各子模块之间互不影响，软件架构设计会轻松不少，开发维护起来更为方便。 
而基于OpenGL开发的各子模块之间总有各种各样因为状态机的缘故引发的Bug，比如： 
1､A模块用了VBO，B模块没有用，集成在一起时由于B模块没有把GL_ARRAY_BUFFER 重新绑定为0,出现段错误。 
2､A模块内部使用了FBO，使用FBO时重新设置了裁剪区域和视口大小，使用完成后没有恢复，导致集成之后，后续的模块绘制出现问题。 
如果基于Vulkan开发，上述的状态不一致的问题将会少很多。

当然，基于Vulkan开发的引擎一般会用多线程加速，这个也会有不少坑，但为了更好的性能，也是值得的。

## Vulkan对开发者的影响

OpenGL还算是对初学者比较友好的API，但到了Vulkan，由于严格把pipeline、descriptor、buffer分开，初学者上手难度变大了，App开发者直接调用图形API的情况将会减少，更多地会依赖于图形引擎。因此，Vulkan标准的渐渐普及会加速开发者的层级分划，使用Vulkan的人将是专业研究图形引擎或作GPGPU算法引擎的人。

对于有志于研究图形的初学者，可以直接学习Vulkan，不用去学习OpenGL了，Vulkan标准与GPU工作原理更为贴近，学习 Vulkan更有利于掌握图形显示的知识。