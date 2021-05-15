class Player:
    def __init__(self, name, level): #初期化
        self.name = name
        self.level = level
        #self.items = items

    def info(self):
        print("Player Name:" + self.name + "Level:" + str(self.level))
    
class Itme:
    def __init__(self, name, count):
        self._name = name
        self._count = count
        return print(self.name)


player = Player("カリュプソー",99)
player.info()
item_dict = dict([('貝殻', '21'), ('布団代わりのワカメ', '3'), ('サングラス', '1'), ('浮き輪', '1')])
item = Itme(item_dict)
print(item)
