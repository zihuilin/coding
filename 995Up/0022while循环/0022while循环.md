## while循环

顺序、分支、循环，是三大基本流程结构。

循环是指：当满足某个条件时，不断执行一段代码的逻辑。

比如：计算所有输入的整数之和，直到输入的整数为0。

```java
Scanner input = new Scanner(System.in);
int num = input.nextInt();
int sum = 0;
while(num != 0) {
	sum = sum + num;
	num = input.nextInt();
}
System.out.println(sum);
```

再比如：输入一个正整数N，输出1到N 之间的所有整数。

```java
Scanner input = new Scanner(System.in);
int n = input.nextInt();
int i = 1; //循环变量
while(i <= n) { //循环条件
//循环体
	System.out.println(i);
	i = i + 1;
}
```

while后面( )里的为循环条件，{ }里的为循环体。

通常将控制循环是否继续的变量，称为循环变量。

* 循环变量通常在循环开始前就声明并初始化；
* 只有循环条件为true，才会执行循环体；
* 循环变量通常会在循环体中发生改变；
* 当循环变量的变化使得循环条件不再满足时，循环结束。

