banana = 100
peach = 300
total_price = (banana*25)+(peach * 25)
print(str(banana) + "円のバナナを25個、"+ str(peach) + "円の桃を25個買ったら、合計" +  "{:,}".format(total_price) + "円になりました。")