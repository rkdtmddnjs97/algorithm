T = int(input())
words = []
for t in range(T):
    word = str(input())
    word_len = len(word)
    words.append((word,word_len))

words = list(set(words))
words.sort(key= lambda x:(x[1],x[0]))
for value, key in words:
    print(value)