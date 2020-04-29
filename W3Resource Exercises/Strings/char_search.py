def search (char,str):
    L = len(str)
    print(L)
    i = 0
    while i < L:
        if str[i]==char:
            return 1
            i = i + 1
        return -1

print(search("T","PYTHON"))
