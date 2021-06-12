from typing import ItemsView
import numpy as np
from numpy.lib.function_base import append

class Player:
    def __init__(self, bag):
        '''
        初期化
        '''
        self.bag = bag

    def add_item(self, item):
        '''
        持ち物を入れる
        '''
        self.bag.getitems(item)

    def pull_item(self, item, count):
        '''
        持ち物を取り出す
        '''

    def eat_item(self, food, cnt):
        '''
        持ち物を食べる
        '''
        food_cnt = food.getCount()
        food_cnt -= cnt
        print('Playerは' + food.getName() + 'を' + str(cnt) + '個食べた')
        food.setCount(food_cnt)
        
class Bag:
    def __init__(self):
        '''
        初期化
        '''
        self.items = []


    def getitems(self, item):
        self.items.append(item)

    def items(self):
        return self.items

class Donkey:
    
    def __init__(self, bag): #初期化
        self.bag = bag

    def get_item(self, name, count):
        '''
        持ち物を入れる
        '''
        return

    def pull_item(self, item, count):
        '''
        持ち物を取り出す
        '''

    def info_item(self):
        '''
        持ち物を出力
        '''
        #bag = self.bag
        for item in self.bag.items:
            print(item.getName() + ':' + str(item.getCount()) + 'こ')


class Item:

    def __init__(self, name:str, count:int): #初期化
        self.name = name
        self.count = count

    def set_name(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setCount(self, count):
        self.count = count
    
    def getCount(self):
        return self.count

bag = Bag()
player = Player(bag)
apple = Item('リンゴ', 3)
bread = Item('パン', 5)
player.add_item(apple)
player.add_item(bread)
donkey = Donkey(bag)
donkey.info_item()
player.eat_item(apple, 2)
donkey = Donkey(bag)
donkey.info_item()
