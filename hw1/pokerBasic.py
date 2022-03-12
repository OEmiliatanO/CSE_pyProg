# This file is a simplified version of the homework, which you should get
# working, before moving on to the more complex version described in the
# poker.py file. If you can succeed in getting this simplified version to
# work correctly, you'll get at least 60% of the points for this programming
# assignment. But if you can't get this simplified version to work, you'll
# get 0% (that is why you should do this simplified version first, to ensure
# that you will get at least the minimum points).

# The code below contains 22 numbered steps. In each step, you must follow
# the instructions for that part.
# In some cases, the step requires you to fill in a blank (____). In these
# cases, the text you add cannot include a ";" symbol because you are just
# supposed to complete the partially-provided Python statement. 
# In other cases the step requires that a (...) be replaced. In these cases,
# you may use multiple statements (on multiple lines and/or separated by ';')

# Below is the template for you to replace parts in:


# 1.
# In this basic version of the assignment, I'm giving you the following, so
# leave it as it is:
deck= [(2,'♠'),(3,'♣'),(4,'♥'),(5,'♦'),(6,'♠'),(7,'♣'),(8,'♥'),(9,'♦'),(10,'♠'),('J','♣'),('Q','♥'),('K','♦'),('A','♠'),(2,'♣'),(3,'♥'),(4,'♦'),(5,'♠'),(6,'♣'),(7,'♥'),(8,'♦'),(9,'♠'),(10,'♣'),('J','♥'),('Q','♦'),('K','♠'),('A','♣'),(2,'♥'),(3,'♦'),(4,'♠'),(5,'♣'),(6,'♥'),(7,'♦'),(8,'♠'),(9,'♣'),(10,'♥'),('J','♦'),('Q','♠'),('K','♣'),('A','♥'),(2,'♦'),(3,'♠'),(4,'♣'),(5,'♥'),(6,'♦'),(7,'♠'),(8,'♣'),(9,'♥'),(10,'♦'),('J','♠'),('Q','♣'),('K','♥'),('A','♦')]

# 2.
# Next, shuffle the deck. Hint: look at the methods available in the "random"
# module that comes standard with Python.
import random
random.shuffle(deck)

# 3.
# Next, take 5 cards from the deck and put them in a new list which is the
# player's hand. If you do this correctly, the deck will now have 47 cards.
phand = deck[:5]
del deck[:5]

# 4.
# The next line is the header of a loop that runs 3 times.
for Round in range(3):
#   5.
#   Now you are in the loop body. For the body's first line, simply type:
    print("You Have:",end=" ")

#   6.
#   The next line must use enumerate to loop over the cards in your hand (see
#   lecture 4, slide #34):
    for [n, val] in enumerate(phand):

#       7.
#       Fill in the blank below to complete the printing of one card.
#       Whereas the better version requires the cards to be labeled with a-e,
#       This basic version does not. Rather, you only need to print the face
#       and suit of the card, followed by 2 spaces. You also need to keep the
#       print from inserting a "\n" at the end (see Lecture 2, slide 102).
        print(chr(ord('a')+n) + '.' + str(val[0]) + str(val[1]), end = ' ')

#   8.
#   This next line asks the user for input on which cards to discard.
    todiscard = input("\nEnter the letters (a-e) all of the cards you want to discard:")

#   9.    
#   This next line loops through all the characters that the user inputted.
#   Now, whereas the better version has to worry about unusual use input,
#   this version does not worry about such input.
    for ch in sorted(list(todiscard), reverse = True):

