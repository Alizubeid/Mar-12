from random import choice
num = "1234567890"
abc = "abcdefghijklmnopqrstuvwxyz"
ABC = abc.upper()
symbols = "~!@#$%^&*()"
all_models = [num, abc, ABC, symbols]


def genrate_password(value: list, num, count):
    for i in range(count):
        so = ""
        for i in range(num):
            so += choice(choice(value))
        yield so


[print(i) for i in genrate_password(all_models, 20, 10)]
