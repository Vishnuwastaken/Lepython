Guest_List = ['Jim', 'Bob', 'Luke', 'Richard']

i = 0
print(f'I can make it, {Guest_List[i]}.')
i = i+1
print(f'I can make it, {Guest_List[i]}.')
i = i+1
print(f'I can make it, {Guest_List[i]}.')
i = i+1
print(f'I cant make it, {Guest_List[i]}.')

print(f'{Guest_List[-1]}. cant attend :(.')

Guest_List[0] = Guest_List[0].upper()
print(f'{Guest_List[0]} is the updated first person on the list.')

Guest_List.append('King;')
print(Guest_List)

Guest_List.insert(0, 'Fish')
print(Guest_List)

del Guest_List[-1]
print(Guest_List)

del Guest_List[-1]
print(Guest_List)

leaving_s = Guest_List.pop()
print(f'Goodbye sucks u cant make it , {leaving_s}')
print(f' The current ppl in the list are {Guest_List}')

leaving_s = Guest_List.pop()
print(f'Goodbye sucks u cant make it , {leaving_s}')
print(f' The current people in the list are {Guest_List}')
