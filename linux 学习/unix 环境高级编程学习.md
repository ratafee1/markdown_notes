# unix 环境高级编程学习

## 第三章

文件描述符：所有打开的文件都通过文件描述符引用

文件描述符0:与标准输入关联

文件描述符1：与标准输出关联

文件描述符2：与标准错误关联

文件描述符的变化范围	0---OPEN_MAX-1





# 调用open或openat函数可以打开或创建一个文件



#include <fcntl.h>

int creat(const char *path, mode_t mode);



#include <unistd.h>

int close(int fd);



#include <unistd.h>

off_t lseek(int fd,off_t offset,int whence);	为打开文件设置偏移量

打开一个文件，除非指定O_APPEND，否则偏移量被设置为0

whence是SEEK_SET，该文件的偏移量设置为距文件开始处offset个字节

​		  SEEK_CUR，……			             当前值加offset

​		  SEEK_END，……				     文件长度加offset

返回：新的文件偏移量



od -c file.hole



#include <unistd.h>

ssize_t read(int fd, void *buf, size_t nbytes); 从打开文件中读数据

返回值：读到的字节数，到达文件尾，返回0；出错，返回-1



#include <unistd.h>

ssize_t write(int fd,const void *buf, size_t nbytes);	调用write函数向打开文件写数据

返回值：若成功，返回已写的字节数；出错，返回-1





## 3.10 文件共享

内核使用3种数据结构表示打开文件，他们之间的关系决定了在文件共享方面一个进程对另一个进程可能产生的影响



## 3.11原子操作

if (lseek(fd,OL,2) < 0 )

​	err_sys("lseek error");

if (write(fd,buf,100) !=100)

​	err_sys("write error");

#### 创建一个文件

if (  (fd = open  (pathname, O_WRONLY) ) <0 ){

​	if( errno == ENOENT){

​		if(   (FD = creat (path, mode) ) <0 )

​			err_sys("creat error");

​	else

​		err_sys("open error");

​	}

}



### 3.12 函数dup和dup2

下面两个函数都可用来复制一个现有的文件描述符

#include <unistd.h>

int dup(int fd);

int dup2(int fd,int fd2);	成功，返回新的文件描述符，出错返回-1



### 函数sync、fsync和fdatasysnc

#include <unistd.h>

int fsync(int fd);

int fdatasync(int fd);

void sync(void);



称为update的系统守护进程周期性地调用sync函数，定期冲洗内核的块缓冲区

fsync可用于数据库这样的应用程序，这种应用程序需要确保修改过的块立即写到磁盘上

fdatasync函数类似于fsync，它只影响文件的数据部分，除数据外，fsync还会同步更新文件的属性



### 3.14 函数fcntl

fcntl函数可以改变已经打开文件的属性

#include <fcntl.h>

int fcntl(int fd, int cmd, ……)

返回值：成功，依赖于cmd；出错，返回-1



#include "apue.h"

#include <fcntl.h>



void set_fl(int fd, int flags){

​	int val;

​	if( (val = fcntl(fd, F_GETFL,0)) <0  )

​		err_sys("fcntl F_GETFL error");

​	val |= flags;

​	if( fcntl(fd,F_SETFL, val) <0 )

​		err_sys("fcntl F_SETFL error");

}



### 函数ioctl

不能用本章中其他函数表示的I/O操作通常都能用ioctl表示

终端I/O是使用ioctl最多的地方

#include <unistd.h>

#include <sys/ioctl.h>

nt ioctl(init fd, int request,……)；

返回值：出错返回-1；成功，返回其他值





### /dev/fd



# 第四章



#include <sys/stat.h>

int stat(const char *restrict pathname, struct stat *restrict buf);返回与此命名文件有关的信息结构

int fstat(int fd, struct stat *buf);

int lstat(const char *restrict pathname,struct stat *restrict buf);

int fstatat(int fd,const char *restrict pathname,struct stat *restrict buf,int flag);



文件类型信息包含在stat结构的st_mode成员中。用宏确定文件类型，宏的参数都是stat结构中的st_mode成员

#include <sys/stat.h>

S_ISREG() 普通文件

S_ISDIR()目录文件

S_ISCHR()字符特殊文件

S_ISBLK()块特殊文件

S_ISFIFO()管道或FIFO

S_ISLNK()符号链接

S_ISSOCK()套接字		图4-1



#<sys/stat.h>		IPC类型宏

S_TYPEISMQ() 消息队列

S_TYPEISSEM() 信号量

S_TYPEISSHM()共享存储对象



## 设置用户ID和设置组ID

与一个进程相关联的ID有6个或更多

实际用户ID	实际组ID			有效用户ID 有效组ID 附属组ID 用于文件访问权限检查		保存的设置用户ID 保存的设置组ID 由exec函数保存

