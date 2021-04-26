from collections import OrderedDict
moji_list = "たったひとつのしんじつみぬく、みためはこども、ずのうはおとな"
moji_list_mojisu = len(moji_list)
moji_uni = ((''.join(OrderedDict.fromkeys(moji_list))))
mojisu = len(moji_uni)

for i in range(mojisu):
    cnt = 0
    moji = moji_uni[i]
    for k in range(moji_list_mojisu):
        moji2 = moji_list[k]
        if moji == moji2:
            cnt += 1
    print(moji + ":　" + str(cnt) + "個")