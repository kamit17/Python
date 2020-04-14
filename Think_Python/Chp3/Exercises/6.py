"""
Write a program which is given an exam mark, and it returns a string —
the grade for that mark — according to this scheme:
------------------------------
| Mark        | Grade        |
------------------------------
| >=75        | First        |
------------------------------
| [70-75)     | Upper Second |
------------------------------
| [60-70)     | Second       |
------------------------------
| [50-60)     | Third        |
------------------------------
| [45-50)     | F1 Supp      |
------------------------------
| [40-45)     | F2           |  
------------------------------
| <40         | F3           |   
------------------------------

The square and round brackets denote closed and
open interval excludes it. So 39.99999 gets grade F3, but 40 gets grade F2. Assume
numbers = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]
"""
numbers = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

for mark in numbers:
    print('\t')
    if mark >=75:
        print(mark , 'First')
    elif mark >=70:
        print(mark ,'Upper Second')
    elif mark >=60:
        print(mark ,'Second')
    elif mark >=50:
        print(mark ,'Third')
    elif mark >=45:
        print(mark ,'F1 Supp')
    elif mark >=40:
        print(mark ,'F2')
    else:
        print(mark ,'F3')
