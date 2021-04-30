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
    
    def print_name(self):
        print(self.name)

shop_A = CarryShop("A", "大阪")
shop_B = CarryShop("B", "名古屋")
shop_C = CarryShop("C", "北海道")

#shopps = []
#shopps.append(CarryShop("A", "大阪"))
#shopps.append(CarryShop("B", "名古屋"))
#shopps.append(CarryShop("C", "北海道"))

sell_shop = input("A B C いずれかを入力してください")
shop_name = "shop_" + sell_shop
print(shop_name)
shop_name.CarryShop.print_name()

print(CarryShop.sell(sell_shop))