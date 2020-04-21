#ceasercypher

answer = input("encrypt or decrypt? E/D")
word = input("what is your word ?")
encrypted_word = []
decrypted_word = []

if (answer == "E"):
    lword = list(word)
    for x in lword:
        encrypted_word.append((chr(ord(x) + 2)))
    print("".join(encrypted_word))

if (answer == "D"):
    lword = list(word)
    for x in lword:
        decrypted_word.append((chr(ord(x) - 2)))
    print("".join(decrypted_word))

