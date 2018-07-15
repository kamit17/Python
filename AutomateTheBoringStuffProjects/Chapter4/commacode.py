"""
Write a function that takes a list value as an argument and 
returns a string with all the items separated by a comma and 
a space, with and inserted before the last item. 
For example, passing the previous spam list to the function 
would return 'apples, bananas, tofu, and cats'. But your function 
should be able to work with any list value passed to it .
"""


def fun(listvalue):  #defining the function fun which has argument list value
    for i in range(len(listvalue)):
        print(listvalue[i] + ' , ', end='')
        if listvalue[i] == listvalue[-2]:
            print('and ' + listvalue[-1], end='')
            break


spam = ['eggs', 'apples', 'peaches', 'grid']
fun(spam)  #calling function and passing the list

