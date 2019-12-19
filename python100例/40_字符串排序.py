def sort_str(str1,str2,str3):
    if str1 > str2: str1, str2 = str2, str1
    if str1 > str3: str1, str3 = str3, str1
    if str2 > str3: str2, str3 = str3, str2
    print(str1,str2,str3)

if __name__ == '__main__':
    str1 = input("Str1:")
    str2 = input("Str2:")
    str3 = input("Str3:")
    sort_str(str1,str2,str3)
