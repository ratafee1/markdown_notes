# pcre编译安装



1.下载地址<https://sourceforge.net/projects/pcre/files/pcre/8.42/pcre-8.42.tar.gz/download>

```
#wget https://sourceforge.net/projects/pcre/files/pcre/8.42/pcre-8.42.tar.gz/download
```

2.解压安装

```
#tar -zxvf pcre-8.42.tar.gz
```

3.编译安装

```
#cd pcre-8.42

#./configure 
#make && make install
```

4.查看pcre版本

```
# pcre-config --version
```

