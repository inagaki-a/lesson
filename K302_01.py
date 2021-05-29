class Horse:
    def __init__(self, name, weight, speed): #初期化
        self.name = name
        self.weight = weight
        self.speed = speed

    def horse_run(self, *args):
        #馬のみ
        if len(args) == 0:
            return self.name + "走る。（速度：" + str(self.speed) + "㎞/h）"
        #人か騎手のせた時
        else:
            total_weight = 0
            count = 0
            for i in args:
                total_weight += i.weight
                count += 1
            #200キロ以上は走らなない
            if total_weight > 200:
                return 0
            #人の場合
            elif isinstance(args[0], Human) == True:
                speed = self.speed - total_weight/Human.jouba
            #騎手の場合
            elif isinstance(args[0], Kishu) == True:
                speed = self.speed - total_weight/Kishu.jouba
            #文章作成
            return self.name + "走る。乗馬者" +str(count) + "名（速度：" + str(speed) + "㎞/h）"
class Human:
    jouba = 10
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class Kishu:
    jouba = 20
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

horse1 = Horse("ディープインパクト", 200.5, 50)
print(Horse.horse_run(horse1))
kishu1 = Kishu("たけゆたか", 50.2)
human2 = Human("たなか", 70.2)
human3 = Human("さとう", 60.6)

#人の処理
print(Horse.horse_run(horse1, human2, human3))

#騎手の処理
print(Horse.horse_run(horse1, kishu1))
    




 #   def horse_human_run(hours, *args):
 #       total_weight = 0
 #       count = 0
 #       for i in args:
 #           total_weight = i.weight
 #           count += 1
#
#        if total_weight > 200:
#            return 0
#        else:
#            return hours.name + "走る。乗馬者" + str(total_weight) + "名（速度：" + str(hours.speed - total_weight/10) + "㎞/h）
#
#    def horse_kishu_run(hours, *args):
#        return hours.name + "走る。乗馬者" + str(len(*args)) + "名（速度：" + str((hours.speed) - sum(*args)/20) + "㎞/h）"
#        #return hours.name + "走る。乗馬者" + str(len(*args)) + "名（速度：" + str(hours.speed - sum(*args)/20) + "㎞/h）"
            



#騎手と人間と同じであれば、変数名はおなじでよい

