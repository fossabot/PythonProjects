scr_list = ['python', 'php', 'perl']

print('-' * 75)

# Get the element that has to be modified
elem = input('Enter Element to Modify ->')
char_rem = input('Enter character to be removed ->')

# Index
if elem in scr_list:
    idx = scr_list.index(elem)
    new_elem = scr_list[idx].replace(char_rem, '')
    scr_list.pop(idx)
    scr_list.insert(idx, new_elem)

print('New List ->', scr_list)

print('-' * 75)

size = int(input('Enter how many elements -> '))
loc = []
print('Enter Locations -> ')
for n in range(1, size + 1):
    inp = input()
    loc.append(inp)
    
print('All Locations ->', loc)

lst = [(1,2),(3,4),(5,6)]
print('Max ->', max(lst))

print('All Locations ->', loc)

print('-' * 75)
