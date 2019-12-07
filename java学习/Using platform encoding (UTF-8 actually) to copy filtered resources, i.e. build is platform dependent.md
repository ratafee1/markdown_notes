# [Using platform encoding (UTF-8 actually) to copy filtered resources, i.e. build is platform dependent](https://www.cnblogs.com/qiumingcheng/p/5855513.html)



修改pom.xml文件，添加以下属性

 

 

[view plain](http://www.programgo.com/article/53393496600/#)

1. <project>  
2.   ...  
3.   <properties>  
4. ​    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>  
5.   </properties>  
6.   ...  
7. </project>  