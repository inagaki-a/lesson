class CarryShop:
    stock = 10

    #初期化メソッド
    def __init__(self, id, name): #初期化
        self.id = id
        self.name = name 

    #売るメソッド
    def sell(self):
        stock = int(CarryShop.stock) - 1
        CarryShop.stock = stock
        return stock
    
    def get_name(self):
        return self.id +  ":" + self.name

shop_A = CarryShop("A", "大阪")
shop_B = CarryShop("B", "名古屋")
shop_C = CarryShop("C", "北海道")

#shopps = []
#shopps.append(CarryShop("A", "大阪"))
#shopps.append(CarryShop("B", "名古屋"))
#shopps.append(CarryShop("C", "北海道"))


while CarryShop.stock != 0:
    print("在庫" + str(CarryShop.stock))
    print(shop_A.get_name(), shop_B.get_name(), shop_C.get_name())
    sell_shop = input("A B C いずれかを入力してください")

    if sell_shop == "A":
        print(shop_A.sell())
    elif sell_shop == "B":
        print(shop_B.sell())
    elif sell_shop == "C":
        print(shop_C.sell())
    else:
        print("存在しません")
        exit
print("在庫切れ　閉店です")

#shop_name = str("shop_" + str(sell_shop))
#print(shop_name)
#print((shop_name).sell())