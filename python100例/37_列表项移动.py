'''
题目：有n个整数，使其前面各数顺序向后移m个位置，
      最后m个数变成最前面的m个数
'''
a = [i for i in range(1,20,2)]
def move_item(n):
    for j in range(n):
        temp = a.pop()
        a.insert(0,temp)
    print(a)

if __name__ == '__main__':
    print("The original list is:\n",a)
    num = int(input("Num(1-9):"))
    move_item(num)
