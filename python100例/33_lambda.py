MAX = lambda x,y:(x>y)*x + (x<y)*y
MIN = lambda x,y:(x>y)*y + (x<y)*x

a = 10
b = 20

if __name__ == '__main__':
    print(MAX(a,b))
    print(MIN(a,b))
