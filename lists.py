list1 = range(0,10)
print(list(list1))
for i in list1:
    print(f'Now looping through the {i} element')
list2 = list1[4:9]
for i in list2:
    print(i*2)

odds =[]
evens = []

for i in list1:
	if i%2 == 0 :
		evens.append(i)
	else:
		odds.append(i)

print(f'Even list: {evens} | odd list :{odds}')
