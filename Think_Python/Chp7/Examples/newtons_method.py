"""
Newton's method for findind square roots
If you start with almost any approximation, you can computer a better approximation
with the following formula
better = (approximation + n/approximation)/2
"""
n = 25
threshold = 0.001
approximation = n/2 # Start with some or other guess at the answer
while True:
    better = (approximation + n/approximation) /2
    if abs(approximation-better) < threshold:  #make this smaller for better accuracy
        print(better)
        break
    approximation = better
