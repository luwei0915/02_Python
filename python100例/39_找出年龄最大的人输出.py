'''
题目：找到年龄最大的人，并输出。请找出程序中有什么问题。
'''
person = {"li": 18, "wang": 50, "zhang": 20, "sun": 22}

if __name__ == '__main__':
    name = ''
    age = -1
    for key in person.keys():
        if (person[key] > age):
            age = person[key]
            name = key
    print(name,age)
