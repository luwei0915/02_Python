def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)
print(fact(5))

def fact1(num,s): #尾递归
    if num == 1:
        return s
    return fact1(num-1,num*s)  #num*s作为新的s
print(fact1(5,1))
'''
(4,5*1)
(3,4*5)
(2,3*20)
(1,2*60)
(0,1x*120)
'''
