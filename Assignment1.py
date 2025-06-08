rows = 5
#Lower Triangle
print('Upper Triangle')
for i in range(1 , rows+1):
    print('*' * i)
print()
#Upper Triangle
print('Lower Triangle')
for i in range(rows , 0 , -1):
    print('*' * i)
print()
#Pyramid
print('Pyramid')
for i in range(1 , rows+1):
    for j in range(rows - i):
        print(' ' , end='')
    for k in range(2*i-1):
        print('*', end='')
    print()