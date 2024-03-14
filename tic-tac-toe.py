position = [" "] * 9  # Erzeugt ein leeres Spielfeld

def draw_board(position):
    print(f" {position[0]} | {position[1]} | {position[2]} ")
    print("-----------")
    print(f" {position[3]} | {position[4]} | {position[5]} ")
    print("-----------")
    print(f" {position[6]} | {position[7]} | {position[8]} ")

draw_board(position)

def check_if_valid(position, move):
    if position[move] == " ":
        return True
    else:
        return False
    
def check_win_condition(liste):
    if liste[0] == liste[1] == liste[2] and liste[0] != " ":
        return True
    elif liste[3] == liste[4] == liste[5] and liste[3] != " ":
        return True
    elif liste[6] == liste[7] == liste[8] and liste[6] != " ":
        return True
    elif liste[0] == liste[3] == liste[6] and liste[0] != " ":
        return True
    elif liste[1] == liste[4] == liste[7] and liste[1] != " ":
        return True
    elif liste[2] == liste[5] == liste[8] and liste[2] != " ":
        return True
    elif liste[0] == liste[4] == liste[8] and liste[0] != " ":
        return True
    elif liste[2] == liste[4] == liste[6] and liste[2] != " ":
        return True
    else:
        return False

player1 = input("Spieler 1, bitte gib deinen Namen ein: ")
print(f"Dein Name: {player1}")
player2 = input("Spieler 2, bitte gib deinen Namen ein: ")
print(f"Dein Name: {player2}")

while True:
    draw_board(position)
    valid_move = False
    
    while not valid_move:
        # Zug von Spieler 1
        player1_zug = int(input("Spieler 1, bitte gib deinen Zug ein: "))
        
        # Ist der Zug spielbar?
        valid_move = check_if_valid(position, player1_zug)
        position[player1_zug] = "x"  # Spiele Zug
        draw_board(position)
        
        # Hat Spieler 1 gewonnen?
        if check_win_condition(position):
            # Hier fehlt noch der entsprechende Code für den Gewinnfall
            print(f"Herzlichen Glückwunsch, {player1}! Du hast das Spiel gewonnen.")
            break

    valid_move = False
        
    while not valid_move:
        # Zug von Spieler 2
        player2_zug = int(input("Spieler 2, bitte gib deinen Zug ein: "))
        
        # Ist der Zug spielbar?
        valid_move = check_if_valid(position, player2_zug)
        position[player2_zug] = "o"  # Spiele Zug
        draw_board(position)

        # Hat Spieler 2 gewonnen?
        if check_win_condition(position):
            # Hier fehlt noch der entsprechende Code für den Gewinnfall
            print(f"Herzlichen Glückwunsch, {player2}! Du hast das Spiel gewonnen.")
            break
        
    valid_move = False

