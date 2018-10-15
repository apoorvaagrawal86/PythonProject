def mul_param(num1, num2, num3):
    return num1 + num2 + num3

print(mul_param(2,3,5))


def prime_num(num):
    count = 2

    while count < num - 1:
        if num % count == 0:
            return False
        count = count + 1


        return True

print(prime_num(11))

