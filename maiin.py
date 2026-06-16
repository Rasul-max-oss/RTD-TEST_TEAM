import random
def menu():
    print("1.подбросить монетку")
    print("2.Посмотреть историю")
    print("3.Выйти")
    
    
while True:
    menu()
    choice = input("Выберите (1-3): ")
    if choice == "1":
        input("Нажмите enter чтобы подбросить!")
        coin = random.choice(['Решка','Орёл'])

        print("Выпала:", coin)
    if choice == "2":
        print("История!")
    if choice =="3":
        print("Пока пока")
        break
    