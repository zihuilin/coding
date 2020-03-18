## 字符串String类及其操作

### String对象的初始化

String的常量：用双引号表示

String类型的对象的初始化：构造方法、常量、字符数组……

```java
 
```



堂上练习： 哪个String的操作可以将字符串对象获得字符数组？

### String对象是不能改变的

String类型的变量引用的String对象是不能改变的。改变的只是引用。

赋值和传参的时候可能出现的“意外”：

```java
 
```



### String对象的比较

长度是否相同：length方法

是否为同一个对象：==

是否内容相同：equals方法

字典序比较：compareTo方法

其它方法：startsWith, endsWith, matches

```java
 
```



堂上练习：对比两个字符串的内容

### String的子串

寻找子串的位置：indexOf

返回某位置上的子串：subString

返回某位置上的字符：charAt

```java
 
```



### String和其它数据的转换

众多的valueOf方法将数据转换为String对象。format方法还可以格式化数据。

```java
 
```

众多的Wrapper类提供parse方法将String对象转换为其它类型的数据。

```java
 
```

