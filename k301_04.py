class Human:

    #初期化メソッド
    def __init__(self, name, weight, Pet): #初期化
        self.__name = name 
        self.weight = weight 
        self.pet = Pet
    
    #名前を取得する
    def get_name(self):
        return self.name

    #体重を取得する
    def get_weight(self):
        return self.weight

    def info(self):
        return '飼い主：' + self.__name + self.weight + '㎏　ペット：' + self.pet.name + self.pet.weight

class Pet:

    #初期化メソッド
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    #名前を取得する
    def pet_get_name(self):
        return self.pet
    
    #体重を取得する
    def pet_get_weight(self):
        return self.weight
    

pet1 = Pet('たろたろ', '10.2')
human1 = Human('たろ', '100.3', pet1)

pet2 = Pet('じろじろ', '30.2')
human2 = Human('じろじろ', '70.5', pet2)

print(human1.info())
print(human2.info())
