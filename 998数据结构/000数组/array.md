## 数组(线性表)

### 数组的特点

* 数组是一段连续的内存空间，在声明的时候不一定指定其长度（有几个元素）。
* 指定下标（索引），可以随机访问一个元素。

https://docs.python.org/3.7/library/stdtypes.html#sequence-types-list-tuple-range
https://docs.python.org/3/library/array.html
https://docs.oracle.com/javase/tutorial/java/nutsandbolts/arrays.html


## 2维数组的基本操作
https://snakify.org/en/lessons/two_dimensional_lists_arrays/
### 声明和元素操作
* 数组的声明，在同一行完成初始化
* 对任意一个元素进行操作：读值和写值

### 使用循环语句遍历数组,，打印每个元素为例
* python使用range()和len()，java使用size()

* 使用便利的迭代方式

  练习：声明一个数组，在其中放入1、2、……、99这99个数字：

  1. 计算，并输出所有元素的和
  2. 输出指定下标的元素，指定的下标是用户输入的。

  ```python
  lst = []
  
  for i in range(1,100):
      lst.append(i)
  
  sum = 0
  for i in range(len(lst)):
      sum += lst[i]
  
  print(sum)   #sum is 4950
  
  i = int(input())  # 输入一个下标
  print(lst[i]) 
  ```

  练习2：小美回家要上楼梯，她一次可以上一个台阶，也可以上两个台阶，小美会输入她回家要上几个台阶（1到100之间），你告诉她可以有多少种走法？

  ```python
  lst = []
  
  lst.append(1) # 第一级台阶有1种走法
  lst.append(2) # 第二级台阶有2种走法
  
  for n in range(2, 100):
      lst.append(lst[n-1] + lst[n-2])
  
  i = int(input())
  print(lst[i-1])
  ```

  

### 创建2维数组
* python: 不可以使用 a = [[0]*m]*n, 应该一行一行的创建List
* java 比较简单： int [][] a = new int[N][M] 就可以声明并创建一个N行M列的数组

2维数组进行矩阵计算

### 多维数组









