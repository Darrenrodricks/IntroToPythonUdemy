fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}
print(fruit)

# for i in range(10):
#     for snack in fruit:
#         print(snack + " is " + fruit[snack])
#     print("*" * 40)
# #
# # ordered_key = sorted(list(fruit.keys()))
# # for g in ordered_key:
# #     print(g + " - " + fruit[g])
# for f in sorted(fruit.keys()):
#     print(f + " - " + fruit[f])
# for val in fruit.values():
#     print(val)
#
# for key in fruit:
#     print(fruit[key])
#
# # print(fruit.keys())
# # print(fruit.values())
#
# fruit_keys = fruit.keys()
# print(fruit_keys)
#
# fruit["tomato"] = "not nice with icecream"
# print(fruit_keys)
print(fruit)
print(fruit.items())
f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)

print(dict(f_tuple))