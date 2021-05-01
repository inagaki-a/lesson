from functools import singledispatch

@singledispatch
def action(num: int):
    print(str(num) + "㎞で走る")

@action.register
def _(text: str):
    print("あるく")

action(10)
action('歩く')

