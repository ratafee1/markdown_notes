

![image-20200106022253088](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20200106022253088.png)





# linux命令查看zookeeper状态

echo mntr[stat] | nc localhost 2181



# maven安装软件包

mvn install -Dmaven.test.skip=true





`CDH` 版本的所有工具都会遵循 `Linux` 的习惯放置 `Log` 和 `Data`, 所以需要先创建 `Zookeeper` 的数据目录, 并且所有者指定给 `Zookeeper` 所使用的用户, 如下命令在所有节点执行

```text
mkdir -p /var/lib/zookeeper
chown -R zookeeper /var/lib/zookeeper/
```



