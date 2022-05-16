from random import shuffle, randrange, sample
NUMCARD = 52 #For debugging, you can try MAXCARD=7, to prove that your codes
             #don't get repeats.

def faceOf(x):
	"""This receives a number below 52 and returns a string of 2-3 characters,
	representing the face and suit of the card mapping to that number.
	The mapping is as follows: 0=>'2♠', 1=>'3♠',...7=>'9♠', 8=>'10♠', 9=>'J♠',
	10=>'Q♠', 11=>'K♠', 12=>'A♠', 13=>'2♣',...25=>'A♣', 26=>'2♦', 38=>'A♦',
	39=>'2♥', 51=>'A♥' """
	return ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'][x%13] + "♠♣♦♥"[x//13] #<=Fill in the blank


# Throughout the following, follow these rules:
#   The term "a shuffled deck" refers to a list of the numbers 0 through 51,
#     arranged in random order.
#   If you are told to "complete the command", then that means that you cannot
#     make new commands. So, you could not insert a ";" or create a multi-line
#     answer (unless it is just a command that is so long that you continued
#     it on another line).


#---------------------------------------------#
#This part creates the list variable "deckV1" #
#---------------------------------------------#
#Complete the following command to create a shuffled deck. Your solution must 
#use expression assignment (See the end of Lecture 10, and also lecture 11):
shuffle(deckV1:=[x for x in range(NUMCARD)])


#------------------------------------------------------------------#
#This part creates the memoryview of a bytearray variable "deckV2" #
#------------------------------------------------------------------#
#Complete the following command to create a shuffled deck. Your solution must
#use be a memory view of a bytearray (See Lecture 11):
deckV2=memoryview(bytearray(sample(range(NUMCARD), NUMCARD)))

#-----------------------------------------------------------#
#This part uses functional programming to display the cards #
#-----------------------------------------------------------#
def printdeckV3():
	"""This part won't create a deckV3 variable, since functional programming
	doesn't use assigment statements. 

	You will, however, need  to use an assignment expression to remember which
	cards were dealt into the hand, so that those cards can be FILTERed out of
	the SAMPLE you will choose to take 2 more cards from. In the blank below,
	provide arguments to the function call of print.

	Note that you cannot use any "[" or "]" symbols."""
	print("Hand:", (deckV3:=list(map(faceOf, sample(range(NUMCARD), NUMCARD)))).__getitem__(slice(0,5)), "\nTwo more cards:", deckV3.__getitem__(slice(5,7)))


#---------------------------------------------------#
# This part creates a generator function for deckV4 #
#---------------------------------------------------#
def gendeckV4():
	"""This generator takes no arguments and returns a new, non repeating card
	each time it is invoked (eg, with a next command). 

	Now the idea of a generator function is that it doesn't contain the things
	it will generate. (I do let you keep a list previously-generated values,
	just not a list of not-yet generated values).

	So there is a rule for how this generator function chooses the new card:
	 - You must keep choosing a random number below NUMCARD, until a number
	   is found that has not been generated earlier.                       """
	out = []
	while True:
		x = randrange(0, NUMCARD)
		if x in out: continue;
		out.append(x)
		yield x

#--------------------------------------------#
# This part creates the generator for deckV5 #
#--------------------------------------------#
def gendeckV5():
	"""This generator takes "hand" and "take2" as arguments and returns a new,
	non repeating card each time it is invoked (eg, with a next command).

	As with gendeckv4, you will need a list previously-generated values.

	A new rule for gendeckV5 is that you must choose the next card by using a
	random number that identifies its ordered position among the remaining,
	not-yet-generated cards.
	What I mean is: Suppose you set NUMCARD=10. And suppose that the numbers
	                0, 2, 5, 7, 8 and 9 had already been chosen before.
	                In that case there are 4 choices, not 10: (1, 3, 4 and 6).
	                So you would generate a random number below 4, and then
	                you convert it by ordered position: 0=>1,1=>3,2=>4,3=>6.

	                Note that this version is more efficient than gendeckV4's
	                looping approach.                                     """
	qu = [*range(NUMCARD)]
	while True:
		x = randrange(len(qu))
		yield qu[x]
		del qu[x]
