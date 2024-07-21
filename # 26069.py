# 26069

N = int(input())

people = set()
cnt = 0

for i in range(N):
    name1, name2 = input().split()
    # ChongChong 이 있으면 그때부터 춤 추는거라서 이후 사람들 넣음
    if name1 == 'ChongChong' or name2 == 'ChongChong':
        people.add(name1)
        people.add(name2)
    # 비어있지 않을 때, 해당 이름들이 기존에 있던 사람인지 체크
    elif name1 in people:
        people.add(name2)
    elif name2 in people:
        people.add(name1)

print(len(people))