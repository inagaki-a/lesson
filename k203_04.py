import decimal
ganpon = 100000
addkingaku = 20000
riritu = 0.07

#年に1度利息がつく
#10年分出力

#毎月2万円を12回積み立てる
#合計残額＋積立額から年利7％で利息を計算する
#合計残額に利息を足す

for i in range(10):
    #10年処理する
    for k in range(12):
        #毎月2万円を12回積み立てる
        ganpon = ganpon + 20000
    risokumaeganpon = ganpon
    #合計残額＋積立額から年利7％で利息を計算する
    #合計残額に利息を足す
    d = decimal.Decimal('0.07')
    risoku = round(risokumaeganpon*d)
    ganpon = ganpon + risoku
    print(str(i) + "年目" + "{:,}".format(risokumaeganpon) + "円" + "{:,}".format(ganpon) + "円")