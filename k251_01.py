from typing import ItemsView


class Player:
    items = dict()

    def __init__(self, name, level, items: dict): #初期化
        self.name = name
        self.level = level
        self.bag = Bag(items)

    def info(self):
        '''
        プレイヤーの情報を表示
        '''
        return "Player Name:" + self.name + "Level:" + str(self.level)

    def get_itme(self, item):
        '''
        アイテムを取得する
        '''
        if self.items == []:
            self.items = { item.get_name() : item.get_count()}
        else:
            self.items[item.get_name()] = item.get_count()

    def hold_items(self, item):
        '''
        保持しているアイテム情報
        '''
        return self.items.get(item)
    
class Item:
    def __init__(self, name, count):
        self._name = name
        self._count = count
    
    def item_list(self):
        return Player.itnems

    def get_name(self):
        return self._name
    
    def get_count(self):
        return self._count

class Bag:

    def getitems(item):
        items = item


calypso = Player("カリピュソー", 99, [])
item1 = Item('貝殻', 21)
item2 = Item('布団代わりのワカメ', 3)
item3 = Item('サングラス', 1)
item4 = Item('浮き輪', 1)
calypso.get_itme(item1)
calypso.get_itme(item2)
calypso.get_itme(item3)
calypso.get_itme(item4)

print(calypso.hold_items("貝殻"))