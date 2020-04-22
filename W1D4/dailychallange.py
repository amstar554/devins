matrix = [
    ['@&@'],
    ['Tsi'],
    ['h x'],
    ['i& '],
    ['sM('],
    ['$a('],
    [' t%'],
    ['ir!'],
]
i = 0
word1, word2, word3 = [],[],[]
while i < 8:
    word1 += matrix[i][0][0]
    word2 += matrix[i][0][1]
    word3 += matrix[i][0][2]
    i += 1
print(word1)
print(word2)
print(word3)

def letterfinder():
    scrambled_sent = word1 + word2 + word3
    only_letters_sent =[]
    for i in scrambled_sent:
        if 65 < ord(i) < 122:
            only_letters_sent.append(i)
        if ord(i) == 32:
            only_letters_sent.append(" ")
    print(only_letters_sent)

letterfinder()
