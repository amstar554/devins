username = input("enter name: ")
secret = input("enter password: ")

i = len(secret)
starred_secret = i * '*'

print(f"Hello {username}, your password {starred_secret} is ", i ," characters long.")