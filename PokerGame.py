'''
Function:deal cards and compare the size of poker points

CODING BY YOUNG
     2016-04-02
'''
import random, time    #import lib about random and time(for sleep())
poker = [[0 for col in range(13)] for line in range(4)]    #2 d array for 52 cards, 0 refers available

class Poker(object):    #associates cards' suits and ranks with numbers 
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def card_desc(self):
        suits = {3:'SPADE', 2:'HEART', 1:'CLUB', 0:'DIAMOND'}    #S is biggest and D is smallest when compare
        ranks = {0:'2', 1:'3', 2:'4', 3:'5', 4:'6', 5:'7', 6:'8',    #A is biggest and 2 is smallest when compare
                 7:'9', 8:'10', 9:'J', 10:'Q', 11:'K', 12:'A'
                 }
        print(suits.get(self.suit),ranks.get(self.rank))    #output cards info when calling Poker.card_desc
        
class Player(object):
    
    score = 0    #players' score
    
    def dealcard(self):    #deal card for player and call Poker class to output card's suit and rank
        while(1):
            rank = random.randint(0,12)    #0<= rank <= 12, 0 refer rank 2 and 12 refer rank Ace
            suit = random.randint(0,3)    #3 refer S and 0 refer D
            if poker[suit][rank] == 0:    #search 2-d array 'poker', 0 refers available
                self.suit = suit    #store suit and rank temp, for function "compare"
                self.rank = rank
                poker[suit][rank] = 1    #set flag to array poker
                card = Poker(suit, rank)    #call Poker class
                card.card_desc()    #call func "card_desc()" to output the card's suit and rank with random number 
                return    #jump out of the circle
            else:
                pass    #continue generating random number to find available card
            
def compare(suit1, rank1, suit2, rank2):    #compare two cards, return 0 if former is bigger, else return 1
    if rank1 == rank2:
        if suit1 > suit2:    #S>H>C>D
            return 0
        else:
            return 1
    elif rank1 > rank2:    #don't need to compare suit when ranks different
        return 0
    else:
        return 1
    
if __name__ == '__main__':    #entry, the same to C's "int main(void){}"
        
    player1 = Player()    #call class Player
    player2 = Player()
    
    while(1):
        print("Player1 get :", end = '')
        player1.dealcard()    #call function "dealcard()" in class Player
        print("Player2 get :", end = '')
        player2.dealcard()
        if not compare(player1.suit, player1.rank, player2.suit, player2.rank):    #if 1, continue running
            player1.score += 1    #player1 got bigger card, score++
            print("Player1's score: ",player1.score)
            print("Player2's score: ",player2.score, end = '\n\n')
        else:
            player2.score += 1
            print("Player1's score: ",player1.score)
            print("Player2's score: ",player2.score, end = '\n\n')
        if player1.score > 13:    #win when score hits 14 or draw when two players' score both hit 13
            print('Player1 win!!!')
            exit(0)
        elif player2.score > 13:
            print('Player2 win!!!')
            exit(0)
        elif player1.score == 13 and player2.score ==13:
            print("Draw!!!")
            exit(0)
        else:
            pass
        time.sleep(2)    #simulate dealing cards
