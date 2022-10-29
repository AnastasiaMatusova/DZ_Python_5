#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

from random import randint

def input_data(name):
    x = int(input(f"{name}, сколько конфет (от 1 до 28) вы хотите взять: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, сколько конфет (от 1 до 28) вы хотите взять: "))
    return x

def data_player(name, candies_numbers, curent_balance, Total_candies):
    print(f" {name} взял {candies_numbers} конфет, теперь у него {curent_balance} конфет. На столе у нас {Total_candies} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
Total_candies = randint(2021, 2022)
print(f'Уважаемые игроки, На столе осталось {Total_candies} конфет')
first_mover = randint(0, 2)  

if first_mover:
    print(f"Первый ход {player1}")
else:
    print(f"Первый ход {player2}")

curent_balance1 = 0
curent_balance2 = 0

while Total_candies > 28:
    if first_mover:
        candy_numbers = input_data(player1)
        curent_balance1 += candy_numbers
        Total_candies -= candy_numbers
        first_mover = False
        data_player(player1, candy_numbers, curent_balance1, Total_candies)
    else:
        candy_numbers = input_data(player2)
        curent_balance2 += candy_numbers
        Total_candies -= candy_numbers
        first_mover = True
        data_player(player2, candy_numbers, curent_balance2, Total_candies)

if first_mover:
    print(f"Поздравляем {player1}, вы победили!")
else:
    print(f"Поздравляем {player2}, вы победили!")

# С ботом не успеваю разобрать.