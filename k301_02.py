class Cow:
    #n = 0

    #初期化メソッド
    def __init__(self, name: str, age: int, sex: bool, weight: float): #初期化
        self.name = name 
        self.age = age
        self.sex = sex
        self.weight = weight

    #話す
    def speak_info(self):
        a = self.sex
        c = self.sex_return(a)
        print((f'{self.name} {self.age} 歳  {c} {self.weight}Kg'))

    #性別出力用
    def sex_return(self, sex):
        b = self.sex
        if sex == True:
            return("オス")
        else:
            return("メス")


cows = []
cows.append(Cow("はなこ", 3, False, 100.4))
cows.append(Cow("たろう", 4, True, 200.5))
cows.append(Cow("むげん", 9, True, 300.6))


for cow in cows:
    cow.speak_info()
