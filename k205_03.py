osero =  [[0 for j in range(5)] for i in range(5)]
osero[0][0] = "〇"
osero[0][1] = "〇"
osero[0][2] = "〇"
osero[0][3] = "〇"
osero[0][4] = "〇"
osero[1][0] = ""
osero[1][1] = ""
osero[1][2] = "●"
osero[1][3] = "〇"
osero[1][4] = ""
osero[2][0] = ""
osero[2][1] = "●"
osero[2][2] = "〇"
osero[2][3] = "●"
osero[2][4] = "●"
osero[3][0] = ""
osero[3][1] = "●"
osero[3][2] = ""
osero[3][3] = "●"
osero[3][4] = ""
osero[4][0] = ""
osero[4][1] = ""
osero[4][2] = ""
osero[4][3] = ""
osero[4][4] = "●"

white_maru = 0
black_maru = 0

for i in osero:
    for k in i:
        if k == "〇":
            white_maru += 1
        elif k == "●":
            black_maru += 1

print("〇: " + str(white_maru) + "個")
print("●: " + str(black_maru) + "個")
if white_maru > black_maru:
    print("〇: " + "勝ち")
elif white_maru < black_maru:
    print("●: " + "勝ち")
else:
    print("引き分け")