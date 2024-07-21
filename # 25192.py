# 25192

N = int(input())

people = set()
cnt = 0

for i in range(N):
    input_string = input()
    
    if (input_string == 'ENTER'): # 엔터입력 후 리스트 비움
        people.clear()
    else:
        # 엔터 입력 후에 입력되는 것들이 리스트안에서 중복 되면 카운트 안함
        # not in 연산자리스트 (List): not in 연산자는 리스트의 모든 요소를 순차적으로 검사하여 값이 존재하지 않음을 확인합니다. 리스트의 길이가 n일 때, 최악의 경우 시간 복잡도는 O(n) set은 O(1)
        if input_string not in people:
            people.add(input_string)
            cnt = cnt + 1

print(cnt)