for i in range(1, 11):
    for j in range(1, 11):
        print(i, i * j)

print("*" * 80)

times = [(i, i * j) for i in range (1, 11) for j in range(1, 11)]
print(times)

print("*" * 80)

for x, y in [(i, i * j) for i in range (1, 11) for j in range(1, 11)]:
    print(x, y)

for x, y in ((i, i * j) for i in range (1, 11) for j in range(1, 11)):
    print(x, y)