# Whenever clock is called, it returns a floating point number representing how many seconds have elapsed since your program started running.

import time

def do_my_sum(xs):
    sum = 0
    for v in xs:
        sum += v
    return sum

sz = 100000000
testdata= range(sz)

t0 = time.clock()
my_result = do_my_sum(testdata)
t1 = time.clock()
print("my_result   = {0} (time taken = {1:.4f} seconds)".format(my_result,t1-t0))

t2 = time.clock()
their_result=sum(testdata)
t3=time.clock()
print("my_result   = {0} (time taken = {1:.4f} seconds)".format(my_result,t3-t2))
