import random

#All this code is from the text book 11.5
class Deck():
    def __init__(self, size):
        self.card_list = [i for i in range(size)]
        self.cards_in_play_list = []
        self.discards_list = []
        random.shuffle(self.card_list)
    
    def deal(self):
        if len(self.card_list) < 1:
            random.shuffle(self.discards_list)
            self.card_list = self.discards_list
            self.discards_list = []
            print('Reshuffling...!!!')
        new_card = self.card_list.pop()
        self.cards_in_play_list.append(new_card)
        return new_card
    
    def new_hand(self):
        self.discards_list += self.cards_in_play_list
        self.cards_in_play_list.clear()
        
#This is all new code.
def main():
    
#The player will be asked if they want to play.
    game = input('Would you like to play a game of Poker? ')
    
    if game.lower() == 'play':
        
#Creating the deck of cards. 
        deck = Deck(52)
        
#The players hand
        num_hand = 5
        
        hand_list = []
        
#The 5 cards in your hand.
        for i in range(num_hand):

            card = deck.deal()

            hand_list.append(card)

            print(card, end=' ')

#Ask the user if they want to exchange the cards
        exchange = input('\nWhich cards would you like to exchange? :')
        

        card_idx_to_exchange_list = exchange.split(',')
        card_idx_to_exchange_list = [int(item) for item in card_idx_to_exchange_list]
        

        for k in card_idx_to_exchange_list:

            hand_list.pop(int(k) - 1)

            hand_list.insert(int(k) - 1, deck.deal())
            

        card_idx_to_exchange_list.clear()
        
        for i in hand_list:
        
            print(i, end=' ')
        deck.new_hand()
        
#To end the game.
    elif game.lower() == 'end':
        quit()
    else:
        print('Please enter "play" to play or "end" to end the game')
        main()
        
if __name__ == '__main__':
    main()
