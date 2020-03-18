## break和continue

break用来结束循环。也就是break后，立即中止并不再循环。

例：输入多个整数，计算它们的和，直到和超过100，最后输出它们的和。

```java
        Scanner input = new Scanner(System.in);
        int num = 0, sum = 0;
        do {
            num = input.nextInt();
            sum = sum + num;
            if (sum > 100)
                break;
        } while(true);
        System.out.println(sum);
```

continue用来中断当前的某次循环体的执行。continue后，视为当前循环体已完成，这时将再次判定循环条件，决定是否再次进入循环。

例：输入多个整数，计算**它们中的奇数**的和，直到和超过100，最后输出它们的和。

```java
        Scanner input = new Scanner(System.in);
        int num = 0, sum = 0;
        do {
            num = input.nextInt();
            if (num%2==0)
                continue;
            sum = sum + num;
            if (sum > 100)
                break;
        } while(true);
        System.out.println(sum);
```

