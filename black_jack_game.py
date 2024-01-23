import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]
                      for value in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def calculate_score(self):
        score = 0
        aces = 0
        for card in self.hand:
            value = card.value
            if value.isdigit():
                score += int(value)
            elif value in ["J", "Q", "K"]:
                score += 10
            else:
                aces += 1
                score += 11

        while score > 21 and aces > 0:
            score -= 10
            aces -= 1

        return score

def play_blackjack():
    player = Player("Player")
    dealer = Player("Dealer")
    deck = Deck()
    deck.shuffle()

    for _ in range(2):
        player.add_card(deck.deal())
        dealer.add_card(deck.deal())

    print(f"{player.name}: {player.hand} - Score: {player.calculate_score()}")
    print(f"{dealer.name}: [{dealer.hand[0]}, XX]")

    while player.calculate_score() < 21:
        move = input("Do you want to hit or stand? ").lower()
        if move == "hit":
            player.add_card(deck.deal())
            print(f"{player.name}: {player.hand} - Score: {player.calculate_score()}")
        elif move == "stand":
            break
        else:
            print("Invalid input. Please choose to hit or stand.")

    dealer_score = dealer.calculate_score()
    while dealer_score < 17:
        dealer.add_card(deck.deal())
        dealer_score = dealer.calculate_score()

    print(f"{dealer.name}: {dealer.hand} - Score: {dealer.calculate_score()}")

    player_score = player.calculate_score()

    if player_score > 21:
        print("Player busts! Dealer wins.")
    elif dealer_score > 21:
        print("Dealer busts! Player wins.")
    elif player_score > dealer_score:
        print("Player wins!")
    elif dealer_score > player_score:
        print("Dealer wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    play_blackjack()