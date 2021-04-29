def homeoutdef(num):
    homeout = "【玄関に向かう】\n立ち上がる\n廊下を歩く\n扉を開ける"
    return homeout

def shoppingdef(num):
    if num == 1:
        shopping = ("【買いに行く】\n道を歩く\nお金を入れる\n飲み物を選択する")
    elif num == 2:
        shopping = ("【買いに行く】\n自転車に乗る\nコンビニに向く\n自転車を走らせる\nコンビニに入る\n飲み物を選択する\nレジに向かう\nお金を払う")
    return shopping

def rehomedef(num):
    if num == 1:
        rehome = ("【戻る】\n道を歩く\n扉を開ける\n廊下を歩く")
    elif num == 2:
        rehome = ("【戻る】\n自転車に乗る\n自宅に向く\n自転車を走らせる\n扉を開ける\n廊下を歩く")
    return rehome

def drinkdef(num):
    drink = ("【飲む】\n栓を開ける\n飲む")
    return drink

num =int(input("何を飲みますか？1: コーラ 2: ポーション"))
process = homeoutdef(num) +"\n\n" + shoppingdef(num) +"\n\n" + rehomedef(num) +"\n\n" + drinkdef(num)
print(process)