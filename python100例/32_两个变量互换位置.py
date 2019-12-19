def exchange(x,y):
    x,y = y,x
    return x,y

if __name__ == '__main__':
    a = 10
    b = 20
    print(a,b)
    a,b = exchange(a,b)
    print(a,b)
