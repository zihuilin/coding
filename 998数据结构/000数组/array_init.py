# -*- coding: utf-8
# 声明长度为5的数组

score=[0]*5
score[1]=5

# print(score[5]) #这里5作为数组的下标，越界了
for s in score[:]:
    print('%d\n' %s)

print("长度：%d" %len(score)) #build-in function len()

score.append(6) #添加元素，使数组的长度增加了
print(score[5])

print('--------------------------------')
array=[[1,2,3],[11,22],[333,444]]

for row in array:
    for ele in row:
        print ("%d\t" % ele,end='')
    print('')

for i in range(len(array)):
    for j in range(len(array[i])):
        print('%d\t' % int(array[i][j]), end='')
    print('')
