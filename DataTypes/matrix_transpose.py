#matrix tranpose without list comprehension

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(matrix)
transposed = []
for i in range(4):
  transposed_row = []
  for row in matrix:
    transposed_row.append(row[i])
  transposed.append(transposed_row)
print('The matrix after tranpose is :' + str(transposed))