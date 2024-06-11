from Menu import menu
from Board import board
from Player import player

import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

class game:

    def __init__(self) -> None:
        self.players = [player(), player()]
        self.menu = menu()
        self.board = board()
        self.current_player = 0

    def start_game(self):
        clear_screen()
        choice = self.menu.display_main_menu()
        if choice == "1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()
    
    def setup_players(self):
        for number, player in enumerate(self.players, start=1):
            clear_screen()
            print(f"player {number}, Enter your details:")
            player.choose_name()
            player.choose_symbol()
            
    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                if self.check_win():
                    print(f"{self.players[1 - self.current_player].name} won!")
                if self.check_draw():
                    print("No one won")
                choice = self.menu.display_endgame_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break

    def play_turn(self):
        player = self.players[self.current_player]
        clear_screen()
        self.board.display_board()
        print(f"{player.name}'s turn ({player.symbol})")
        while True:
            try:
                cell_choice = int(input("Choose a cell (1-9): "))
                if 1 <= cell_choice <= 9 and self.board.update_board(cell_choice, player.symbol):
                    break
                else:
                    print("Invalid move, try again")
            except ValueError:
                print("Please enter a number between 1 and 9.")
        self.switch_player()

    def switch_player(self):
            self.current_player = 1 - self.current_player

    def check_win(self):
        winnings = [
            [0,1,2], [3,4,5], [6,7,8],      #rows
            [0,3,6], [1,4,7], [2,5,8],      #coloums
            [0,4,8], [2,4,6]                #diagonals
        ]
        for win in winnings:
            if (self.board.board[win[0]] == self.board.board[win[1]] == self.board.board[win[2]]):
                return True
        return False

    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board) 

    def restart_game(self):
        self.board.reset_board()
        self.current_player = 0
        self.play_game()

    def quit_game(self):
        print("Thank You for playing!")

game1 = game()
game1.start_game()