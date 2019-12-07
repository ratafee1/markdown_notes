# linux查看进程ps -ef | grep redis

关闭redis

./redis-cli shutdown





# redis 五种数据类型

set key value

get key value

incr key

decr key



hset key field value

hset key field

hincrby key field num	#设置增数量





### list

list 是有顺序可重复（数据结构中的	双链表，队列）

lpush list1 a b c d

lrange list1 0 -1

rpush list1 e f g

lrange list1 0 -1

lpop list1

rpop list1



### set

无顺序 不能重复

sadd set1 a a a b c

smembers set1

srem set1 a



### zset(sorted set)

有顺序 不能重复

zadd zset1 1 a 2 b 3 c

zrange zset1 0 -1

zrange zset1 0 -1 withscores

zrevrange zset1 0 -1 

zincrby zset1 5 a

expire zset1 20

ttl zset1

persist zset1

del zset1

exists zset1



### redis持久化方案

rdb 快照形式（定期将当前时刻的数据保存磁盘中）会产生一个dump.rdb文件	特点：会存在数据丢失，性能较好，数据备份

aof append only file 所有对redis的操作命令纪录在aof文件中，恢复数据，重新执行一遍即可