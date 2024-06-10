class board:

    def __init__(self) -> None:
        self.board = [str(i) for i in range(1, 10)]

    def display_board(self):
        for x in range(0,9,3):
            print("|".join(self.board[x:x+3]))
            if x < 6:
                print("-"*5)

    def update_board(self, choice, symbol):
        while True:
            if self.is_valid_move(choice): 
                self.board[choice-1] = symbol
                return True
            return False

    def is_valid_move(self, choice):
        return self.board[choice - 1].isdigit()
    
    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]