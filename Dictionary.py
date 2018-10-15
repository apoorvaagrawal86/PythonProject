person = {'Name':'Apoorva','Address':'Sector 23','Age':'31',}

print(person)

print(person['Name'])

person['City'] = 'Gurgaon'
print(person['City'])

print(person)

print('Name' in person)

print('Pin' not in person)

del(person['City'])

print(person)

person['City'] = 'Delhi'

print(person)

print(person.keys())

print(person.values())

print(person.items())

print(person.pop('Address'))

person['Address'] = 'Sector 23'

print(person)

print(person.popitem())

print(person)

new_person_dict = person.copy()

print(new_person_dict)

new_person_dict['Address'] = 'Sector 23'

print(new_person_dict)

new_person_dict.clear()

print(new_person_dict)