for i in range(1, 11):

    for j in range(1, 11):
        print(f'{i*j:3}', end=' ')
    print(end='\n')


print('#'*20)

for n in range(1, 11):
    for m in range(1, 11):
        print(n, '*', m, '=', f'{n*m:3}')
    print('-'*20)
