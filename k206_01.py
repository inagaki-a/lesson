karuta = {"い":"犬も歩けば棒に当たる", "ろ":"論より証拠", "は":"花より団子"}
cnt = 0

for i in range(3):
    keyword = input("一文字入力してください")
    result = karuta.get(keyword)
    if result == None:
        print("そんなのないよ!")
        exit()
    else:
        print(result)
        cnt += 1
        if cnt == 3:
            exit()