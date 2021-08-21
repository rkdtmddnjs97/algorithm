# voca_list = []
# for i in range(int(input())):               # 테스트케이스 수 입력
#     voca_list.append(input())               # 입력하는 단어를 리스트로 저장
 
# print(voca_list)
# set_voca_list = list(set(voca_list))        # 리스트의 중복 제거

# print("set_voca_list",set_voca_list)
# sort_voca_list = []
 
# for j in set_voca_list:
#     sort_voca_list.append((len(j), j))      # 단어의 길이와 단어를 같이 리스트화 시켜 저장
# print("sort_voca_list",sort_voca_list)
# sort_voca_list.sort()                       # sort()는 len(j), j 에서 앞을 먼저 정렬후에 앞의 조건이 일치하면 뒤를 정렬한다.
# print("sort_voca_list2",sort_voca_list)
# for len_voca, voca in sort_voca_list:       # 리스트를 순환시켜 순서대로 출력
#     print(voca)

words_num = int(input())
words_list = []

for _ in range(words_num):
    word = str(input())
    word_count = len(word)
    words_list.append((word, word_count))

#중복 삭제
words_list = list(set(words_list))
print("sort전",words_list)
#단어 숫자 정렬 > 단어 알파벳 정렬
words_list.sort(key = lambda word: (word[1], word[0]))
print("sort후",words_list)
for word in words_list:
    print(word[0])