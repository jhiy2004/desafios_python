def maior(*num):
    for n in num:
        print(n, end=' ')
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {max(num) if len(num) > 0 else 0}.')
    print('-='*30)

print('-='*30)
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()