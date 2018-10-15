colors = ['blue','green','yellow','red']
print(colors)

different_data_types = [1,2,0.4,'James',True]
print(different_data_types)

print(colors.count('green'))

colors.append('red')

print(colors.count('red'))

numbers = [1,2,3]

for i in range(4, 11):
    numbers.append(i)
    print(numbers)

print(colors)
colors.pop()
print(colors)

print(len(colors))

total = colors + numbers
print(total)
print(len(total))

print('green' in colors)
print(colors)
print(colors[-1])




