import math

a = int(input('Enter a term: '))
b = int(input('enter b term:'))
c = int(input('enter c term:'))

print("press 1 to find the roots. press 2 to find weather it has a single root 2 roots or complex")
choice = int(input())
if choice == 1:
    dis = b ** 2 - 4 * a * c

    if dis < 0:
        print('erorr')
    else:
        sqrtdis = math.sqrt(dis)
        x1 = (-b + sqrtdis) / (2 * a)
        x2 = (-b - sqrtdis) / (2 * a)
        print('x1=', x1, 'x2= ', x2)
if choice == 2:
    dis = b ** 2 - 4 * a * c
    if dis == 0:
      print('1 root')
    if dis > 0:
      print('two roots')
    if dis < 0:
        print('complex')

else:
    print('invalid')
