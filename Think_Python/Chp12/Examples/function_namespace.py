def f():
    n = 7
    print("printing n inside of f: ",n)
    
def g():
    n = 42
    print("printing n inside of g: ",n)

n = 11
print("printing n before calling f : ",n)
f()
print("printing n after calling f: ",n)
g()
print("printing n after calling g: ",n)