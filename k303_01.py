class Pikachu():

    #初期化メソッド
    def __init__(self, name, power, attack, defense, speed): #初期化
        self.name = name
        self.power = power
        self.attack = attack
        self.defense = defense 
        self.speed = speed
        self.waza = 1
    
    def status(self):
        return self.power, self.attack, self.defense, self.speed
    
    def denkou(self):
        damage = self.power * self.waza * 1
        print(self.name + "が電光石化をした。(ダメージ：" + str(damage) + ")")

    def bolt(self):
        damage = self.power * self.waza * 2
        print(self.name + "が10万ボルトをした。(ダメージ：" + str(damage) + ")")

    def aian(self):
        damage = self.power * self.waza * 3
        print(self.name + "がアイアンテールをした。(ダメージ：" + str(damage) + ")")
    
    
class Raichu(Pikachu):
    def __init__(self, name, power, attack, defense, speed):
        super().__init__(name, power, attack, defense, speed)
        self.waza = 2

    def rocket(self):
        damage = self.power * self.waza * 3
        print(self.name + "がロケット頭突きをした。(ダメージ：" + str(damage) + ")")

    def pikapanch(self):
        damage = self.power * self.waza * 3
        print(self.name + "がかみなりパンチをした。(ダメージ：" + str(damage) + ")")

    def pika(self):
        damage = self.power * self.waza * 3
        print(self.name + "がかみなりをした。(ダメージ：" + str(damage) + ")")

pikachu = Pikachu("さとしピカチュウ", 100, 200, 300, 400)
raichu = Raichu("さとしライチュウ", 100, 200, 300, 400)

pikachu.denkou()
pikachu.bolt()
pikachu.aian()

raichu.denkou()
raichu.pikapanch()
raichu.pika()