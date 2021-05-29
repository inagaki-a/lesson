class Fish:
    def __init__(self):
        self.name = "魚"
        self.swim = ""

class Demekin(Fish):
    def __init__(self):
        super().__init__()
        self.name = "出目金"
        self.swim = "ふりふり"

class Shake(Fish):
    def __init__(self):
        super().__init__()
        self.name = "サメ"
        self.swim = "すいすい"

def action(self):
    return self.name + "は" + self.swim + "泳ぐ。"

sakana = Fish()
demekin = Demekin()

print(action(sakana))
print(action(demekin))
print(action(sakana))
