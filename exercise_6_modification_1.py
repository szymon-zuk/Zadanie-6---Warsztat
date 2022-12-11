import random


def rolls():
    """
    This function calculates the dice roll from a pattern of input in format xDy+z.
    :return: int
    """
    dice_string = input("Enter which dice do you choose in format xDy+z: ")
    allowed_dice_types = [3, 4, 6, 8, 10, 12, 20, 100]
    try:
        dice_list = [x for x in dice_string]
        number_of_rolls = int(dice_list[0])
        dice_type = int(dice_list[2])
        if dice_type not in allowed_dice_types or dice_list[1] != "D":
            return "Non-existent dice type!"
        if dice_list[4:] != None:
            increased_result_list = dice_list[4:]
            increase_result = int(''.join(increased_result_list))
    except ValueError:
        return "The roll format is incorrect!"
    one_roll = random.randint(1, dice_type)
    second_roll = random.randint(1, dice_type)
    result = one_roll + second_roll + increase_result
    return result


def game2001():
    """
    Game 2001 - whoever gets 2001 points first - wins.
    :return: str
    """
    players_score = 0
    computers_score = 0
    while players_score < 2001 and computers_score < 2001:
        try:
            new_round = input("Press ENTER for next round: ")
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
            print(f"""Player has rolled: {players_round_score}. His total score now is {players_score}.
Computer has rolled: {computers_round_score}. Computer's total score is now {computers_score}""")
        except Exception:
            print("The roll format is incorrect!")


print(game2001())
