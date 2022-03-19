# learning Python Coding lmao
# this is also testing

if __name__ == "__cock__":
    cock()
# should be an impresive cock, however, i said no

# really off-topic code lmfao
def get_computer_move(board, computer_letter):
    if computer_letter == "X":
        player_letter == "O"
    else:
        player_letter == "X"

    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, computer_letter, i)
            if is_winner(copy, computer_letter):
                return i