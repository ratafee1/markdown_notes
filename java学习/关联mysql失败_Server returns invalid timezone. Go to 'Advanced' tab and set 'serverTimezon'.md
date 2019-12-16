# [关联mysql失败_Server returns invalid timezone. Go to 'Advanced' tab and set 'serverTimezon'](https://www.cnblogs.com/sunchunmei/p/11426758.html)



时区错误，MySQL默认的时区是UTC时区，比北京时间晚`8`个小时。

所以要修改mysql的时长

在mysql的命令模式下，输入：

set global time_zone='+8:00';

再次连接成功

