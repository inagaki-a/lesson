from abc import ABC
from abc import abstractmethod

class Car:
    '''
    車クラス
    '''
    def __init__(self, type: str, fuel: int, buttery: int, carpower1, carpower2):
        '''
         初期化
         '''
        self.type = type
        self.fuel = fuel
        self.buttery = buttery
        self.carpower1 = carpower1
        self.carpower2 = carpower2

    def car_run(self):
        rotation1, rotation2 = 0, 0
        if self.carpower1 != None:
            rotation1 = self.carpower1.total_rotation(self.fuel, 0)
        if self.carpower2 != None:
            rotation2 += self.carpower2.total_rotation(0, self.buttery)
        total_run = int((rotation1 + rotation2)*10 / 1000)
        return self.type + " 燃料" + str(self.fuel) + " バッテリー" + str(self.buttery) + " " + str(total_run) + "㎞ 走る"

class Car_Power(Car):
    '''
    動力
    '''
    def total_rotation(self, fuel, buttery):
        '''
        合計回転数
        '''
        #total_rotation = Gasoline_Engine.run_roatation(fuel) + Motor_Engin.run_roatation(buttery)
        print(self.carpower2)
        return total_rotation

class Gasoline_Engine(Car_Power):
    def __init__(self, fuel):
        '''
        初期化メソッド
        '''
        self.fuel = fuel

    def run_roatation(fuel):
        run = fuel * 100
        return run

class Motor_Engin(Car_Power):
    def __init__(self, buttery):
        '''
        初期化メソッド
        '''
        self.buttery = buttery

    def run_roatation(buttery):
        run = buttery * 500
        return run

gasoline_engine = Gasoline_Engine(0)
motor_engin = Motor_Engin(0)
gasoline_car = Car('Car', 100, 0, gasoline_engine, None)
print(gasoline_car.car_run())
hv_car = Car('HV', 50, 50, gasoline_engine, motor_engin)
print(hv_car.car_run())
ev_car = Car('HV', 0, 100, None, motor_engin)
print(ev_car.car_run())