def draw_board(position):
    print(f" {position[0]} | {position[1]} | {position[2]} ")
    print("-----------")
    print(f" {position[3]} | {position[4]} | {position[5]} ")
    print("-----------")
    print(f" {position[6]} | {position[7]} | {position[8]} ") 

# Zeichnet die Spielposition position

def check_if_valid(position, move):
    if position[move] == " ":
        return True
    else:
        return False
    
# Liefert einen boolschen Wert ob der Zug zug in der aktuellen Spielposition position möglich ist.
    
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
    
# Überprüft, ob in der Spielposition position jemand gewonnen hat. Falls ja, soll dies zurückgegeben werden. Ergänze (falls noch nicht vorhanden) die Funktion so, dass sie erkennt, wenn das Spielfeld voll ist und niemand gewonnen hat.
    
def clear_board():
    position = [" "] * 9 
    return position 
    
# Erzeugt ein leeres Spielfeld

