#33. Write a Python program to print the following integers with zeros on the left of specified width.

x = 252342
print("string with  padding of  5 on left with 0  is {:0>5d}".format(x))
print("string with  padding of  5 on rigth with *  is {:*<5d}".format(x))
print("string with  comma seperator   is {:,}".format(x))
print("string with  percentage   is {:.2%}".format(x))
print("Left aligned (width 10)   :"+"{:< 10d}".format(x));
print("Right aligned (width 10)  :"+"{:10d}".format(x));
print("Center aligned (width 10) :"+"{:^10d}".format(x));
print()
