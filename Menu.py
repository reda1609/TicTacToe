class menu:

    def display_main_menu(self):
        print("Welcome to my X-O game")
        print("1. Start game")
        print("2. Quit game")
        while True:
            choice = input("Enter your choice (1 or 2): ")
            if choice == "1" or choice == "2":
                break
        return choice

    def display_endgame_menu(self):
        menu_text = """
        Game Over !
        1. Restart game
        2. Quit game
        """
        print(menu_text)
        while True:
            choice = input("Enter your choice (1 or 2): ")
            if choice == "1" or choice == "2":
                break
        return choice