每个文件由一个所有者和组所有者，所有者由stat结构中的st_uid指定，组所有者则有st_gid指定



### 文件访问权限

### 新文件和目录的所有权

### 函数access和faccessat

#include <unistd.h>

int access(const char *pathname,int mode);

int faccessat(int fd,const char *pathname,int mode,int flag);

### 函数umask

#include <sys/stat.h>

mode_t umask(mode_t cmask);



## 函数chmod、fchmod和fchmodat

chmod、fchmod和fchmodat这3个函数使我们可以更改现有文件的访问权限

#include <sys/stat.h>

int chmod(const char *pathname,mode_t mode);

int fchmod(int fd,mode_t mode);

int fchmodat(int fd,const char *pathname,node_t mode,int flag);

返回值，成功返回0，出错返回1

### 黏着位

4.11 函数chown、fchown、fchownat和lchown

用于更改文件的用户ID和组ID，如果两个参数owner或group中的任意一个是-1，则对应的ID不变

下面几个chown函数用于更改文件的用户ID和组ID，如果两个参数owner或group中的任意一个是-1，则对应的ID不变j

#include <unistd.h>

int chown(const char *pathname, uid_t owner,gid_t group);

int fchown(int fd,uid_t owner,gid_t group);

int fchownat (int fd,const char *pathname, uid_t owner,gid_t group, int flag);

int lchown(const char *pathname,uid_t owner, gid_t group);



### 文件长度

### 文件中的空洞

### 文件截断

#include <unistd.h>

int truncate(const char *pathname,off_t length);

int ftruncate(int fd,off_t length);

### 文件系统

### 函数link、linkat、unlink、unlinkat和remove

#include <unistd.h>

int link(const char *existingpath,const char *newpath);

int linkat(int efd, const char *existingpath, int nfd, const char *newpath,int flag);



#include <unistd.h>

int unlink(const char *pathname);

int unlinkat(int fd,const char *pathname,int flag);



### 函数rename和renameat

#include <stdio.h>

int rename(const char *oldname, const char *newname);

int renameat(int oldfd, const char *oldname,int newfd, const char *newname);



### 符号链接

### 创建和读取符号链接

#include <unistd.h>

int symlink(const char *actualpath, const char *sympath);

int symlinkat(const char * actualpath,int fd,const char *sympath);

### 文件的时间

函数 futimens、utimensat和utimes

#include <sys/stat.h>

int futimens(int fd,const struct timespec times[2]);

int utimensat(int fd, const char *path, const struct timespec times[2], int flag);



#include <sys/time.h>

int utimes(const char *pathname,const struct timeval times[2]);

### 函数mkdir、mkdirat和rmdir

#include <sys/stat.h>

int mkdir(const char *pathname, mode_t mode);

int mkdirat(int fd, const char *pathname, mode_t mode);



## 第五章

流的定向决定了所读、写的字符是单字节还是多字节的，如若在未定向的流上使用一个多字节I/O函数（<wchar.h>）,则该流的定向设置为宽定向。若在未定向的流上使用单字节I/O函数，该流的定向设为字节定向。freopen函数清楚一个流的定向，fwide函数设置流的定向。

#include <stdio.h>

#include <wchar.h>

int fwide(FILE *fp,int mode);	宽定向返回正值，字节定向返回负值，未定向返回0			

mode参数为负，使指定的流是字节定向的，参数为正，使指定的流是宽定向的，参数值为0，不试图设置流的定向，返回标识该流定向的值。



### 标准输入、标准输出和标准错误

STDIN_FILENO、STDOUT_FILENO和STDERR_FILENO

这3个标准I/O流通过预定义文件指针stdin、stdout和stderr引用，定义在<stdio.h>中

### 缓冲

标准错误是不带缓冲的

若是指向终端设备的流，则是行缓冲的，否则是全缓冲的

下面两个函数更改缓冲类型

#include <stdio.h>

void setbuf(FILE *restrict fp,char *restrict buf);

int setvbuf(FILE *restrict fp,char *restrict buf,int mode,size_t size);

_IOFBF 全缓冲 _IOLBF行缓冲 _IONBF不带缓冲



#include<stdio.h>

int fflush(FILE *fp);



### 打开流

#include <stdio.h>

FILE *fopen(const char *restrict pathname, const char *restrict type);

FILE *freopen(const char *restrict pathname,const char *restrict type,FILE *restrict fp);

FILE *fdopen(int fd, const char *type);



fopen 打开路径名为pathname的指定的文件

freopen 在一个指定的流上打开指定的文件，如若该流已经打开，则先关闭该流，若该流已经定向，则使用freopen清除该定向。此函数一般用于将指定的文件打开为预定义的流，标准输入，标准输出或标准错误