#       10.
#       As stated in step 9, this basic version does not worry about weird
#       input. The way that we avoid these worries is to only test properly
#       formatted input.
#       Q. And what is a "proper" format?
#       A. The input is only letters between a-e (ie, no commas, spaces,etc).
#          The letters will only be entered in lower case (so no "A", etc).
#          The letters will not repeat (so no "aa", etc).
#          The letters are always inputted in reverse order (so "e" is before
#              "a",etc). So the following are all OK: "eb", "ba", "dcb", etc.
#
#       Now, your job, in this step 10 is to use this input (which you know
#       will be well-formatted), to discard the cards corresponding to those
#       input letters.
#       Now further notice that we're inside of a for-loop started on step 9.
#       This means that you only need to delete one card from you hand.
#       But note: the card you are deleting does not have the value of the
#       loop index variable from step 9. For example, if the user input is
#       "dca", then the loop index variable will be "d", then "c", then "b".
#       This means that we need to delete the 4th card, then the 3rd card,
#       then the 2nd card. But none of these cards will have the values of
#       "d", "c", or "b" (instead the cards will have values like (5,'♦'),
#       ('Q','♥'), or ('J','♣')).
#       So to know which card to delete, we should recall lecture, slide 59,
#       and that the ascii code of 'a' is 97. If we think about these ideas,
#       we can find how to compute from 'a' to the zeroeth (ie the 1st), and
#       from 'e' to the foureth (ie, the 5th).
#       So insert your code to delete the correct card here:
        if ch.isalpha():
            del phand[ord(ch.lower()) - ord('a')]

#   11.
#   This next part ends the loop early if no cards were discarded.
    if len(phand) == 5:
        break

#   12.
#   This next part fills the hand back up to 5 cards, by moving some cards
#   from the deck to your hand.
    tmp = deck[:5 - len(phand)]
    del deck[:5 - len(phand)]
    phand.extend(tmp)

# 13.
# This part prints the final state of your hand. It prints "In the end, you
# have:", and then it prints the cards. The printing of the cards should be
# done by copy-pasting the code from steps 6 & 7. Then also, add code for
# printing an empty line when done with executing the copy-pasted steps 6-7.
# Note: in this basic implementation, this step 13 always executes when the
# loop from step 4 finishes (regardless of how the loop finished).
print("In the end, you have: ", end = '')
for [n, val] in enumerate(phand):
    print(chr(ord('a')+n) + '.' + str(val[0]) + str(val[1]), end = ' ')
    
# 14. Print an empty line: 
print() #This empty line is not the sane as the one that step 13 requires.

# 15.
# Create two tuples. One holds all of the face values of the 5 cards in your
# hand. The other holds the 5 suits.
F = tuple([f[0] for f in phand])
S = tuple([s[1] for s in phand])

# 16.
# The following creates a boolean that is true if all of the cards are the
# same suit:
flush= all(x == S[0] for x in S)

# 17.
# This part creates a list of 5 numbers that count how many other cards have
# the same value as the card at each of the positions in your hand. That is
# to say, if the hand held (7, 'A', 3, 'A', 7), then the list of 5 numbers
# would be [2, 2, 1, 2, 2]. Or if the hand held (8, 8, 8, 2, 8), then the
# list of 5 numbers would be [4, 4, 4, 1, 4].
# Hint: Lecture 5, slide 138.
counts = [F.count(x) for x in F]

# 18.
# This line uses the list of 5 numbers to see if there is 4 of a kind.
# Hint, Lecture 3, slide 44:
if 4 in counts: print("Four of a kind!")

# 19.
# This line checks the list of 5 numbers for a full house:
elif 3 in counts and 2 in counts: print("Full House!")

# 20.
# This line checks for 3 of a kind (given that we already know it is not a
# full house):
elif 3 in counts: print("3 of a kind!")

# 21.
# This line checks for 2 pair:
elif counts.count(2) == 4: print("2 pair!")

# 22.
# This line checks for 1 pair:
elif counts.count(2) == 2: print("1 pair.")

# This is the end of the basic version. It does not print scores for flushes,
# straights, or high-cards, because the steps 23-30 are only in the better
# version of the game. Once you verify that the above code all works, save
# your solution to a back-up file with a different name, before proceeding,
# since you don't want any later changes to break the minimum code that you
# have verified is working (because if you break your code and don't have a
# saved back-up of the basic program, then you could get a zero if you can't
# get the basic output to work anymore).

# Once you have saved this basic version, go on to read the advanced template
# in the poker.py file. You can paste-and-modify the above 22 steps into that
# template.

