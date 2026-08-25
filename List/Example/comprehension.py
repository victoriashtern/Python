countries =['Argentina','Belice','Brazil','Canada','Danmark','Estonia','Zambia']
list =[0,1,2,3,4,5,6,7,8,9]
comprehension =[x+1 for x in list if x<5]

print(comprehension)

print([c + ":" for c  in countries])
print([c + ":" for c  in countries if len(c) >7])
list.extend([1,3])


list =[0,1,2,3,4,5,6,7,8,9]
print(list.extend([1,3]))
