a = ['Bananas','Orange','Mangoes']
b = ['Bread', 'Eggs','Tomatoes']
c = ['Rice','Beans','Yams']


print('SN\t','\tOBJECT\t','\tPOSITION')
print()
food = [a,b,c]
count = 0
for column in range(3):
    for row in range(3):
        count+=1
        print(f'{count}\t\t{food[row][column]}\t\t{[row]}{[column]}',end=" ")
        print('')

print('==================================================')
print()
print('SN\t','\tOBJECT\t','\tPOSITION')
count = 0
for row in range(2,-1,-1):
    for column in range(2,-1,-1):
        count +=1
        print(f'{count}\t\t{food[column][row]}\t\t{[column]}{[row]}',end=" ")
        print('')
        

print('==================================================')

print('SN\t','\tObject\t','\tPosition')
print()
count = 0
for row in range(3):
    for column in range(3):
        count+=1
        print(f'{count}\t\t{food[row][column]}\t\t{[row]}{[column]}',end=" ")
        print('')
        
        
    