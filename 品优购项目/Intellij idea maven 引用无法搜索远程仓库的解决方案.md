# [Intellij idea maven 引用无法搜索远程仓库的解决方案](https://www.cnblogs.com/Bruce_H21/p/9875125.html)

~~~
<profiles>
    <profile>
        <id>dev</id>
        <repositories>
            <repository>
                <id>Nexus</id>
                <url>http://121.42.166.202:8081/nexus/content/groups/public</url>
                <releases>
                    <enabled>true</enabled>
                    <updatePolicy>always</updatePolicy>
                    <checksumPolicy>warn</checksumPolicy>
                </releases>
                <snapshots>
                    <enabled>true</enabled>
                    <updatePolicy>never</updatePolicy>
                    <checksumPolicy>fail</checksumPolicy>
                </snapshots>
            </repository>
        </repositories>
        <pluginRepositories>
            <pluginRepository>
                <id>Nexus</id>
                <url>http://121.42.166.202:8081/nexus/content/groups/public</url>
                <releases>
                    <enabled>true</enabled>
                    <checksumPolicy>warn</checksumPolicy>
                </releases>
                <snapshots>
                    <enabled>true</enabled>
                    <checksumPolicy>fail</checksumPolicy>
                </snapshots>
            </pluginRepository>
        </pluginRepositories>
        <!-- <properties> <environment.type>prod</environment.type> </properties> -->
    </profile>
~~~

