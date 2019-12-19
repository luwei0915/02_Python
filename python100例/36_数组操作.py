'''
题目：输入数组，最大的与第一个元素交换，
      最小的与最后一个元素交换，输出数组。
'''
a = []
MAX = 0
MIN = 100

def findMax(x):
    global MAX,MIN
    if x > MAX:
        MAX = x
    if x < MIN:
        MIN = x

def exchange(*args):
    a = list(args)
    # 定位元素
    index_max = a.index(MAX)
    index_min = a.index(MIN)
    v_max = a[0]
    v_min = a[len(a)-1]
    # 替换元素
    a[0] = MAX
    a[index_max] = v_max
    a[len(a)-1] = MIN
    a[index_min] = v_min
    print(a)

if __name__ == '__main__':
    a = list(map(int,input("Nums separated by spaces:").strip().split(" ")))
    for i in a:
        findMax(i)
    exchange(*a)
