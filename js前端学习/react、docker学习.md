# react学习	runnoob

# docker学习	itcast



![image-20191208135103372](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191208135103372.png)



![image-20191208135405572](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191208135405572.png)

### 拉取镜像	docker pull centos

### 查询镜像	docker search tomcat

### 删除镜像	docker rmi 镜像名称或者id	名称

### 查看正在运行的容器	docker ps

### 退出交互式容器	exit

###	 列出所有容器状态	docker ps -a

### 容器启动与停止	docker start/stop	c1



![image-20191208161901385](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191208161901385.png)

### 创建守护式容器	docker run -itd	--name c2 centos /bin/bash

### 查看容器的详细信息	docker inspect c3

###	查看容器的ip地址	docker inspect -f/--format=‘{{\.NetworkSettings.IPAddress}}’ c3

### 删除所有容器	docker rm \`docker ps -a -q\`

### 查看容器日志	docker logs 容器/id

### 文件拷贝	docker cp 1.txt c2:2.txt	docker cp c2:/root/2.txt /root

### 目录挂载	docker run -itd --name c2 -v /opt:/usr/local/mythml  centos /bin/bash





### 制作docker镜像	方式一docker	commit	方式二docker	build和Dockerfile文件

### docker commit mycentos mytomcat

### 端口映射



### 镜像打包	docker save -o /root/tomcat.tar mytomcat

### scp tomcat7.tar	其他服务器ip:/root	导入镜像docker load -i /root/tomcat7.tar

### 容器打包	docker export -o /root/t1.tar t1	导入容器docker import t1.tar mytomcat:latest



![image-20191208190037415](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191208190037415.png)

### Dockerfile方式创建镜像

1.创建一个目录：/usr/local/rw_test

2.编辑Dockerfile文件，vim Dockerfile

3.编辑内容如下

~~~
#pull down centos image
FROM docker.io/centos
MAINTAINER ruanwen onlien033_login@126.com

#install nginx
RUN yum install -y pcre pcre-devel openssl openssl-devel gcc gcc+ wget vim net-tools
RUN useradd www -M -s /sbin/nologin
RUN cd /usr/local/src && wget http://nginx.org/download/nginx-1.8.0.tar.gz && tar -zxvf nginx-1.8.0.tar.gz
RUN cd /usr/local/src/nginx-1.8.0 && ./configure --prefix=/usr/local/nginx --user=www --group=www --with-http_stub_status_module --with-http_ssl
_module && make && make install
ENTRYPOINT /usr/local/nginx/sbin/nginx && tail -f /usr/local/nginx/logs/access.log

~~~

4.在rw_test目录下构建镜像

docker build -t rw_nginx --rm=true .

-t	表示选择指定生成镜像的用户名，仓库名和tag

--rm=true	表示指定在生成镜像过程中删除中间产生的临时容器

.	表示使用当前目录下的Dockerfile构建镜像

5.测试	docker run -it -d --name test_nginx -p 8899:80 rw_nginx /bin/bash

docker exec test_nginx /bin/bash

通过浏览器访问：http://ip:8899



### docker仓库	dockerhub	阿里云	自己搭建私有仓库

### 设置镜像标签	docker tag local-image:tagname	new-repo:tagname

eg:docker tag hello-world:latest	ratafee/test-hello-world:v1

### 登录docker hub	docker login

### 推送镜像	docker push new-repo:tagname

eg:docker push ratafee/test-hello-world:v1

### 搭建私有仓库	使用Docker官方提供的Registry镜像就可以搭建本地私有镜像仓库

~~~
docker run -d \
-p 5000:5000 \
--restart=always \
--name registry \
-v /mnt/registry:/var/lib/registry \
registry:2		
//容器销毁后，在/var/lib/registry目录下的数据自动备份到宿主机指定目录

--restart=always:表示容器启动后自动启动本地私有镜像仓库
~~~





### docker网络管理

###	docker network ls

### 在Docker Swarm集群环境下，提供了docker_gwbridge和ingress两种默认网络

### docker network inspect bridge

### 创建新的网络	docker network create --driver bridge isolated_nw	

### docker run -itd --name=nwtest --network=isolated_nw busybox

### docker network connect/disconnect bridge nwtest	//	添加/移除网络

### docker network rm isolated_nw

### docker attach c1



### docker swarm集群

### docker compose编排工具 .yml .yaml



### docker 可视化工具

