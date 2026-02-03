def sumList(nums):
    '''Return the sum of the numbers in the list nums.'''
    sum = 0
    for num in nums:
        sum = sum + num
    return sum


def main():
    print(sumList([2,4,6,7,8]))
    print(sumList([62,47,67,77,87]))
    print(sumList([32,54,26,711,1118]))
    print(sumList([21,42,63,71,81]))
    print(sumList([]))

main()
