#Создайте программу для игры в ""Крестики-нолики"".

play_active = True
curent_player = 'X'

playboard = [" ",
             "1","2","3",
             "4","5","6",
             "7","8","9"]

def playboard_initiation():
    print (playboard[1] + "  " + playboard[2] + "  " + playboard[3] )
    print (playboard[4] + "  " + playboard[5] + "  " + playboard[6] )
    print (playboard[7] + "  " + playboard[8] + "  " + playboard[9] )

def player_entry():
    global play_active
    while True:
        move = input("Пожалуйста, укажите номер поля: ")
        
        if move == 'q':
            play_active = False
            return
        try:
            move = int(move)
        except ValueError:
            print("Пожалуйста, введите число от 1 до 9")
        else:
            if move >= 1 and move <= 9:
                if playboard[move] == 'X' or playboard[move] == 'O':
                    print("Это поле занято, укажите другое число!")
                else:
                    return move
            else:
                print("Число должно быть от 1 до 9")
def change_player():
    global curent_player
    if curent_player == 'X':
        curent_player = 'O'
    else:
        curent_player = 'X'

def check_winner():
   
    if playboard[1] == playboard[2] == playboard[3]:
        return playboard[1]
    if playboard[4] == playboard[5] == playboard[6]:
        return playboard[4]
    if playboard[7] == playboard[8] == playboard[9]:
        return playboard[7]
   
    if playboard[1] == playboard[4] == playboard[7]:
        return playboard[1]
    if playboard[2] == playboard[5] == playboard[8]:
        return playboard[2]
    if playboard[3] == playboard[6] == playboard[9]:
        return playboard[3]
  
    if playboard[1] == playboard[5] == playboard[9]:
        return playboard[5]
    if playboard[7] == playboard[5] == playboard[3]:
        return playboard[5]
        
def ckeck_draw():
    if (playboard[1] == 'X' or playboard[1] == 'O') \
      and (playboard[2] == 'X' or playboard[2] == 'O') \
      and (playboard[3] == 'X' or playboard[3] == 'O') \
      and (playboard[4] == 'X' or playboard[4] == 'O') \
      and (playboard[5] == 'X' or playboard[5] == 'O') \
      and (playboard[6] == 'X' or playboard[6] == 'O') \
      and (playboard[7] == 'X' or playboard[7] == 'O') \
      and (playboard[8] == 'X' or playboard[8] == 'O') \
      and (playboard[9] == 'X' or playboard[9] == 'O'):
        return ('ничья')
        
playboard_initiation()
while play_active:
    print()
    print ("Игрок " + curent_player + " ваш ход ")
    mover = player_entry()
    if mover:
        playboard[mover] = curent_player
        playboard_initiation()
        winer = check_winner()
        if winer:
            print ("Игрок " + winer + " победил!")
            play_active = False
            break
        draw = ckeck_draw()
        if draw:
            print ("Игра закончилась вничью")
            play_active = False
        change_player()
print() 