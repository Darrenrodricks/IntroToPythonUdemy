text = "what have the romans ever done for us"

capitals = [char.upper() for char in text]
print(capitals)

map_capitals = list(map(str.upper, text))
print(map_capitals)


def comp_caps():
    capitals = [char.upper() for char in text]
    return capitals


# use map
def map_caps():
    map_capitals = list(map(str.upper, text))
    return map_capitals
