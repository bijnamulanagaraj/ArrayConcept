sentence = "python is stuitable for more technologies"

sentence_length = len(sentence)
char_list = []
for i in range(sentence_length):
    if i % 2 == 0:
        char_list.append(sentence[i])
print(char_list)