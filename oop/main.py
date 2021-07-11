from enemy import Enemy, Troll, Vampire, VampireKing

ugly_troll = Troll("pug")
print("Ugly Troll - {}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another Troll - {}".format(another_troll))

brother = Troll("Urg")
print(brother)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()

vamp = Vampire("demon")
print(vamp)

itadori = Vampire("sukuna")
print(itadori)

itadori.take_damage(12)
vamp.take_damage(12)

# while itadori.alive:
#     itadori.take_damage(1)
        # print(itadori)

vamp._lives = 0
vamp._hit_points = 1
print(vamp)

carti = VampireKing("carti")
carti.take_damage(20)