class player:
    
    def __init__(self) -> None:
        self.name = ""
        self.symbol = ""
    
    def choose_name(self):
        while True:
            name = input("Enter your name (letters only): ")
            if name.isalpha():
                self.name = name
                break
            print("please enter letters only")

    def choose_symbol(self):
        symbol = input(f"Hiii {self.name}, Enter your symbol (X or O): ").upper()
        while True:
            if symbol == "X" or symbol == "O":
                self.symbol = symbol
                break
            print("please enter X or O only")