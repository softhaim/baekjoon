# 20920
'''
자주 나오는 단어일수록 앞에 배치한다.
해당 단어의 길이가 길수록 앞에 배치한다.
알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다
'''
import sys 
N, M = map(int, sys.stdin.readline().rsplit())

word_set = dict()

for i in range(N):
    word = sys.stdin.readline().strip()
    # 단어가 M보다 길이가 긴 경우만 외울 것
    if len(word) >= M:
        # 단어 세트에 없으면 처음보는 단어이니 카운트 1
        if word not in word_set:
            word_set[word] = 1
        # 있으면 본 단어이니 기존 카운트 + 1    
        else:
            word_set[word] += 1

#-x[1]: value 기준으로 내림차순 정렬. -len(word): 단어 길이를 기준으로 내림차순 정렬. word: 단어를 알파벳 순으로 오름차순 정렬.
sorted_dict_list = sorted(word_set.items(), key=lambda x:(-x[1] ,-len(x[0]), x[0]))

# 정렬된 단어 리스트 출력
for item in sorted_dict_list:
    print(item[0])