## 字符串String类及其操作

### String对象的初始化

String的常量：用双引号表示

String类型的对象的初始化：构造方法、常量、字符数组……

```java
		String str1 = "abc";
		char[] chars = {'a', 'b','c'};
		String str2 = new String(chars); //创建出另一个String对象
		String str3 = new String(str1);  //创建出第三个String对象
		
		if (str1 == "abc")
			System.out.println("str1 == \"abc\"");
		else
			System.out.println("str1 != \"abc\"");
		
		System.out.println(str2);
		
		if (str2 == "abc")
			System.out.println("str2 == \"abc\"");
		else
			System.out.println("str2 != \"abc\"");
		
		System.out.println(str3);
		
		if (str3 == "abc")
			System.out.println("str3 == \"abc\"");
		else
			System.out.println("str3 != \"abc\"");
		
		System.out.println(str1.equals(str2));
		System.out.println(str2.equals(str3));
```



作业： 哪个String的操作可以通过字符串获得字符数组？

### String对象是不能改变的

String类型的变量引用的String对象是不能改变的。改变的只是引用。

赋值和传参的时候可能出现的“意外”：

```java
 		String str1 = "abc";
		String str2 = str1; //str2引用了str1引用的String对象
		
		if(str2==str1)
			System.out.println("str2和str1是同一个对象");
		else
			System.out.println("str2和str1不是同一个对象");
		
		str1 = str1 + "d";
		
		System.out.println("经过修改后……");
		
		if(str2==str1)
			System.out.println("str2和str1是同一个对象");
		else
			System.out.println("str2和str1不是同一个对象");
		
		System.out.println("str1: " + str1);
		System.out.println("str2: " + str2);
```

练习：

1. 将Student作为参数，传入一个方法，修改Student对象的内容，然后在方法之外，验证Student对象有没有变化；
2. 将String作为参数，传入一个方法，修改String对象的内容，然后在方法之外，验证String对象有没有变化；

### String对象的比较

长度是否相同：length方法

是否为同一个对象：==

```java
		String str1 = "abc";
		String str2 = "abc";
		
		//判断str1和str2是不是同一个对象
		if (str1 == str2) { //验证两个变量引用的是不是同一个对象
			System.out.println("str1和str2是同一个对象");
		} else
			System.out.println("str1和str2不是同一个对象");
```

```java
		//每次构造方法都会产生一个新的对象
		String str1 = new String("abc");;
		String str2 = new String("abc");
		
		//判断str1和str2是不是同一个对象
		if (str1 == str2) { //验证两个变量引用的是不是同一个对象
			System.out.println("str1和str2是同一个对象");
		} else
			System.out.println("str1和str2不是同一个对象");
```

是否内容相同：equals方法

```java
		//每次构造方法都会产生一个新的对象
		String str1 = new String("abc");;
		String str2 = new String("abc");
		
		//判断str1和str2是不是同一个对象
		if (str1.equals(str2)) { //验证两个对象的内容是不是相同
			System.out.println("str1和str2内容相同");
		} else
			System.out.println("str1和str2内容不相同");
```

字典序比较：compareTo方法

```java
		//比较str1和str2的字典序
		//返回负数说明str1是先于str2在字典里出现
		System.out.println(str1.compareTo(str2));
```



其它方法：startsWith, endsWith, matches

```java
 		String str1 = "student";
		
		System.out.println(str1.startsWith("stu"));
		
		String studentID = "P2019070869";
		
		if (studentID.startsWith("P2019")) {
			System.out.println("这是个大一学生");
		} else {
			System.out.println("这不是个大一学生");
		}
```

```java
	public static boolean isMobiPhoneNum(String telNum){
		String regex = "^((13[0-9])|(15[0-9])|(18[0-9]))\\d{8}$";
        Pattern p = Pattern.compile(regex,Pattern.CASE_INSENSITIVE);
        Matcher m = p.matcher(telNum);
        return m.matches();
	}

```

```java
		String fileName = "My Student001.jpg";
		//匹配文件名中间有Student的jpg文件：
		System.out.println(fileName.matches("(.*)Student(.*)jpg"));
```

练习：验证一个字符串是不是以"ed"结尾，比如：“lowered"

### String的子串

寻找子串的位置：indexOf

返回某位置上的子串：subString

返回某位置上的字符：charAt

```java
		String str = "abc123";
		String subStr = "123"; //要找的子串
	
		/**
		 * abc123
		 * 012345   <---位置
		 * 因此123是在3号位置开始的
		 */
		//在str里找subStr的位置
		System.out.println(str.indexOf(subStr)); //返回的是3号位置
		
		//返回某位置上的子串：subString
		System.out.println(str.substring(3)); //得到从3号位置开始的子串
		
		//只要从3号位置开始的2个字符：
		System.out.println(str.substring(3, 3+2));
		int i = 2;
		//得到从i开始的4个字符：
		System.out.println(str.substring(i, i+4));
		
		//得到某位置上的字符： charAt
		System.out.println(str.charAt(3));
```

练习：

1. 判断某个字符串里是不是只有1个@，而且@前后必须都有其它字符，比如”zihui.lin@163.com" --> true，"zihui.lin@163@.com" -->false,  "zihui.lin163.com" -->false

2. 得到一个电子邮箱的服务器地址部分："zihui.lin@163.com" -->得到163.com, "56510666@qq.com" --> qq.com

### String的匹配替换

有两个常用的方法：

1. replaceAll可以替换所有子串为另一个字符串,

   ```java
   String str = "zihui.lin@163.com";
   String str2 = str.replaceAll("@", ""); //删除所有@
   //只有一个@
   System.out.println((str.length() - str2.length()) == 1);
   ```

   

2. split按给定的子串，将原字符串分成多个字符串

   ```java
   String str = "zihui.lin@163.com";
   String[] strs = str.split("@");
   
   System.out.println(strs.length); //2 :只有1个@
   ```

   ```java
   String str = "i am a boy";
   String[] strs = str.split(" ");
   		
   System.out.println(strs.length); //4 :有4个单词
   ```

   练习：输入一段英文，统计其中有多少个句子，并输出每个句子

   注：每个英文句子以英文的句点：.

   ```
   		//输入一段英文，统计其中有多少个句子，并输出每个句子
   		String p = "I'm jack. I'm 18 years old. I'm a student.";
   		//因为 '.' 在正则表达式中通配单个字符， 因此要匹配真正的“.”要加\\ 
   		String[] sens = p.split("\\."); 
   		System.out.println(sens.length); //3，因为有3个句子
   		for (String s : sens) {
   			//trim可以去掉前后的空格
   			System.out.println(s.trim() + "."); 
   		}
   		
   ```

作业：

输入一段用空格隔开的单词，

1. 统计其中有多少个不重复的单词，
2. 每个单词出现了多少次。

比如： “I am a boy I live in jiangmen i am 18 years old"

提示：使用split，使用到isDigit，

### String和其它数据的转换

众多的valueOf方法将数据转换为String对象。format方法还可以格式化数据。

```java
 
```

众多的Wrapper类提供parse方法将String对象转换为其它类型的数据。

```java
 
```

