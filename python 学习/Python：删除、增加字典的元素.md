# [Python：删除、增加字典的元素](https://www.cnblogs.com/volcao/p/8695371.html)

### 一、增加一个或多个元素

- ```
  d = {'a': 1}
  ```

   

1. ```
   d.update(b=2)  #也可以 d.update({‘b’: 2})
   print(d)
   # {'a': 1, 'b': 2}
   ```

2. ```
   d.update(c=3, d=4)
   print(d)
   # {'a': 1, 'c': 3, 'b': 2, 'd': 4}
   ```

    

3. ```
   d['e'] = 5
   print(d)
   # {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
   ```

    

4. ```
   d.update({'f': 6, 'g': 7})  #即d.update(字典)
   print(d)
   # {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6}
   ```

    

 

### 二、删除一个或多个元素

- #### pop(key)

1. ```
   x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
   ```

   ```
   x.pop(1)   # pop(key)
   print(x)
   # {0: 0, 2: 1, 3: 4, 4: 3}
   ```

 

- #### del dict[key]

1. ```
   x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
   del x[1]
   print(x)
   # {0: 0, 2: 1, 3: 4, 4: 3}
   ```

 





# python中dict的打印

```
a=dict(a ='2',b ='3',c = '4')
print(dict)

for key,value in a.items():
    print(key,value)
```



# python dict的初始化

dict()                        # 创建空字典
{}

>>> dict(a='a', b='b', t='t')     # 传入关键字
>>> {'a': 'a', 'b': 'b', 't': 't'}
>>> dict(zip(['one', 'two', 'three'], [1, 2, 3]))   # 映射函数方式来构造字典
>>> {'three': 3, 'two': 2, 'one': 1} 
>>> dict([('one', 1), ('two', 2), ('three', 3)])    # 可迭代对象方式来构造字典
>>> {'three': 3, 'two': 2, 'one': 1}







# python对象存储 对象序列化

