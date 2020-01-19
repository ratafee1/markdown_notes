# Failed to execute goal org.apache.tomcat.maven:tomcat7-maven-plugin:2.2:run (default-cli) on project





### 解决办法：

开始以为是jdk或者tomcat版本的问题,试过几个版本没有解决，终于找到是由于dubbox依赖的servlet-api是spring不支持的
为dubbo的依赖排除servlet-apijar包。

```
<dependency>
	<groupId>com.alibaba</groupId>
	<artifactId>dubbo</artifactId>
	<version>2.8.4</version>
	<exclusions>
		<exclusion>
			<groupId>javax.servlet</groupId>
			<artifactId>javax.servlet-api</artifactId>
		</exclusion>
	</exclusions>	
</dependency>
```

