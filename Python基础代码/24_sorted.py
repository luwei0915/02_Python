L = [-12,100,-90,1,9]
print(sorted(L))
print(sorted(L,key=abs))

L1 = ['a','b','c','A','B','C']
print(sorted(L1))

L2 = ['bob','about','Zoo','Credit']
print(sorted(L2,key=str.lower,reverse=True))
