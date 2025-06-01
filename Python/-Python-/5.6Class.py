# d={"students":[{"name":"A","sex":"M"},{"name":"B","sex":"C"}]}
# for k1 in d.keys():
#     for k2 in d[k1]:
#         for k3 in k2.keys():
#             print(k3,k2[k3])
while True:
    coin=hero.findNearestItem()
    if coin:
        hero.move(coin.pos)
    if hero.gold>=80:
        for i in range(4):
            hero.summon("soldier")
        break
# 召唤 4 个士兵来做诱饵
