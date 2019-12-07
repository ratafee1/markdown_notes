最近突然发现，maven的中央仓库下载pom文件失败，报错是Could not transfer artifact (https://repo.maven.apache.org/maven2): Received fatal alert: protocol_version -> [Help 1]，浏览器是能够访问的。

其实就是中央仓库必须要TLS1.2版本才能访问，貌似是今年六月份刚改的，所以有两种解决方法

 

第一种方法：将jdk版本升级到jdk1.8，因为在1.8及以上版本，才会默认使用TLS1.2

第二种方法(没有测试过):

maven的setting.xml设置为阿里云私服


<mirrors>
​	 <mirror>
​		<id>nexus-aliyun</id>
​		<mirrorOf>*</mirrorOf>
​		<name>Nexus aliyun</name>
​		<url>http://maven.aliyun.com/nexus/content/groups/public</url>
​	 </mirror>
</mirrors>

