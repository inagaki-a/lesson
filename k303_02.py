from abc import ABC, ABCMeta
from abc import abstractmethod

class Main:
    pass    


class Game:
    #初期化メソッド
    def __init__(self, title, charactor):
        self.title = title
        self.charactor = charactor
            
    #ゲーム開始
    def game_start(self):
        print(self.title + "スタート")

class Controller(metaclass = ABCMeta):
    @abstractmethod
    def up():
        pass
    
    def down():
        pass

    def left():
        pass

    def right():
        pass

class Dorakoe(Controller):
    #初期化メソッド
    def __init__(self, charactor):
        self.title = "ドラコエ"
        self.charactor = charactor
        Game.game_start(self)

    #上ボタン処理
    def up(self):
        return print(self.charactor + "上に進む")
    
    #下ボタン処理
    def down(self):
        return print(self.charactor + "下に進む")

    #左ボタン処理
    def left(self):
        return print(self.charactor + "左に進む")

    #右ボタン処理
    def right(self):
        return print(self.charactor + "右に進む")


class Streetfight(Controller):
    #初期化メソッド
    def __init__(self, charactor):
        self.title = "ストリートフォイター"
        self.charactor = charactor
        Game.game_start(self)

    #上ボタン処理
    def up(self):
        return print(self.charactor + "がジャンプする")
    
    #下ボタン処理
    def down(self):
        return print(self.charactor + "がしゃがむ")

    #左ボタン処理
    def left(self):
        return print(self.charactor + "が後に進む")

    #右ボタン処理
    def right(self):
        return print(self.charactor + "が前に進む")


dorakoe = Dorakoe('勇者')
dorakoe.up()
dorakoe.down()
dorakoe.left()
dorakoe.right()

streetfight = Streetfight('春香')
streetfight.up()
streetfight.down()
streetfight.left()
streetfight.right()