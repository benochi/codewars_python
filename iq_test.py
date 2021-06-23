"""should count odd and even numbers and return the index of the outlying number"""
def iq_test(numbers):
    zero = 0
    one = 0
    zeros = 0
    ones = 0
    list1 = numbers.split()
    for element in list1:
        integer = int(element)
        if integer % 2 == 0:
            zero = list1.index(element)
            zeros += 1
        else:
            one = list1.index(element)
            ones += 1
    if zeros < ones:
        return zero + 1
    else:
        return one + 1
 #SAME AS
def iq_test(n):
    n = [int(i)%2 for i in n.split()]
    if n.count(0)>1:
        return n.index(1)+1
    else:
        return n.index(0)+1      
