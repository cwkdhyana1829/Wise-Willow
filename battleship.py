from random import random, randint
import string
 
hit_board = []
enemy_board = []
for i in range(10):
    hit_board.append(["0"] * 10)
    enemy_board.append(["0"] * 10)
 
def print_board(board, title):
    print(title)
    print("    A B C D E F G H I J")
    n = 1
    for row in board:
        if n == 10:
            print(str(n) + " |" + " ".join(row))
        else:
            print(str(n) + "  |" + " ".join(row))
        n += 1
print_board(hit_board, "Hit Board")
 
class Ship:
    def __init__(self, name, size):
        self.length = size
        self.name = name
        self.positions = []
        self.direction = (int)(random() * 2) * 90
        self.damage = 0
       
        row = 0
        col = 0
        not_valid_position = True
        while not_valid_position:
            not_valid_position = False
            #choose a random position
            #horizontal
            if self.direction == 0:
                row = randint(0, (len(hit_board) - 1))
                col = randint(0, (len(hit_board[0]) - 1) - self.length)
                for i in range(self.length):
                    if enemy_board[row][col + i] == "1":
                        not_valid_position = True
                        break
            #vertical
            elif self.direction == 90:
                row = randint(0, (len(hit_board) - 1) - self.length)
                col = randint(0, (len(hit_board[0]) - 1))
                for i in range(self.length):
                    if enemy_board[row + i][col] == "1":
                        not_valid_position = True
                        break
        if self.direction == 0:
            for i in range(self.length):
                enemy_board[row][col + i] = "1"
                self.positions.append((row, col + i))
        elif self.direction == 90:
            for i in range(self.length):
                enemy_board[row +i][col] = "1"
                self.positions.append((row + i, col))


ships = []
ships.append(Ship("Terminator", 2))
ships.append(Ship("Destructor", 3))
ships.append(Ship("Wave of Power", 3))
ships.append(Ship("Warship", 4))
ships.append(Ship("Sea Queen", 5))
print_board(enemy_board, "Enemy Board")


def main():
    while (len(ships) !=0):
        guess_row = input("Enter row: ")
        guess_col = input("Enter column: ")
        if not guess_col.isalpha():
            print("Invalid input")
        elif guess_row < 1 or guess_row > 10 or guess_col < 1 or guess_col > 10:
            print("Invalid input")
            guess_col -=1
            guess_row -= 1
            if hi5_board[guess_row][guess_col] != "0":
                print("You already tried that position.")
            else:
                for ship in ships:
                    for position in ship.positions:
                        if position[] == guess_row and position[1] == guess_col:
                            hit = True

main()