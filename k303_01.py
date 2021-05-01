class Pikachu():

    #初期化メソッド
    def __init__(self, power, attack, defense, speed, technique1, technique2, technique3): #初期化
        self.power = power
        self.attack = attack
        self.defense = defense 
        self.speed = speed 
        self.technique1 = technique1
        self.technique2 = technique2
        self.technique3 = technique3
    
    def status(self):
        return self.power, self.attack, self.defense, self.speed, self.technique1, self.technique2, self.technique3, self.technique4, self.technique5, self.technique6,
    
class Raichu(Pikachu):
    def __init__(self, power, attack, defense, speed, technique1, technique2, technique3, technique4, technique5, technique6):
        super().__init__(power, attack, defense, speed, technique1, technique2, technique3)
        self.technique4 = technique4
        self.technique5 = technique5
        self.technique6 = technique6

pikachu = Pikachu(100, 200, 300, 400, "電光石火", "10万ボルト", "アイアンテール")
raichu = Raichu(100, 200, 300, 400, "電光石火", "10万ボルト", "アイアンテール", "ロケット頭突き", "かみなりパンチ", "かみなり")

print(raichu.status())