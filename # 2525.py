h, m = map(int, input().split())
c = int(input())

m += c
if m >= 60:
    over_hour = m//60
    m = m%60
    h += over_hour
if h>= 24:
    h = h%24
print(h, m)