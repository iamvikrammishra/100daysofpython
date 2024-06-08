import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """Returns a random card from the deck."""
    return random.choice(cards)

def calculate_score(hand):
    """Calculates the score of the given hand of cards."""

    if sum(hand) == 21 and len(hand) == 2:
        return 0  
    

    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    
    return sum(hand)

def compare_scores(user_score, computer_score):
    """Compares the user's score with the computer's score and returns the result."""
    if user_score > 21 and computer_score > 21:
        return "You both went over. It's a draw! 😅"
    if user_score == computer_score:
        return "It's a draw! 😅"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack! 😱"
    elif user_score == 0:
        return "Win with a Blackjack! 😎"
    elif user_score > 21:
        return "You went over. You lose! 😭"
    elif computer_score > 21:
        return "Opponent went over. You win! 😁"
    elif user_score > computer_score:
        return "You win! 😁"
    else:
        return "You lose! 😭"

def play_blackjack():
    """Main function to play the Blackjack game."""
    print("Welcome to Blackjack!")

    # Deal initial cards
    user_hand = [deal_card(), deal_card()]
    computer_hand = [deal_card(), deal_card()]

    is_game_over = False

    while not is_game_over:
        user_score = calculate_score(user_hand)
        computer_score = calculate_score(computer_hand)
        
        print(f"Your cards: {user_hand}, current score: {user_score}")
        print(f"Computer's first card: {computer_hand[0]}")

        # Check for end of game conditions
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == 'y':
                user_hand.append(deal_card())
            else:
                is_game_over = True

    # Dealer's turn to draw cards
    while computer_score != 0 and computer_score < 17:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)

    print(f"Your final hand: {user_hand}, final score: {user_score}")
    print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
    print(compare_scores(user_score, computer_score))

play_blackjack()
