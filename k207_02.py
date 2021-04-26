from decimal import Decimal, ROUND_DOWN
import pandas as pd

def powerkeisan(power, magic, charm):
    power_keisu = Decimal('1.5')
    magic_keisu = Decimal('1.7')
    charm_keisu = Decimal("10")
    total_power = ((power*power_keisu) + (magic*magic_keisu)) * (charm/charm_keisu)

    return total_power

row0 = ["ヨシヒコ", 70, 30, 50]
row1 = ["ダンジョ", 90, 0, 45]
row2 = ["ムラサキ", 10, 80, 90]
row3 = ["メレブ", 20, 50, 5]

df = pd.DataFrame([row0,row1,row2,row3], columns=['名前','ちから','まりょく','みりょく'])

for index, row in df.iterrows():
    total = powerkeisan(row['ちから'], row['まりょく'] , row['みりょく'])
    print(row['名前'] + " : " + str(total))
    