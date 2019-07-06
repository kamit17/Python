def eggs(someParameter):
    someParameter.append('Hello')
    someParameter.insert(0, 2)


spam = [1, 2, 3, 11, 14, 16, 333333, 213, 23, 2, 32, 34, 23]
eggs(spam)
print(spam)
