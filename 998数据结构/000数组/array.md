## 数组的特点
* 数组是一段连续的内存空间，在声明的时候必须指定其长度（有几个元素）。
* 指定下标（索引），可以随机访问一个元素。
* 本身并不知道自己的长度

https://docs.python.org/3.7/library/stdtypes.html#sequence-types-list-tuple-range
https://docs.python.org/3/library/array.html
https://docs.oracle.com/javase/tutorial/java/nutsandbolts/arrays.html


## 2维数组的基本操作
https://snakify.org/en/lessons/two_dimensional_lists_arrays/
# 声明和元素操作
* 数组的声明，在同一行完成初始化
* 对任意一个元素进行操作：读值和写值
* (练习：打印数组的第1例）

# 遍历数组,需要双重循环，以打印每个元素为例
* python使用range()和len()，java使用size()
* 使用便利的迭代方式
* (练习：计算2维数组中所有元素的和）

# 创建2维数组
* python: 不可以使用 a = [[0]*m]*n, 应该一行一行的创建List
* java 比较简单： int [][] a = new int[N][M] 就可以声明并创建一个N行M列的数组

## 2维数组进行矩阵计算

## 多维数组
多维数组使用语言本身的方式来声明不太方便。可以使用一维数组来模拟。

