#side note

# is_friend = True
# can_message = "message allowed" if is_friend else "not allowed to message"

# print(can_message)

#exercise

string = input("give me a 10 character word: ")

if (len(string) == 10):
    print("first char is: ", string[0])
    print("last char is: ", string[9])
    
    for i in range(len(string)):
        print(string[i])
        i += 1

else: 
    print("give me a 10 char word plz..")

#jumbler

s = list(string)
s[0] = s[5]
s[1] = s[6]
s[2] = s[7]
s[3] = s[8]
s[4] = s[9]
s = "".join(s)
print(s)
