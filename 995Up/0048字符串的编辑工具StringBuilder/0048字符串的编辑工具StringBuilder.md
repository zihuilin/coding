## 字符串的编辑工具StringBuilder

StringBuilder是一个高效的字符串编辑工具。

capacity: 容量大小

length: 内容的长度

### StringBuilder的构造方法

```java
StringBuilder sb = new StringBuilder();
StringBuilder sb = new StringBuilder("opqrst");
```

### StringBuilder对字符串的编辑方法

一般来说，编辑无非就是“增删查改”四种常见操作。通过查看官方的StringBuilder文档，可以找出这四种操作的方法。

```java
//增
int i = 575859;
sb.append(i); //增加一个整数
sb.insert(3, i);  //将整数i插入到下标为3的位置上
System.out.println(sb);

//删
		//delete会从start开始，删除（end - start)个字符
//因此start等于end，delete就不会有任何操作
//官方文档：删除start到end-1位置上的字符
sb.delete(2, 5); //删除“q57”
System.out.println(sb);

//查
//和String一样的indexOf
//和String一样的substring

//改
//修改位置1到3的内容为abc
//start到end-1的长度和替换的内容的长度可以不同
//也就是说，可以替换为更长或更短的内容。
sb.replace(1, 4, "ab");
System.out.println(sb);
```

练习：在有下面一段英文字符串的基础上，用StringBuilder进行编辑：

```java
		StringBuilder sb = new StringBuilder(
				"You are big, I am big too. You are tall, I am short too. You are Hot, I am cool. You are bad, I am good.");

		// 1. 在所有 are 和 am 后面加上very
		// 找出所有的"are"
		int location = -1;
		while (true) { // 不断找are的位置
			location = sb.indexOf("are", location + 1);
			if (location == -1)
				break;
			else
				sb.insert(location + 3, " very"); //加入very
		}
		System.out.println(sb);

		// 找出所有的"am"
		location = -1;
		while (true) { // 不断找am的位置
			location = sb.indexOf("am", location + 1);
			if (location == -1)
				break;
			else
				sb.insert(location + 2, " very");
		}
		System.out.println(sb);
		
		// 2. 把第3个I am 换为 He is
		location = -1;
		for (int i=0;i <3; i++) {
			location = sb.indexOf("I am", location + 1);
		}
		if (location != -1)
			sb.replace(location, location + 4, "He is");
		System.out.println(sb);
		
		// 3. 把第2个too删除
		location = -1;
		for (int i=0;i <2; i++) {
			location = sb.indexOf("too", location + 1);
		}
		if (location != -1)
			sb.delete(location, location + 4);
		System.out.println(sb);
		
		// 4. 在最开始位置加入： "Read after me: "
		sb.insert(0, "Read after me: ");
		System.out.println(sb);
```



### StringBuilder的其它方法

将字符串反转：如“abcd"--> "dcba"

直接设置字符串的长度：setLength

```java
StringBuilder sb2 = new StringBuilder("abcd");
sb2.reverse(); //反转
System.out.println(sb2);

sb.setLength(5); //设置长度为5,原来内容里从6开始的字符就删除了。
System.out.println(sb);
sb.setLength(15); //再次设置为15,原来后面的内容也回不来。
System.out.println(sb);
```

### 高效的编辑工具

程序里如果需要做大量关于字符串的编辑，StringBuilder会比直接用String的操作要高效得多（为什么）。