class Animal:
    def __init__(self, name):
        self.name = name

class Fish(Animal):
    def __init__(self, name, swim):
        super().__init__(name)
        self.swim = swim

    def action(self):
        return self.name + "は" + self.swim + "泳ぐ。"


fish1 = Fish('出目金', 'ふりふり')
fish2 = Fish('サメ', 'すいすい')
fish3 = Fish('シーラカンス', 'ゆらゆら')

print(fish1.action())
print(fish2.action())
print(fish3.action())