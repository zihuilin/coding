## this关键字

之前已经将this用在引用某个对象的属性上：

```java
	String name;

	public ThisDemo(String name) {
		super();
		this.name = name; //引用对象的属性
    }
	public String whatsYourName() {
		return this.name; //引用对象的属性
	}
```

每次调用方法时，this指代的对象是可以不同的：

```java
		ThisDemo jack = new ThisDemo("Jack");
		ThisDemo rose = new ThisDemo("Rose");
		System.out.println(jack.whatsYourName());
		System.out.println(rose.whatsYourName());
```

另外，this还可以引用某个对象的方法：

```java
	public void sayHi() {
		System.out.println(this.whatsYourName() + " says Hi~~~");
	}
```

上面的情况下，也可以省略this.

```java
	public void sayHi() {
		System.out.println(whatsYourName() + " says Hi~~~");
	}
```

堂上练习：this关键字不能引用静态的属性和方法。为什么？

```java
	static int count = 0;
	public String whatsYourName() {
		int a = this.count; //会报“警告”：The static field ThisDemo.count should be accessed in a static way
		return name; //引用对象的属性
	}
```

this关键字还可以调用构造方法

(注意不可以递归调用构造方法，而且this调用构造方法必须写在第1行)

```java
	public ThisDemo() {
		this.name = "无名氏";
	}

	public ThisDemo(String name) {
		this(); //调用了上面的无参构造方法
		if (name != null)
			this.name = name; //引用对象的属性
    }
	public static void main(String[] args) {
		ThisDemo nobody = new ThisDemo(null);
		System.out.println(nobody.whatsYourName());
    }
```

练习：为学生类写一个只接收学号的构造方法，然后另外写：

* 一个接收学号和姓名的构造方法，并通过this调用只接收学号的构造方法
* 一个接收学号、姓名和年龄的构造方法，并通过this调用另外一个构造方法

总结一下，this可以：

* 在构造方法和非静态方法里调用非静态的属性和方法
* 在构造方法的第1行调用其它构造方法