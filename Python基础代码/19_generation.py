L1 = [x*x for x in range(5)]
print(L1)
g = (x*x for x in range(5))  # 生成器
print(g)
print(next(g))
print(next(g))

# for i in g:
#    print(i)