fdopen函数取一个已有的文件描述符（open、dup、dup2、fcntl、pipe、socket、socketpair或accept函数得到此文件描述符），并使一个标准I/O流与该描述符相结合



type参数指定对该I/O流的读、写方式，ISO C规定type参数可以有15种不同的值，

type			说明							open标志

r或rb			为读而打开						O_RDONLY

w或wb			把文件截断至0长，或为写而创建	O_WRONLY|O_CREAT|O_TRUNC

a或ab			追加；为在文件尾写而打开，或为写而创建	O_WRONLY|O_CREAT|O_APPEND

r+或r+b或rb+	为读和写而打开					O_RDWR

w+或w+b或wb+	把文件截断至0长，或为读和写而打开	O_RDWR|O_CREAT|O_TRUNC

a+或a+b或ab+	为在文件尾读和写而打开或创建		O_RDWR|O_CREAT|O_APPEND



关闭流

#include <stdio.h>

int fclose(FILE *fp);



### 读和写流

每次一个字符的I/O

每次一行的I/O	fgets和fputs，没行都以一个换行符种植

直接I/O	fread和fwrite函数支持这种类型的I/O，每次I/O操作读或写某种数量的对象，而每个对象具有指定的长度

以下3个函数可用于一次读一个字符

#include <stdio.h>

int getc(FILE *fp);

int fgetc(FILE*fp);

int getchar(void);

getchar等同于getc（stdin）



#include <stdio.h>

int ferror(FILE *fp);

int feof(FILE *fp);

void clearerr(FILE *fp);

为每个流在FILE对象中维护了两个标志：

出错标志		文件结束标志		调用clearerr可以清楚这两个标志

从流中读取数据以后，可以调用ungetc将字符再压送回流中

#include <stdio.h>

int ungetc(int c,FILE *fp);

输出函数

#include <stdio.h>

int putc(init c,FILE *fp);

int fputc(int c, FILE *fp);

int putchar(int c);

putchar(c)等同于putc(c,stdout),putc可被实现为宏，而fputc不能实现为宏



### 每次一行I/O

#include <stdio.h>

char *fgets(char *restrict buf,int n, FILE *restrict fp);

char *gets(char *buf);



#include <stdio.h>

int fputs(const char *restrict str,FILE *restrict fp);

int puts(const char *str);



### 标准I/O的效率

### 二进制I/O

#include <stdio.h>

size_t fread(void *restrict ptr, size_t size, size_t nobj, FILE *restrict fp);

size_t fwrite(const void *restrict ptr, size_t size, size_t nobj, FILE *restrict fp);

读或写一个二进制数组	为了将一个浮点数组的第2-5个元素写至一个文件上，

float data[10];

if( fwirte(&data[2], sizeof(float),4,fp) != 4	)

​	err_sys("fwrite error");

struct{

​	short count;

​	long total;

​	char name[NAMESIZE];

}item;

if(fwrite(&item,sizeof(item),1,fp) != 1 )

​	err_sys("fwrite error");



### 定位流

#include <stdio.h>

long ftell(FILE *fp);		若成功返回当前文件位置指示

int fseek(FILE *FP, long offset, int whence);

void rewind(FILE *fp);



#include <stdio.h>

off_t ftello(FILE *fp);

int fseeko(FILE *fp, off_t offset, int whence);



#include <stdio.h>

int fgetpos(FILE *restrict fp, fpos_t *restrict pos);

int fsetpos(FILE *fp, const fpos_t *pos);



### 格式化I/O

#include <stdio.h>

int printf(const char *restrict format,……)；

int fprintf(FILE *restrict fp, const char *restrict format,……)；

int dprintf(int fd,const char *restrict format, ……)；

​			3个函数成功，返回输出字符数，输出出错，返回负值

int sprintf(char *restrict buf,const char *restrict format,……)；

​			返回存入数组的字符数

int snprintf(char *restrict buf, size_t n, const char *restrict format, ……)；

​			返回存入数组的字符数



printf将格式化数据写到标准输出，fprintf写至指定的流，dprintf写至指定的文件描述符

sprintf将格式化的字符送入数组buf中，sprintf在该数组的尾端自动加一个null字节



#include <stdarg.h>

#include <stdio.h>

int vprintf(const char *restrict format,va_list arg);

int vfprintf(FILE *restrict fp,const char *restrict format, va_list arg);

int vdprintf(int fd, const char *restrict format, va_list arg);

​			成功，返回输出字符数

int vsprintf(char *restrict buf, const char (restrict format, va_list arg));

​			返回存入数组的字符数

int vsnprintf(char *restrict buf, size_t n, const char *restrict format, va_list arg);

​			返回存入数组的字符数



格式化输入

