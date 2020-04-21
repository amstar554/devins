#ex1

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
#
# x = zip(keys, values)
# print(dict(x))

#ex2

store = {
    "name" : "Zara",
    "creation_date" : 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": {"men", "women", "children", "home"},
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {"France": ["blue"], "Spain": ["red"], "US": ["pink", "green"]}
}

store["number_stores"] = 2
print("Zara clients are: ", store["type_of_clothes"])
store["country_creation"] = "Spain"
if ("international_competitors" in store):
    store["international_competitors"].append("Desigual")
del store["creation_date"]
print(store["international_competitors"][-1])
print("Major colors in the US: ", store["major_color"]["US"])
print("length of dictionary: ", len(store))
print("here are the keys: ")
for key in store:
    print(" -> ", key)

more_on_store = {
    "creation_date": 1975,
    "number_stores": 10000
}
more_on_store["number_stores"] += store["number_stores"]
store.update(more_on_store)
print("number of stores: ", store["number_stores"])

print(store)