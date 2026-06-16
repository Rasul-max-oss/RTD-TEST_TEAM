print("Тест")
print("Тест2")

print("Ураа Дима привет")

def add_history(coin):
    with open('data.txt','a', encoding='utf-8') as file:
        file.write(f"{coin}\n")

import random
while True:
    input("Нажмите enter чтобы подбросить!")
    coin = random.choice(['Решка','Орёл'])
    add_history(coin)

    print("Выпала:", coin)