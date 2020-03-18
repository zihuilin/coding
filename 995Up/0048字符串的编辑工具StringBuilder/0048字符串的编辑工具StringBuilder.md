## 字符串的编辑工具StringBuilder

StringBuilder是一个高效的字符串编辑工具。

### StringBuilder的构造方法

```java
 
```

### StringBuilder对字符串的编辑方法

一般来说，编辑无非就是“增删查改”四种常见操作。通过查看官方的StringBuilder文档，可以找出这四种操作的方法。

```java
//增

//删

//查

//改

```

练习：在有下面一段英文字符串的基础上，进行编辑：

```java
String str = "You are big, I am big too. You are tall, I am short too. You are Hot, I am cool. You are bad, I am good.";
// 1. 在所有 are 和 am 后面加上very

// 2. 把第3个I am 换为 He is

// 3. 把第2个too删除

// 4. 在最开关加入： "Read after me: "

```



### StringBuilder的其它方法



```java
 
```



### 高效的编辑工具

程序里如果需要做大量关于字符串的编辑，StringBuilder会比直接用String的操作要高效得多（为什么）。