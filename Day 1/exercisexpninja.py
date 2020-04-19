# #ex2
# a = 70
# b = 9

# if (a > b):
#     print("cello world")

#ex3
month = input("I'll tell you the season if you tell me the month (1-12): ")
month = int(month)

if (month >= 3 and month <= 5):
    season = "springggg"
elif (month >= 6 and month <= 8):
    season = "summa summa summaa"
elif (month >= 9 and month <= 11):
    season = "AUTUMN"
else: 
    season = "gotta be wintaa"
print(season)
