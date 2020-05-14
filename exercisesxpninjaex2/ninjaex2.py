from faker import Faker

fake = Faker()

users = []
for i in range(5):
    user = {"name": fake.name(), "address": fake.address(), "language": fake.language_code()}
    users.append(user)

print(users)
