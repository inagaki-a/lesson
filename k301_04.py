class Human:

    def __init__(self, name, weight, pet):
        """初期化メソッド"""
        self.__name = name 
        self.weight = weight 
        self.pet = pet
    
    def get_name(self):
        """名前を取得する"""
        return self.name

    def get_weight(self):
        """体重を取得する"""
        return self.weight

    def info(self):
        """情報を表示する"""
        return '飼い主：' + self.__name + self.weight + '㎏　ペット：' + self.pet.name + self.pet.weight

    def pet_naming(self, value):
        #ペットの名前を付ける
        value = value
        self.pet.pet_naming(value)

class Pet:

    def __init__(self, name, weight):
        """初期化メソッド """
        self.name = name
        self.weight = weight

    def pet_get_name(self):
        """名前を取得する """
        return self.pet

    def pet_naming(self, name):
        """ペットの名前を付けられる"""
        self.name = name

    def pet_get_weight(self):
        """体重を取得する """
        return self.weight
    
"""
pet1 = Pet('たろたろ', '10.2')
human1 = Human('たろ', '100.3', pet1)

pet2 = Pet('じろじろ', '30.2')
human2 = Human('じろじろ', '70.5', pet2)
"""

tarotaro = Pet("たろたろ", '10.2')
taro = Human('たろ', '100.3', tarotaro)
taro.pet_naming('しば')

jirojiro = Pet('じろじろ', '30.2')
jiro = Human('じろ', '70.5', jirojiro)

print(taro.info())
print(jiro.info())
