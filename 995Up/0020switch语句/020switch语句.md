## switch语句

### 根据某个状态码/类型码，执行不同的逻辑。

```java
int status = 2;
if (status == 0){
	System.out.println("status is 0");
} else if (status == 1){
	System.out.println("status is 1");
} else if (status == 2){
	System.out.println("status is 2");
} else if (status == 3){
	System.out.println("status is 3");
} else {    
	System.out.println("status is is not listed");    
}
```

```java
int status = 2;                          
switch(status){                          
	case 0:                                           
		System.out.println("Status is 0");
		break;
	case 1:
		System.out.println("Status is 1");
		break;
	case 2:
		System.out.println("Status is 2");
		break;
	case 3:
		System.out.println("Status is 3");
		break;
	default:
		System.out.println("Status is not listed");
 }
```

上面的if语句和switch语句实现的逻辑相同。

switch语句的作用就是根据给定的状态码，依次判断哪个case与其相同，并执行其中的逻辑。switch的用法如下：

* switch的状态码可以是char、byte、short和int类型之一；
* case里的常量的数据类型必须和switch的状态码相同；
* break不是必须的，如果没有break，将继续执行一下个case中的逻辑；
* defualt是可选的，default中的逻辑将在没有任一case匹配时执行；

因为经常会忘记写break，导致程序出现逻辑错误，一般情况下不建议使用swtich。