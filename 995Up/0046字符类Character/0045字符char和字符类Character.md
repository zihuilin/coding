## 字符类Character

### Character是char的包装类

Character类的实例可以表示一个字符。

```java
char c = 'a';
Character character = 'a';
```

练习创建四个字符类型的对象：J、a、v、a，并输出它们。

```java
//这样不行，会输出数字386
System.out.println(Character.toUpperCase(j) + a + v + a);

//这样才可以。
System.out.println(Character.toUpperCase(j));
System.out.println(a);
System.out.println(v);
System.out.println(a);
```

### Character类的操作

Character提供了一系列关于字符的操作。

比如，isDigit，compareTo，toUpperCase以及其它的操作等等。

```java
Character z = 'z';
Character a = 'a';
Character v = 'v';
Character two = '2';
System.out.println(a.compareTo(z));
		System.out.println(Character.isLetter(a));    //true
		System.out.println(Character.isLetter(two)); //false
		
		System.out.println(Character.isDigit(two)); //true
		System.out.println(Character.isDigit(a)); //false
```

练习：

1. 用户输入1个字符，若是字母，一律转换为大写；若是数字，一律输出其英文名。
2. 用户输入两个字符，对比它们的字典序的先后。
3. 用户输入一句英文，以句点‘.'结尾，输出其中26个字母各出现了多少次（不区分大小写）（作业）。

