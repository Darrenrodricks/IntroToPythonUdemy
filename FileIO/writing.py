# cities = ["San Jose", "Almaden", "San Francisco"]
#
# with open("cities.txt", 'w') as city_file:
#     for city in cities:
#         print(city, file=city_file)

# cities = []
#
# with open("cities.txt", 'r') as city_file:
#     for city in city_file:
#         cities.append(city.strip('\n'))
#
# print(cities)
# for city in cities:
#     print(city)

# imelda = "More Mayhem", "Imedla May", "2011", (
#     (1, "pulling the rug"), (2, "psycho"), (3, "mayhem"), (4, "kentish town road"))
#
# with open("imdela3.txt", 'w') as imelda_file:
#     print(imelda, file=imelda_file)

with open("imdela3.txt", 'r') as imdelda_file:
    contents = imdelda_file.readline()

imdela = eval(contents)

print(imdela)
title, artist, year, tracks = imdela
print(title)
print(artist)
print(year)
