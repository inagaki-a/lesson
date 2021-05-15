class Human:

    #初期化メソッド
    def __init__(self, name, weight, pet): #初期化
        self.__name = name 
        self.weight = weight 
        self.pet = Pet
    
    #名前を取得する
    def get_name(self):
        return self.__name

    #体重を取得する
    def get_weight(self):
        return self.weight

    def into(self):
        return '飼い主：' + Human.get_name(self) + str(Human.get_weight(self)) + '㎏　ペット：' + Pet.pet_get_name(self) + " " + str(Pet.pet_get_weight(self)) + "㎏"

class Pet(Human):

    #初期化メソッド
    def __init__(self, name, weight, pet, pet_weight):
        super(Pet, self).__init__(name, weight, pet)
        self.pet_weight = pet_weight

    #名前を取得する
    def pet_get_name(self):
        return self.pet
    
    #体重を取得する
    def pet_get_weight(self):
        return self.pet_weight



pet = Pet('たろ', 100.3, 'たろたろ', '10.2')
pet2 = Pet('じろ', 70.5, 'じろじろ', '30.2')
print(pet.into())
print(pet2.into())
