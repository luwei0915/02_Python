'''
打印如下图形，行数由输入控制
   *                 3  1  3
  ***                2  3  2
 *****               1  5  1
*******              0  7  0
 *****               1  5  1
  ***                2  3  2
   *                 3  1  3
'''
num = int(input("输入一个奇数："))
print(num)
row = int((num + 1) / 2)
times = int((num - 1) / 2)
sp = " "
char = "*"

for i in range(1,num+1):
    if (i <= row):
        s = times*sp + (num - 2*times)*char + times*sp
        print(s)
        times -= 1     # 最后一次循环，times = -1
        if (times == -1):
            times += 1
    else:
        times += 1
        s = times * sp + (num - 2 * times) * char + times * sp
        print(s)
