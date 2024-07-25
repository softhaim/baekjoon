n1, n2, n3 = map(int, input().split())

if n1 == n2 and n2 == n3:
    print(10000+(n1*1000))
# 3번째가 다름
elif (n1 == n2 and not n2 == n3):
    print(1000+(n1*100))
# 1번째가 다름
elif(not n1 == n2 and n2 == n3):
    print(1000+(n3*100))
# 2번째가 다름
elif n1 == n3 and not n1 == n2:
    print(1000 + (n1*100))
else:
    list_dice = [n1, n2, n3]
    list_dice.sort()
    print(list_dice[-1]*100)