import random,pywhatkit,phonenumbers

def random_phone_num_generator():
    first = str(91)
    second = str(random.randint(66666, 99998)).zfill(5)
    last = (str(random.randint(1, 99998)).zfill(5))

    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 9998)).zfill(4))
    return '{}{}{}'.format(first, second, last)

n = int(input("How much mobile numbers do you want to generate: "))

for i in range(0, n):
    print('+'+random_phone_num_generator())
