# This file is the full version of the homework, which you should only work
# on once you get pokerBasic.py to work. Read that file before reading this
# file...

# The code below contains 30 numbered steps. In each step, you must follow
# the instructions for that part.
# In some cases, the step requires you to fill in a blank (____). In these
# cases, the text you add cannot include a ";" symbol because you are just
# supposed to complete the partially-provided Python statement. 
# In other cases the step requires that a ... be replaced. In these cases,
# you may use multiple statements (on multiple lines and/or separated by ';')

# As we know, this is the full version of the homework. As such, there will
# be certain step where I introduce specific REQUIREMENTS on how they step is
# to be implemented. To get the points for such a step, you must follow its
# requirements. For example, suppose that there was one step where you didn't
# follow the requirement, but the code still works, nonetheless. Well, in
# such a case, we know a few things: 1) you will get at least 60%, because
# the code works and these REQUIREMENTS were not a part of pokerBasic.py. And
# 2) You will get more than 60%, because only one requirement was not met,
# meaning that most of the requirements described below were met.

# The code below contains 30 numbered steps (whereas the basic version had 22
# steps, because it ignored straights and flushes). OK, let's see the steps:



# 1.
# This line defines the deck of 52 cards.
# In the basic version I gave you a direct answer for a list with each of the
# 52 values. In this better version, however, you must compute these 52 card
# values, all on one line.
# REQUIREMENTS:
#  In filling in the blank below, you can only use these functions: zip(),
#     range(), chr().
#  In filling in the blank, you CANNOT use any of these: 5, 6, ♣, ♠, ♦, or ♥.
#     Hints: As stated, you can't use a "♣" symbol-- but you can use ord("♣")
#              to find its unicode value, then you use that value in a chr().
#            Similarly, you can't use a "6", but you can use a range() to
#              create an object that contains a 6.
#
# So, following the above rules, fill in the blank below:
deck=[(f,s) for (f,s) in zip([*range(2,11),'J', 'Q', 'K', 'A'] * 4,[chr(ord('♣')),chr(ord('♠')),chr(ord('♦')),chr(ord('♥'))] * 13)]

# If your above code is correct, then pasting the [___] into interactive mode
# should produce the same list values as what was provided for you in the
# pokerBasic.py file. Note: the order of these 52 cards is not important, but
# my implementation created the order provided in pokerBasic.py.


# 2.
# This step shuffles the deck. It is the same as for pokerBasic.py.
import random
random.shuffle(deck)

# 3.
# This step puts 5 cards from the deck into your hand. Same as pokerBasic.py.
phand = deck[:5]
del deck[:5]

# 4.
# This line is the header of a loop that runs 3 times. Same as pokerBasic.py.
for Round in range(3):
    
#   5.
#   Now you are in the loop body. For the body's first line, simply type:
    print("You Have:",end=" ")

#   6.
#   This next line loops over the card in your hand, but it does it better
#   than in the basic version.
#   REQUIREMENT: To keep track of the indices of the cards as you loop over
#                them, you must use enumerate (see lecture 4, slide 94)
    for [n, val] in enumerate(phand):
        
#       7.
#       This prints the cards, but has extra rules beyond the basic version.
#       REQUIREMENTS:
#        1) Because we have improved step 6, we now know the index and must
#           use it to print a letter ('a.' to 'e.') along with the card.
#        2) You must use splat on the variable representing the card, thereby
#           turning its face and its suit into two arguments of the print.
        print(chr(ord('a')+n) + '.', *val, end = '  ')
    

#   8.
#   Asks the user for input on which cards to discard. Same as pokerBasic.py.
    todiscard = input("\nEnter the letters (a-e) all of the cards you want to discard:").strip()

#   9.    
#   This loops through the characters the user inputted. But, unlike in the
#   basic version, we will consider cases where the user types weird input,
#   and it must still work. (And note that you answer goes in a ____, so you
#   aren't allowed to use multiple statements.)
#   REQUIREMENTS:
#   1) Any upper case inputted letters should get converted to lower case.
#      Hint: Lecture 3, slide 46. 
#   2) Any duplicated inputs need to be removed. Hint: Lecture 5, slide 58. 
#   3) We need the discards to be handled in reverse of their sorted order.
#      (We need this rule since step 10 will delete cards from your hand, and
#       deleting right to left allows the discards' indices to keep lined-up
#       with the hand. (See the warning about changing a list while looping
#       over it, in Lecture 4, slide 42. Technically, we're currently looping
#       over the discards, not the hand -- but the warning of that slide is
#       still relevant to this requirement.)
    for ch in sorted(list(set(todiscard)), reverse = True):

#       10.
#       This deletes cards from the hand. Same as pokerBasic.py.
        if ch.isalpha() and ch.lower() in [chr(ord('a') + i) for i in range(5)]:
            del phand[ord(ch.lower()) - ord('a')]

