一个完整的mapreduce程序在分布式运行时有三类实例进程：

1. MRAppMaster 负责整个程序的过程调度及状态协调
2. MapTask 负责map阶段的整个数据处理流程
3. ReduceTask 负责reduce阶段的整个数据处理流程



![image-20191215191130513](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191215191130513.png)



# 2. MapReduce 编程规范





![image-20191215192052325](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191215192052325.png)



7. 对多个 Map 任务的结果进行排序以及合并, 编写 Reduce 函数实现自己的逻辑, 对输入的
Key-Value 进行处理, 转为新的 Key-Value（K3和V3）输出
8. 设置 OutputFormat 处理并保存 Reduce 输出的 Key-Value 数据





![image-20191215194137098](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191215194137098.png)

![image-20191215194147194](C:\Users\app\AppData\Roaming\Typora\typora-user-images\image-20191215194147194.png)

# 6. MapReduce 排序和序列化



# MapReduce 中的计数器
计数器是收集作业统计信息的有效手段之一，用于质量控制或应用级统计。计数器还可辅助
诊断系统故障。如果需要将日志信息传输到 map 或 reduce 任务， 更好的方法通常是看能否
用一个计数器值来记录某一特定事件的发生。对于大型分布式作业而言，使用计数器更为方
便。除了因为获取计数器值比输出日志更方便，还有根据计数器值统计特定事件的发生次数
要比分析一堆日志文件容易得多。
hadoop内置计数器列表