#include <stdio.h>

int scanf(const char *restrict format, ……)；

int fscanf(FILE *restrict fp,const char *restrict format, ……)；

int sscanf(const char *restrict buf, const char *restrict format, ……)；

​			赋值的输入项，若输入出错或在任一转换前已到达文件尾端，返回EOF



#include <stdarg.h>

#include <stdio.h>

int vscanf(const char *restrict format, va_list arg);

int vfscanf(FILE *restrict fp,const char *restrict format,va_list arg);

int vsscanf(const char *restrict buf, const char *restrict format, va_list arg);



### 实现细节





# 第6章 系统数据文件和信息

#include <pwd.h>

struct passwd *getpwuid(uid_t uid);

struct passwd *getpwnam(const char *name);

两个获取口令文件项的函数



#include <pwd.h>

struct passwd *getpwent(void);

void setpwent(void);

void endpwent(void);

查看整个口令文件，getpwent返回口令文件中的下一个纪录项



访问阴影口令

#include <shadow.h>

struct spwd *getspnam(const char *name);

struct spwd *getspent(void);

void setspent(void);

void endspent(void);



### 6.4 组文件

#include <grp.h>

struct group *getgrgid(gid_t gid);

struct group *getgrnam(const char *name);



#include <grp.h>

struct group *getgrent(void);

void setgrent(void);

void endgrent(void);



### 6.5附属组ID

#include <unistd.h>

int getgroups(int gidsetsize, gid_t grouplist[]);



#include <grp.h>		/* on linux */

#include <unistd.h>	/* on freebsd, mac os x, and solaris */

int setgroups(int ngroups, const gid_t grouplist[]);

#include <grp.h>		/* on linux and solaris */

#include <unistd.h>	/* on freebsd and mac os x */

int initgroups(const char *username, gid_t basegid);



其他数据文件

说明		数据文件		头文件		结构		附加的键搜索函数

口令	/etc/passwd		<pwd.h>		passwd		getpwnam	getpwuid

组		/etc/group		<grp.h>		group		getgrnam	getgrgid

阴影	/etc/shadow		<shadow.h>	spwd		getspnam

主机	/etc/hosts		<netdb.h>	hostent		getnameinfo	getaddrinfo

网络	/etc/networks	<netdb.h>	netent		getnetbyname	getnetbyaddr

协议	/etc/protocols	<netdb.h>	protoent	Getprotobyname	getprotobynumber

服务	/etc/services		<netdb.h>	servent		getservbyname	getservbyport



### 6.8登录账户纪录

### 6.9系统标识

#include <sys/utsname.h>

int uname(struct utsname *name);

struct utsname{

​	char sysname[];

​	char nodename[];

​	char release[];

​	char version[];

​	char machine[];

};



#include <unistd.h>

int gethostname(char *name, int namelen);



### 6.10 时间和日期例程

返回当前日期和时间

#include <time.h>

time_t time(time_t *calptr);

获取指定时钟的时间

#include <sys/time.h>

int clock_gettime(clockid_t clock_id,struct timespec *tsp);

int clock_getres(clockid_t clock_id, struct timespec *tsp);

对特定的时钟设置时间

#include <sys/time.h>

int clock_settime(clockid_t clock_id, const struct timespec *tsp);



#include <sys/time.h>

int gettimeofday(struct timeval *restrict tp, void *restrict tzp);



#include <time.h>

struct tm *gmtime(const time_t *calptr);

struct tm *localtime(const time_t *calptr);



#include <time.h>

time_t mktime(struct tm *tmptr);



#include <time.h>

size_t strftime(char *restrict buf, size_t maxsize, const char *restrict format, const struct tm *restrict tmptr);

size_t strftime(char *restrict bur, size_t maxsize,const char *restrict format, const struct tm *restrict tmptr, locale_t locale);



字符串时间转换为分解时间

#include <time.h>

char *strptime(const char *restrict buf, const char *restrict format, struct tm *restrict tmptr);







# 第19章 伪终端













# 第20章 数据库函数库

#include "apue_db.h"

DBHANDLE db_open(const char *pathname, int oflag, …… /* int mode */);

void db_close(DBHANDLE db);



#include "apue_db.h"

int db_store (DBHANDLE db,const char *key, const char *data, int flag);

flag参数可以是DB_INSERT\DB_REPLACE或DB_STORE



#include "apue_db.h"

char *db_fetch(DBHANDLE db,const char *key);

若成功，返回指向数据的指针，没有找到纪录，返回NULL



#include "apue_db.h"

int db_delete (DBHANDLE db, const char *key);



#include "apue_db.h"

void db_rewind(DBHANDLE db);

char *db_nextrec(DBHANDLE db, char *key);

# 第21章 与网络打印机通信

