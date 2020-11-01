def test():
    assert sum([3,4,5]) == 12
    assert ElementWiseMultiplication([3,2],[4,5])==[12,10]
    assert DotProduct([1,2],[3,-4]) == -5

def ElementWiseMultiplication(list1,list2):
    return [list1[i]  *  list2[i] for i in range(len(list1))]

def DotProduct(list1,list2):
    return sum(ElementWiseMultiplication(list1,list2))