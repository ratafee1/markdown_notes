# 从Maven资源库下载Jar包

~~~
call mvn -f pom.xml dependency:copy-dependencies
~~~

~~~
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>temp.download</groupId>
    <artifactId>temp-download</artifactId>
    <version>1.0-SNAPSHOT</version> 
    <dependencies>
    <!-- 将需要下载的jar包依赖关系粘贴到dependencies标签中 -->

    </dependencies>
</project>
~~~

