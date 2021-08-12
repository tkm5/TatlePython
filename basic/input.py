

age = int(input("how old are you?"))
threshold = 18
game_txt = """choose game!
1: roulette
2:blackjack
3:poker
"""

if age >= threshold:
    print("you can enter casino")

    game = int(input(game_txt))
    if game == 1:
        print("roulette")
    elif game == 2:
        print("blackjack")
    elif game == 3:
        print("poker")
    else:
        print("choose 1 ~ 3")
else:
    print("you can't enter casino")

