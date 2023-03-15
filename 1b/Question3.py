def addition(a, b):
    carry = 0
    result = ''
    for i in range(max(len(a), len(b))):
        a_i = int(a[len(a) - i - 1]) if i < len(a) else 0
        b_i = int(b[len(b) - i - 1]) if i < len(b) else 0
        s = a_i + b_i + carry
        result = str(s % 2) + result
        carry = s // 2
    if carry:
        result = '1' + result
    return result

def subtraction(a, b):
    borrow = 0
    result = ''
    for i in range(max(len(a), len(b))):
        a_i = int(a[len(a) - i - 1]) if i < len(a) else 0
        b_i = int(b[len(b) - i - 1]) if i < len(b) else 0
        s = a_i - b_i - borrow
        if s < 0:
            s += 2
            borrow = 1
        else:
            borrow = 0
        result = str(s) + result
    return result

def multiplication(a, b):
    result = '0'
    for i in range(len(b)):
        if b[len(b) - i - 1] == '1':
            result = addition(result, a + '0' * i)
    return result

def division(a, b):
    dividend = a
    divisor = b
    quotient = ""
    remainder = ""
    while len(dividend) >= len(divisor):
        if dividend[0] == "1":
            remainder += "0"
            dividend = subtraction(dividend, divisor)
        else:
            remainder += "1"
            dividend = dividend[1:]
        quotient += "1" if dividend != "0"*len(dividend) else "0"
    return quotient, remainder

a = input("Enter the first binary number: ")
b = input("Enter the second binary number: ")
print("The result after binary addition: ", end="")
print(addition(a,b))
print("The result after binary subtraction: ", end="")
print(subtraction(a,b))
print("The result after binary Multiplication: ", end="")
print(multiplication(a,b))
Quotient, Remainder = division(a,b)
print("The result after binary Division: ", end="")
print(f"Quotient= {Quotient}, Remainder= {Remainder}")

