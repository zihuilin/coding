## OO思维：不能在外部构造对象的类

为什么不让外部构造对象？

因为我们想控制对象的构造，不愿意随便构造。

如何做：

（1）构造对象要调用构造方法，为了不让外部构造对象，要让构造方法“不可见”：

```java
public class Manager {
	
	private String name;

    //私有的构造方法
	private Manager(String name) {
		super();
		this.name = name;
	}
}
```

（2）对象只能在类的内部构造：

```java
	public static Manager getManager() {
		return new Manager("nobody");
	}

```

（3）外部得到构造好的对象：

```java
 	public static void main(String[] args) {
		Manager someManager = Manager.getManager();
		someManager.setName("Jack");
		System.out.println(someManager);
	}
```

（4）如果要让Manager对象是唯一的：

```Java
	private static Manager theManager = null;
	public static Manager getManager() {
		if (theManager == null) //保证只new一次
			theManager = new Manager("nobody");
		return theManager;
	}
```

练习：老板说，试用版本的程序只能管理6个机器，当用户购买了软件以后，再发可以管理60个机器的版本。如何修改Machine类，实现这个需求？

