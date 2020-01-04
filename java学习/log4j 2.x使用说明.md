# log4j 2.x使用说明

添加配置 log4j.xml

~~~
<?xml version="1.0" encoding="UTF-8"?>

<Configuration status="info">
    <Appenders>
        <Console name="Console" target="SYSTEM_OUT">
            <PatternLayout pattern="%m%n" />
        </Console>
        <File name="log" fileName="log/graph.log" append="false">  
            <PatternLayout pattern="%d{yyyy.MM.dd HH:mm:ss} %5p %C %M %m%n"/>  
        </File>  
    </Appenders>
    <Loggers>
        <Root level="INFO">
            <AppenderRef ref="Console" />
            <AppenderRef ref="log" />
        </Root>
    </Loggers>
</Configuration>
~~~



log4j.properties

~~~
log4j.rootLogger=DEBUG, CA

log4j.appender.CA=org.apache.log4j.ConsoleAppender

log4j.appender.CA.layout=org.apache.log4j.PatternLayout
log4j.appender.CA.layout.ConversionPattern=%-4r [%t] %-5p %c %x - %m%n
~~~

