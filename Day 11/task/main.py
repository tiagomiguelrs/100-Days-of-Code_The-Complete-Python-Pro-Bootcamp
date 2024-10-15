from art import logo
from random import choice

# TODO-3 create a function to check whether the ace should be a 1 or an 11
def ace_value(hand):
    if len(hand) > 2 and hand[-1] == 11:
        if sum(hand) > 21:
            hand[-1] = 1
    else:
        pass
    return hand


# TODO-2 create a function that deals cards
def deal(hand):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    hand.append(choice(cards))
    hand = ace_value(hand)
    return hand


# TODO-4 create a function that deals the first two cards to the player and computer
def start():
    p_hand, c_hand = [], []
    for i in range(2):
        p_hand = deal(p_hand)
        c_hand = deal(c_hand)
    return p_hand, c_hand


# TODO-7 create a function that tells if a hand has busted
def is_busted(hand):
    if sum(hand) >= 22:
        return True
    else:
        return False


def busted(p_hand, c_hand):
    # Check whether there was a bust
    if is_busted(c_hand) and is_busted(p_hand):
        print("Both busted. It's a draw")
        return True
    elif is_busted(c_hand) or is_busted(p_hand):
        if is_busted(c_hand):
            print("Computer got busted. Player wins")
        elif is_busted(p_hand):
            print("Player got busted. Computer wins")
        return True
    # If no bust
    else:
        return False

# TODO-10 create a function that tells you who won if no busting
def who_won(p_hand, c_hand):
    if sum(p_hand) == sum(c_hand):
        print("It's a draw")
    elif sum(p_hand) > sum(c_hand):
        print("Player wins")
    else:
        print("Computer wins")


# TODO-12 create a function that deals a card to the computer if it does not have over 18
def over_18(hand):
    if sum(hand) > 18:
        pass
    else:
        return deal(hand)


# TODO-14 create a function "blackjack" that you can call
def blackjack(p_hand, c_hand):
    # TODO-5 create a loop that hands cards to the player and computer

    dealing = True
    while dealing:
        keep_dealing = input("Do you want to keep dealing? Type [y] if yes or type [n] if no.\n")
        if keep_dealing == "y":
            p_hand = deal(p_hand)

            # TODO-6 if the computer has a score of over 18 make it choose not to take cards
            c_hand = over_18(c_hand)
            print(f"Your hand: {p_hand}. Sum = {sum(p_hand)}.")
            # print(f"Computer's first card: {c_hand[0]}.")
            print(f"Computer's hand: {c_hand}. Sum = {sum(c_hand)}.")

            # TODO-8 check if any or both hands have busted
            got_busted = busted(p_hand, c_hand)
            if got_busted:
                # TODO-9 if anyone busts, stop the game
                dealing = False
        else:
            # TODO-12 if the player does not want to keep dealing, check hands
            # TODO-12 if pc has less than 18 points, take another card for it
            while sum(c_hand) < 19:
                c_hand = over_18(c_hand)
            got_busted = busted(p_hand, c_hand)
            if got_busted:
                pass
            else:
                who_won(p_hand, c_hand)
            print(f"Your hand: {p_hand}. Sum = {sum(p_hand)}.")
            print(f"Computer's hand: {c_hand}. Sum = {sum(c_hand)}.")
            dealing = False


# TODO-13 create a loop that keeps playing until you don't want more
keep_playing = True
while keep_playing:
    # TODO-14 print the logo
    print("\n" * 20)
    print(logo)

    # TODO-1 deal first two cards for player and computer

    player_hand, computer_hand = start()
    print(f"Your hand: {player_hand}. Sum = {sum(player_hand)}.")
    print(f"Computer's first card: {computer_hand[0]}.")

    blackjack(player_hand, computer_hand)

    replay = input("Do you want to play again? Type [y] for yes and [n] for no.\n")
    if replay == "y":
        pass
    else:
        keep_playing = False
