import random


def rolls():
    one_roll = random.randint(1, 6)
    second_roll = random.randint(1, 6)
    result = one_roll + second_roll
    return result


def game2001():
    players_score = 0
    computers_score = 0
    while players_score < 2001 and computers_score < 2001:
        new_round = input("Press ENTER: ")
        players_round_score = rolls()
        if players_round_score == 7:
            players_score = players_score // 7
        elif players_round_score == 11:
            players_score = players_score * 11
        else:
            players_score = players_score + players_round_score
        computers_round_score = rolls()
        if computers_round_score == 7:
            computers_score = computers_score // 7
        elif computers_round_score == 11:
            computers_score = computers_score * 11
        else:
            computers_score = computers_score + computers_round_score
        if players_score > 2001:
            return "Player won!"
        elif computers_score > 2001:
            return "Computer won!"
        elif new_round != "":
            print("You pressed the wrong key!")
        print(f"""Player has rolled: {players_round_score}. His total score now is {players_score}.
Computer has rolled: {computers_round_score}. Computer's total score is now {computers_score}""")


if __name__ == '__main__':
    game2001()
