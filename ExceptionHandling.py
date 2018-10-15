# try:
#     str1 = input('What is your name? ')
#     int1 = int(input('What is your age? '))
#     print('Hello {}, your age is {}'.format(str1,int1))
# except:
#     print('Please enter a valid input')


def dummy_exceptions(num1, num2):
    try:
        return(num1/num2)
    except:
        print('Please enter a valid input')

print(dummy_exceptions(999,0.0000000000))
