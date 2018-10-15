numbers = []

for i in range(1,11):
    numbers.append(i)

print(numbers)

guess = int(input("Enter a no. from 1 to 10"))
if guess in numbers:
    print('You Won!')
else:
    print('You Lost')
