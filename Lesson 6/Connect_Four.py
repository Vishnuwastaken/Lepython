try:
    spacer = "--**-- --**-- --**-- --**-- --**-- "

    def create_board():
        global board
        board = [
            ["#", "#", "#", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", "#", "#"],
        ]
        return

    def draw_board():
        line_skip()
        for r in range(6):
            for c in range(7):
                print(board[r][c], end=" ")
            print()

        print("1 2 3 4 5 6 7\n")
        return

    def place_piece():
        global check
        if board[i][move - 1] == "#":
            if turn % 2 == 0:
                board[i][move - 1] = "!"
            elif turn % 2 == 1:
                board[i][move - 1] = "@"
            check = True
        return

    def line_skip():
        for i in range(10):
            print()
        return

    def check_for_winning_move():
        global winner
        for c in range(4):
            for r in range(6):
                if board[r][c] == "!" and board[r][c+1] == "!" and board[r][c+2] == "!" and board[r][c+3] == "!":
                    winner = 1
                    return True
                if board[r][c] == "@" and board[r][c + 1] == "@" and board[r][c + 2] == "@" and board[r][c + 3] == "@":
                    winner = 2
                    return True
        for c in range(7):
            for r in range(3):
                if board[r][c] == "!" and board[r+1][c] == "!" and board[r+2][c] == "!" and board[r+3][c] == "!":
                    winner = 1
                    return True
                if board[r][c] == "@" and board[r+1][c] == "@" and board[r+2][c] == "@" and board[r+3][c] == "@":
                    winner = 2
                    return True
        for c in range(4):
            for r in range(3):
                if board[r][c] == "!" and board[r+1][c+1] == "!" and board[r+2][c+2] == "!" and board[r+3][c+3] == "!":
                    winner = 1
                    return True
                if board[r][c] == "@" and board[r+1][c+1] == "@" and board[r+2][c+2] == "@" and board[r+3][c+3] == "@":
                    winner = 2
                    return True
        for c in range(4):
            for r in range(3, 6):
                if board[r][c] == "!" and board[r-1][c+1] == "!" and board[r-2][c+2] == "!" and board[r-3][c+3] == "!":
                    winner = 1
                    return True
                if board[r][c] == "@" and board[r-1][c+1] == "@" and board[r-2][c+2] == "@" and board[r-3][c+3] == "@":
                    winner = 2
                    return True

    print(spacer)
    print("Fish's connect 4!\n")
    print("A python interpretation of a classic!\nIn this game, a player must have four\npieces in a row (vertically, horizontally, diagonally).")
    print(spacer)
    ready = input("Are both players ready to play? (Y/N):\n")

    if ready.lower() == "y" or ready.lower() == "yes":
        game_over = False
    else:
        game_over = True

    while not game_over:
        create_board()
        round_over = False
        turn = 0
        while not round_over:
            draw_board()
            if turn % 2 == 0:
                move = int(input("Player 1, what column would you like to place your piece?\n"))
            elif turn % 2 == 1:
                move = int(input("Player 2, what column would you like to place your piece?\n"))

            check = False
            i = 5
            while check == False:
                if i == -1 or move <= 0 or move >= 8:
                    draw_board()
                    if turn % 2 == 0:
                        move = int(input("Player 1, move is impossible where would you like your new piece?\n"))
                        i = 5
                    elif turn % 2 == 1:
                        move = int(input("Player 2, move is impossible where would you like your new piece?\n"))
                        i = 5
                else:
                    place_piece()
                i = i - 1

            if check_for_winning_move():
                round_over = True
            else:
                turn += 1
        line_skip()
        if winner == 1:
            print(f"Player 1 (!) won in {turn} turns!")
        elif winner == 2:
            print(f"Player 2 (@) won in {turn} turns!")
        again = input("Would you like to play again? (Y/N)\n")
        if again.lower() == "y" or again.lower() == "yes":
            game_over = False
        else:
            game_over = True

    line_skip()
    print(spacer)
    print(spacer, end=" ")
except:
    line_skip()
    print(spacer)
    print("You cannot enter a string into an integer! (re-run)\nThank You!")
    print(spacer, end=" ")