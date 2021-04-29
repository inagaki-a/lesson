class Cow:
    def __init__(self, name: str, age: int, sex: bool, weight: float):
        self.name = name
        self.age = age
        self.sex = sex
        self.weight = weight



    def speak_info(self):
        sex = get_sex(self)
        return (f'({self.name} {self.age} 歳, {self.sex}, {self.weight}Kg)')

    def get_sex(self):
        print("a")



cow1 = Cow("はなこ", 3, False, 100.4)
cow2 = Cow("たろう", 4, True , 200.5)

print(Cow.speak_info(cow2))