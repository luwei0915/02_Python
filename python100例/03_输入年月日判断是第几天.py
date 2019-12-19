'''
题目：输入某年某月某日，判断这一天是这一年的第几天？
'''
year = int(input("Year:"))
month = int(input("Month:"))
day = int(input("Day:"))
day_p = (31,28,31,30,31,30,31,31,30,31,30,31)
day_r = (31,29,31,30,31,30,31,31,30,31,30,31)

def getNums(y,m,d):
    s = 0
    if ( y % 400 == 0) or (y % 4 == 0) and (y % 100 != 0):
        for i in range(m-1):
            s += day_r[i]
        print("这是闰年的第:",end="")
    else:
        for i in range(m-1):
            s += day_p[i]
        print("这是平年的第:", end="")
    print(str(s + d) + "天")

getNums(year,month,day)
