# idea中使用ant



Ant最初是为Java量身定做的工程构建工具，但因为其简单的XML语法和内置的任务，作为前端领域的构建工具也不失为一个明智的选择。关于Ant与前端，明河的教程有更详细的介绍：http://book.36ria.com/ant/index.html，对于Ant的常规使用方法，新手请直接学习明河的教程。下面来说说Intellij IDEA，它内置了Ant，如果你不喜欢命令行，那么在Intellij IDEA中使用Ant是非常方便的，本文主要介绍windows下在Intellij IDEA中使用Ant进行前端构建的方法，如果你使用其他操作系统，也可以参考。

**1、**首先，确保你的系统已经安装了Java运行环境，如果你的机子已经安装jdk，那么请跳过这一步，如果没有，请移步至http://willerce.com/post/jdk。参照此教程安装好jdk。

**2、**配置project structure。点击File>Project Structure(快捷键ctrl+alt+shift+s)，在Project SDK这一项中，如果显示的是“No SDK”，说明还木有设置运行环境，我们点击New，选择你的jdk安装目录，比如我的是C:\Program Files (x86)\Java\jdk1.6.0_10。设置好以后，会显示jdk的版本信息，如下图。



**3、**在你需要的地方写好build.xml配置文件，点右边栏的Ant Build标签（有个小蚂蚁的图标，看到没？），在弹出的Ant Build面板中点击+号，可以引入一个build.xml配置文件，你可以引入多个，点击-号可以删除选中的配置文件。引入配置文件之后，选中需要运行的任务，可以是Project，也可以是Target，再点击上面的播放按钮就可以Run了。比起命令行，是不是很直观呢？



**4、**现在我们来用下面这个build.xml作为栗子，运行看看结果如何。

~~~
<?xml version="1.0"?>
<project name="61" default="build">
 
    <!--基目录-->
    <dirname property="base.dir" file="${ant.file}"/>
 
    <!--css路径-->
    <property name="css.path" location="${base.dir}/css"/>
    <property name="css.dest" location="${base.dir}/build/css"/>
 
    <!--js路径-->
    <property name="js.path" location="${base.dir}/js"/>
    <property name="js.dest" location="${base.dir}/build/js"/>
 
    <!--YUI compressor路径-->
    <property name="yuicps.path" location="D:\Program Files\yui-compressor\yuicompressor.jar"/>
 
    <!--Closure compiler路径-->
    <property name="compiler.path" location="D:\Program Files\closure-compiler\compiler.jar"/>
 
    <target name="build" depends="min-css, min-js, copy">
        <echo>操作完成</echo>
    </target>
 
    <target name="min-css">
        <echo>开始使用YUI-Compressor压缩css</echo>
        <apply executable="java" dest="${css.dest}">
            <fileset dir="${css.path}" includes="*.css"/>
            <arg line="-jar"/>
            <arg path="${yuicps.path}"/>
            <arg line="--charset utf-8"/>
            <arg value="--type"/>
            <arg value="css"/>
            <arg value="-o"/>
            <targetfile/>
            <mapper type="glob" from="*.css" to="*-min.css"/>
        </apply>
    </target>
 
    <target name="min-js">
        <echo>开始使用Closure-Compiler压缩JS</echo>
        <apply executable="java" dest="${js.dest}">
            <fileset dir="${js.path}" includes="*.js"/>
            <arg line="-jar"/>
            <arg path="${compiler.path}"/>
            <arg value="--warning_level"/>
            <arg value="QUIET"/>
            <arg value="--js"/>
            <srcfile/>
            <arg value="--js_output_file"/>
            <targetfile/>
            <mapper type="regexp" from="^(.*[^-min])\.js$" to="\1-min.js"/>
        </apply>
    </target>
 
    <target name="copy">
        <echo>开始同步其他文件</echo>
        <copy overwrite="true" todir="${base.dir}/build">
            <fileset dir="${base.dir}" includes="*.html"/>
        </copy>
        <copy overwrite="true" todir="${base.dir}/build/img">
            <fileset dir="${base.dir}/img"/>
        </copy>
    </target>
 
</project>
~~~



**5、**在Message面板可以看到运行结果：3个target都顺利工作了。

这就是Intellij IDEA中Ant的基本用法，