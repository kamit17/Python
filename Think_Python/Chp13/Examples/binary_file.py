
f=open("/Users/maverick/GitHub/Python/Think_Python/Chp13/Examples/bats-three-2.jpg", "rb")

g=open("/Users/maverick/GitHub/Python/Think_Python/Chp13/Examples/bats_copy.jpg","wb")

while True:
    buf = f.read(1024)
    if len(buf) == 0:
        break

    g.write(buf)
#print(type(buf))

f.close()
g.close