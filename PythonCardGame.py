import random 
class Card:
    def __init__(self,suit,rank):
        self.suit =  suit
        self.rank = rank

    def equals(self,other):
        if self.suit==other.suit and self.rank ==other.rank:
            return True
        else:
            return False 
        
    def __repr__(self):
        return self.rank+self.suit
            
    def getSuit(self):
        return self.suit
    
    def getRank(self):
        return self.rank


        

        
            

class Deck:
    deck = []
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(Card(suit,rank))
                
    deck.pop(23)

    def __init__(self,deck =[],x=0):
        if deck == [] and x == 0:
            self.deck = Deck.deck
        else:
            self.deck = deck
        


    def shuffle_deck(self):
        random.shuffle(self.deck)
    
    def deal_cards(self):
        dealer=Deck([],1)
        other=Deck([],1)
    
        for i in range(0,len(self.deck),2):
            dealer.deck.append(self.deck[i])
        for j in range(1,len(self.deck),2):
            other.deck.append(self.deck[j])
        return (dealer, other)
    
    def length(self):
        counter = 0
        for i in range(len(self.deck)):
            counter+=1
        return counter
    
    def sortdeck(self):
        n = len(self)
       
        swapped = False
        
        for i in range(n-1):
          
            for j in range(0, n-i-1):
    
             
                if self[j].rank > self[j + 1].rank:
                    swapped = True
                    self[j], self[j + 1] = self[j + 1], self[j]
            
            if not swapped:
            
                return
    
    def remove_pairs(self):
        no_pairs = Deck([],1)
        deck = Deck.sortdeck(self.deck)
        counter = 0

        test1 = self.deck[0]
        test2 = self.deck[1]
        if len(self.deck)==2 and test1.rank == test2.rank:
            no_pairs = []
            return no_pairs  
        
        for i in range(len(self.deck)-1):
            x=self.deck[i]
            y=self.deck[i+1]
            if x.rank == y.rank:
                counter+=1
            else:
                if counter% 2 ==0:
                    no_pairs.deck.append(self.deck[i])
                counter = 0 
            
        counter = 0
        n = -1
        flag = True 
        while flag:
            x = self.deck[n]
            y = self.deck[n-1] 

            if x.rank == y.rank:
                counter+=1
                n = n - 1
            else:
                if counter % 2 == 0:
                    no_pairs.deck.append(self.deck[n])
                    flag = False
                else:
                    flag = False 
        
        #random.shuffle(no_pairs)
        return no_pairs

    def __repr__(self):
        s = ''
        for card in self.deck:
            s=s+str(card)+' '

        return s 






def playGame():
        deck = Deck()
        deck.shuffle_deck()
        tmp = Deck.deal_cards(deck)
        dealer = tmp[0]
        player = tmp[1]
        
        print("Hello. My name is Robot and I am the dealer.")
        print("Welcome to my card game!")
        print("Your current deck of cards is:")
        print(player)
        print("Do not worry. I cannot see the order of your cards")

        print("Now discard all the pairs from your deck. I will do the same.")

        dealer = Deck.remove_pairs(dealer)
        player = Deck.remove_pairs(player)
        
        flag = True
        turn = 0
        while flag:
            if dealer == []:
                print('***********************************************************')
                print('Ups. I do not have any more cards\nYou lost!,I Robot,win')
                flag = False
            elif player == []:
                print('***********************************************************')
                print('Ups. You do not have any more cards\nCongratulations!You,Human,win')
                flag = False
            elif turn % 2 == 0:
                print('***********************************************************\nYour Turn\n\nYour current deck of cards is\n\n')
                print(player)
                print('\n\nI have '+str(len(dealer.deck))+' cards. If 1 stands for my first card and\n'+str(len(dealer.deck))+ ' for my last card, which of my cards would you like?')
                num = get_valid_input(len(dealer.deck)) - 1
                
                print('You asked for my '+str(num+1)+'th card.')
                print('Here it is. It is '+str(dealer.deck[num]))
                print('\nWith '+str(dealer.deck[num])+' added your current deck of cards is:\n\n')
                player.deck.append(dealer.deck[num])
                dealer.deck.remove(dealer.deck[num])
                print(player)
                player = Deck.remove_pairs(player)
                print('And after discarding pairs and shuffling, your deck is:\n\n')
                print(player)
                
                turn +=1
                wait_for_player()
            elif turn % 2 != 0:
                print('***********************************************************')
                x = random.randint(1,len(player.deck))
                dealer.deck.append(player.deck[x-1])
                player.deck.remove(player.deck[x-1])
                dealer = Deck.remove_pairs(dealer)
                print('I took your '+str(x)+'th card')
                wait_for_player()
                turn += 1

def get_valid_input(n):
     
     num = int(input('Give me an integer between 1 and '+ str(n)+ ': '))
     l = []
     for i in range(1,n+1):
         l.append(i)

     while num not in l:
         num = int(input('Invalid number. Please enter integer between 1 and '+ str(n)+ ': '))
    
    
     return num

def wait_for_player():
    try:
        input("\nPress enter to continue. ")
        print()
    except SyntaxError:
        pass

playGame()
