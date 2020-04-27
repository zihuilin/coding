## OO思维：组合在一起的对象

现实世界中的事物是由各种部分组成的：

* 汽车有1个发动机和4个轮子
* 一个班级有60个学生

为了将对象组合在一起，可以将一些类作为另一个类的成员：

```java
public class Car {
	private String name;
	private Engine engine = null;
	private Tire[] tires = new Tire[4];
	
	public Car(String name) {
		this.name = name;
	}
	
	
	public void setEngine(Engine engine) {
		this.engine = engine;
	}
	
	public void setTires(Tire tire1, 
				Tire tire2, Tire tire3, Tire tire4) {
		tires[0] = tire1;
		tires[1] = tire2;
		tires[2] = tire3;
		tires[3] = tire4;
	}

	@Override
	public String toString() {
		return "这是个汽车，它名为" + name 
				+ ", 发动机使用的是" + engine 
				+ ", 四条轮胎分另是：" + Arrays.toString(tires) + "。";
	}
} 
```

这时getter和setter可以通过接收另一些类的对象，完成成员的管理：

```java
 	public void setEngine(Engine engine) {
		this.engine = engine;
	}
	
	public void setTires(Tire tire1, 
				Tire tire2, Tire tire3, Tire tire4) {
		tires[0] = tire1;
		tires[1] = tire2;
		tires[2] = tire3;
		tires[3] = tire4;
	}
```

作业：写一个班级(MyClass)，里面有无限多个学生，可以：

* 通过addStudent(Student stu);添加一个学生。
* 通过“学号”索引学生，比如getStudent("P2019090807")得到班里的学生。如果班里没有这个学生，返回NULL。
* 通过getStudentCount()返回班级里的学生数。