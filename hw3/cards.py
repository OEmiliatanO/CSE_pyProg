import random
class Hand():
    """The cards class has the following:
       - A PRIVATE class attribute "__deck" that holds a list of numbers. This
         attribute must be initialized to hold a randomized list of all of the
         numbers from 0 to 51. It must be initialized using list comprehension.
       - A PRIVATE class attribute "__players" that is initialized to an empty
         list.
       - A classmethod named "new", which: 1) resets the class attribute to a
         new randomized list of 52 numbers, and 2) for each item in __players,
         discard all of that item's cards. 
       - A classmethod named "deal" that returns the value it pops from __deck
         (Recall that __deck is a list, so it has a pop method). If __deck is
         empty, it must not give an error, but instead return the value of 52.
  
    Objects of the Hand class also have the following regular methods defined: 
       __init__, __len__, __str__, __le__, __lt__, __ge__, __gt__, __eq__,
       __ne__, __iter__, __getitem__, __delitem__, sort, display, discard,
       retire.

    They also have a private method __score (which I've written for you).   """
    
    __deck = [x for x in range(52)]
    random.shuffle(__deck)
    __players = []
    
    @classmethod
    def new(cls):
        cls.__deck = [x for x in range(52)]
        random.shuffle(cls.__deck)
        for player in cls.__players:
            player.hand = []

    @classmethod
    def deal(cls):
        if len(cls.__deck) > 0: return cls.__deck.pop()
        return 52

    def __init__(self, num=5): 
        """This creates a new player by:
           1. Adding itSELF to the class attribute "__players".
           2. Creating a normal attribute named "hand". Create it this way:
                - It must be created with a list comprehension.
                - It must get its elements by calling the "deal" class method
                  a total of "num" times.
                - If the card that is return by deal has the value of 52, then
                  do not add that value into "hand".                       """
        def faceOf(x):
            return ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'][x%13] + "♠♣♦♥"[x//13]
        Hand.__players.append(self)
        self.hand = [faceOf(x) for i in range(num) if ((x:=Hand.deal()) != 52)]

    def __len__(self): 
        """Returns the number of cards in the hand (usually, it is 5).   """
        if self not in Hand.__players:
            raise IndexError
        return len(Hand.__players[Hand.__players.index(self)].hand)

    def __str__(self):
        """This uses the code from the earlier homework to return a string
        describing what the score of this hand is. There are rules that make
        it a little bit more complicated than in the prior homework however:

          1. If the hand does not have exactly five cards, then return:
               "incomplete hand"

          2. If it is just a high card, return "Ace high", "King high", "Queen
               high", "Jack high", "Ten high", "Nine high", etc

          3. If it is one pair, return: "two Aces", "two Kings","two Queens",
               "two Jacks", "two Tens", "two Nines", ... or "two Twos".
        
          4. If it is three of a kind, return: "three Aces", "three Kings",
               "three Queens", ... or "three Twos".
        
          5. If it is two pair, return: "two pair: Aces and Kings", etc
        
          6. If it is full house, return: "full house: Aces and Kings", "full
             house: Sevens and Fours", "full house: Fours and Sevens", etc.
             Note that case the card that had 3 matches must go first (that is
             why the "Sevens and Fours" differs from "Fours and Sevens").

          7. If it is four of a kind, return: "four Aces", "four Kings", "four
             Queens", "four Jacks", "four Tens", "four Nines", etc.

          8. If it is a royal straight flush, return: "royal straight flush".
        
          9. If it is a straight flush, return: "straight flush, King high", or
             "straight flush, Jack high", "straight flush, Nine high", etc.

          10.If it is a flush, return: "flush, King high", "flush Nine high",
             etc.
        
          11. If it is a royal straight, return: "royal straight"

          12.If it is a straight, return: "straight, King high", or "straight
             Jack high", "straight, Nine high", etc.                      """
        NumtoWord = {'A': 'Aces', 14: 'Aces', '2': 'Twos', 2: 'Twos', '3': 'Threes', 3: 'Threes', '4': 'Fours', 4: 'Fours', '5': 'Fives', 5: 'Fives', '6': 'Sixs', 6: 'Sixs', '7': 'Sevens', 7: 'Sevens', '8': 'Eights', 8: 'Eights', '9': 'Nines', 9: 'Nines', '10': 'Tens', 10: 'Tens', 'J': 'Jacks', '11': 'Jacks', 11: 'Jacks', 'Q': 'Queens', '12': 'Queens', 12: 'Queens', 'K': 'Kings', '13': 'Kings', 13: 'Kings'}

        if len(self.hand) <  5:
            return "incomplete hand"

        F, S = zip(*self.hand)
        F = [x[:-1] for x in self.hand]
        S = [x[-1:] for x in self.hand]

        flush = all(x == S[0] for x in S)

        counts = [F.count(x) for x in F]

        if 4 in counts: return "four " + NumtoWord[F[counts.index(4)]]

        elif 3 in counts and 2 in counts: return "full house: " + NumtoWord[F[counts.index(3)]] + " and " + NumtoWord[F[counts.index(2)]]

        elif 3 in counts: return "three " + NumtoWord[F[counts.index(3)]]

        elif counts.count(2) == 4:
            s = set()
            for x in enumerate(counts):
                if x[1] == 2:
                    s.add(F[x[0]])
            return "two pair: " + NumtoWord[s.pop()] + " and " + NumtoWord[s.pop()]

        elif counts.count(2) == 2: return "two " + NumtoWord[F[counts.index(2)]]

        else:
            mapp = {'J':11, 'Q':12, 'K':13, 'A':14}
            for key in mapp:
                while key in F:
                    F[F.index(key)] = mapp[key]
            F = [int(x) for x in F]
            F.sort()

            if F[0] == 10 and F[4] == 14:
                if flush:
                    return "royal straight flush"
                else:
                    return "royal straight"

            elif (F[0] == 2 and F[3] == 5 and ((high := F[4]) == 14)) or any(F[0] == x and ((high := F[4]) == x + 4) for x in range(2,10)):
                if flush:
                    return "straight flush, " + NumtoWord[high] + " high"
                else:
                    return "straight, " + NumtoWord[high] + " high"

            elif flush: "flush, " + NumtoWord[F[4]]
            else: return NumtoWord[F[4]] + " high"

    def __score(self):
        """I am giving you this function. It uses __str__ to score the hand
        as a 3-digit floating point number, according to the rules of poker.
        Technically, there are a few cases where to hand will score the same,
        even though the rules of poker define a tie-breaker. That is not
        important, however, and this function works well enough. """
        S=self.__str__().replace('royal straight','straight Ace high').replace('straight Ace high flush','flush Ace high').replace('straight flush','flush straight')
        if S[0].islower(): S = "one "+S
        code={'Two':'02','Three':'03','Four':'04','Five':'05','Six':'06',
              'Seven':'07','Eight':'08','Nine':'09','Ten':'10','Jack':'11',
              'Queen':'12','King':'13','Ace':'14','incomplete hand':'000',
              'one ':'0','two ':'1','1pair: ':'2','one pair: ':'2',
              'three ':'3','straight':'4','flush':'5','full house: ':'6',
              'four ':'7','s':'',' and ':'.',' high':''}
        for k in code: S=S.replace(k,code[k])
        return float(S.replace(' ',''))

    def __le__(self, otherHand):
        """Returns True if this hand is <= the otherHand.
        (Use __score() to get their values to compare.)   """
        return self.__score() <= otherHand.__score()

    def __lt__(self, otherHand):
        """Returns True if this hand is < the otherHand.
        (Use __score() to get their values to compare.)   """
        return self.__score() < otherHand.__score()

    def __ge__(self, otherHand):
        """Returns True if this hand is >= the otherHand.
        (Use __score() to get their values to compare.)   """
        return self.__score() >= otherHand.__score()

    def __gt__(self, otherHand):
        """Returns True if this hand is > the otherHand.
        (Use __score() to get their values to compare.)   """
        return self.__score() > otherHand.__score()

    def __eq__(self, otherHand):
        """Returns True if this hand is == the otherHand.
        (Use __score() to get their values to compare.)   """
        return self.__score() == otherHand.__score()

    def __ne__(self, otherHand):
        """Returns True if this hand is != the otherHand.
        (Use __score() to get their values to compare.)   """
        return self.__score() != otherHand.__score()

    def __iter__(self):
        """This allows you to iterate over the cards in the hand, returning on
        each iteration a number between 0 and 51. """
        return iter(self.hand)

    def __getitem__(self, pos):
        """This lets you index a card in the hand by its position. If the
        position is out of range or isn't an integer, then raise IndexError."""
        return self.hand[pos]

    def __delitem__(self, pos):
        """This lets you delete a card from the hand by its position.
        position is out of range or isn't an integer, then raise IndexError."""
        del self.hand[pos]

    def sort(self):
        """This sorts the hand's cards, in place, based on card values (which
        is to say, based on their numbers from 0 to 51). In the sort, the
        highest card goes on the left (ie, in the zeroeth list-position).    """
        self.hand.sort()

    def display(self):
        """This prints the hand, in this format:
        ┏━━━━┓   ┏━━━━┓   ┏━━━━┓   ┏━━━━┓   ┏━━━━┓
        ┃5♣  ┃   ┃K♠  ┃   ┃10♥ ┃   ┃7♣  ┃   ┃A♠  ┃
        ┃    ┃   ┃    ┃   ┃    ┃   ┃    ┃   ┃    ┃
        ┃    ┃   ┃    ┃   ┃    ┃   ┃    ┃   ┃    ┃
        ┃    ┃   ┃    ┃   ┃    ┃   ┃    ┃   ┃    ┃
        ┗━━━━┛   ┗━━━━┛   ┗━━━━┛   ┗━━━━┛   ┗━━━━┛   

        Note: the "10" take up 2 characters.
        Note also: there may be any number of cards, but it does not need to
        display properly, if there are more than 9.                        """

        print("┏━━━━┓   ┏━━━━┓   ┏━━━━┓   ┏━━━━┓   ┏━━━━┓")
        print(" ", end = '')
        for i in range(5):
            print("|", self.hand[i], '|', end = '   ')
        print("\n┃    ┃   ┃    ┃   ┃    ┃   ┃    ┃   ┃    ┃\n┃    ┃   ┃    ┃   ┃    ┃   ┃    ┃   ┃    ┃\n┃    ┃   ┃    ┃   ┃    ┃   ┃    ┃   ┃    ┃\n┗━━━━┛   ┗━━━━┛   ┗━━━━┛   ┗━━━━┛   ┗━━━━┛   ")

    def discard(self, pos, replace = True):
        """This removes the card at the indicated position, and then calls
        the deal method to replace the card, if the replace variable is True."""
        def faceOf(x):
            return ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'][x%13] + "♠♣♦♥"[x//13]
        if replace:
            self.hand[pos] = faceOf(Hand.deal())
        else:
            del self.hand[pos]

    def retire(self):
        """This removes myself from list class attribute holding the list of
        players."""
        Hand.__players.remove(self)
        del self

player1,player2,player3=Hand(),Hand(),Hand()
print(player1,":")
player1.display()
print()
print(player2,":")
player2.display()
print()
print(player1<player2)
print()
player2.discard(3)
player2.discard(4)
player2.display()
print()
player2.discard(4,replace=False)
print(len(player2))

player1.retire()
Hand.new()
print(len(player2))
try:
    print(len(player1))
except:
    print("Player 1 retired")