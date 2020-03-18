## 函数的return

函数调用后都将返回。

当返回值类型为void时，可以不明确写出return，这时整个函数体都将被执行。

```java
public static void main(String[] args){
	System.out.println( max(10, 5) );
}
```

明确写出return时，函数体将在return语句上结束执行。

```java
    public static void fun(int num){
        if (num < 0) {
            System.out.println("Hello, 小于0");
            return;
        }
        System.out.println("Hello, 大于或等于0");
    }
```

当返回值类型不为void时，函数体内必须要有return语句，并且return的数据类型必须和返回值类型一致。

```java
     public static int max(int param1, int param2){
        int result = 0;
        if (param1 > param2) {
            System.out.println("max is: " + param1);
            result = param1;
        }
        else {
            System.out.println("max is: " + param2);
            result = param2;
        }
        return result;
    }
```

注意当返回值类型不为void，函数体内的逻辑必须保证所有的分支都有相应的return。

```java
     public static int max(int param1, int param2){
        if (param1 > param2) {
            System.out.println("max is: " + param1);
            return param1;
        }
        else {
            System.out.println("max is: " + param2);
            return param2;
        }
    }
```

