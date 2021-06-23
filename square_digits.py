def square_digits(num):
    digits =[]
    number = num
    if num != 0:
        while number > 0:
            last_digit = number % 10
            squared = last_digit * last_digit
            digits.insert(0, squared)
            number = (number - number % 10) // 10
        strings = [str(digit) for digit in digits]    
        a_string = "".join(strings)
        an_integer = int(a_string)
        return an_integer
    else:
        return num

square_digits(9119) #return 811181
square_digits(0) #return 0

def square_digits(num):
    string_int = ""
    for x in str(num):
        string_int += str(int(x) ** 2)
    return int(string_int)
