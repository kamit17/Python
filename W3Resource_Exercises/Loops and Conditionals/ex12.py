"""
12. Write a Python program that accepts a sequence of lines (blank line to terminate
) as input and prints the lines as output (all characters in lower case).
"""
lines = []
while True:
    line = input()
    if line:
        lines.append(line.upper())
    else:
        break
for line in lines:
    print(line)