#   11.
#   This ends the loop early if no cards discarded. Same as pokerBasic.py.
    if len(todiscard) == 0:
        break

#   12.
#   This next part fills the hand back up to 5 cards, but has a new rule.
#   REQUIREMENT: you must do this all on one line, and without using a ";".
    tmp = deck[:5 - len(phand)]
    del deck[:5 - len(phand)]
    phand.extend(tmp)
    
# 13.
# This part prints the final state of your hand. It prints "In the end, you
# have:", and then it prints the cards. There are new rules...
# REQUIREMENTS:
# 1) This final printing of the hand should only print if step 11 did not end
#    early (since users would've already seen the final hand, in that case).
#    Hint: See Lecture 4, slide 36.
# 2) The printing of the cards should be done by copy-pasting the code from
#    above steps 6 & 7 (but remove the printing of the a-e letters & the ".")
# 3) Also, add the printing of an empty line when done (same as pokerBasic).
else:
    print("In the end, you have: ", end = '')
    for [n, val] in enumerate(phand):
        print(chr(ord('a')+n) + '.', *val, end = '  ')


    
# 14. Print an empty line (same as pokerBasic): 
print()

# 15.
# Create two tuples for the faces and suits. But there are new rules...
# REQUIREMENT: you must do this all on one line, and without using a ";".
#              Hint: Lecture 4, slides 46 & 73.
F, S = zip(*phand)

# 16.
# Create a boolean of if all cards are the same suit (same as pokerBasic): 
flush = all(x == S[0] for x in S)

# 17.
# This part creates a list of 5 numbers that count how many other cards have
# the same value as the card at each position (same as pokerBasic): 
counts = [F.count(x) for x in F]

# 18.
# Uses the list of 5 numbers to check for 4 of a kind (same as pokerBasic):
if 4 in counts: print("Four of a kind!")

# 19.
# Uses the list of 5 numbers to check for a full house (same as pokerBasic):
elif 3 in counts and 2 in counts: print("Full House!")

# 20.
# Uses the list of 5 numbers to check for 3 of a kind (same as pokerBasic):
elif 3 in counts: print("3 of a kind!")

# 21.
# Uses the list of 5 numbers to check for 2 pair (same as pokerBasic):
elif counts.count(2) == 4: print("2 pair!")

# 22.
# Uses the list of 5 numbers to check for 1 pair (same as pokerBasic):
elif counts.count(2) == 2: print("1 pair.")

# 23. Type this line, as-is (steps 23-30 are all new to this better version):
else:

#   So now we know there are no repeats. Flushes and straights are possible
#   only in such non-repeating cases. But it is also possible that the hand
#   is neither a flush nor a straight, in which case the hand is scored just
#   by its highest card.
 
#   24.
#   To identify straights, we would like to sort the cards. But there is a
#   problem because some of the cards are strings, while others are numbers.
#   So the strings need to be converted as follows: 'J'=>11, 'Q'=>12, 'K'=13,
#   'A'=>14. 
#   But there is a second problem, because step 15 created a tuple for the
#   faces, and tuples are immutable.
#   Anyway, insert into the space below the code that fixes these problems
#   (remember, I allow you as many statements as need to implement a "..."):
    listF = list(F)
    mapp = {'J':11, 'Q':12, 'K':13, 'A':14}
    for key in mapp:
        while key in listF:
            listF[listF.index(key)] = mapp[key]
    F = listF

#   25.
#   Now that the faces are all numbers in a mutable list, they can be sorted.
#   This sounds like a good thing to do, as it'll make it easier to identify
#   straight sequences. So let's sort it:
    F.sort()
    

#   26.
#   This part checks for royal straights.
#   Note that step 23 has ensured that all of the cards here are different.
#   Note that step 25 has ensured that the cards are all sorted.
#   Note that royal straights have a 10 as the LOWEST card.
    if F[0] == 10 and F[4] == 14:

#       27.
#       This part either prints "Royal straight flush!" or "Royal straight!":
        if flush:
            print("Royal straight flush!")
        else:
            print("Royal straight!")

#   28.
#   This checks for straights (not royal ones, since step 26 handled those).
#   But note that the ACE, if used in a non-royal straight, can only function
#   as the "1", in a 1-5 sequence (and yet its value is stuck at 14, not 1).
    elif (F[0] == 2 and F[3] == 5 and F[4] == 14) or any(F[0] == x and F[4] == x + 4 for x in range(2,9)):

#       29.
#       This part either prints "Straight flush!" or "Straight!":
        if flush:
            print("Straight flush!")
        else:
            print("Straight!")

#   30. Fill in the blanks below:
    elif flush: print("Flush!")
    elif 14 in F: print("Ace high.")
    elif 13 in F: print("King high.")
    elif 12 in F: print("Queen high.")
    elif 11 in F: print("Jack high.")
    else: print(F[4],"high.")
print()
