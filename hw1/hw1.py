deck=[(f,s) for (f,s) in zip([*range(2,11),'J', 'Q', 'K', 'A'] * 4,[chr(ord('♣')),chr(ord('♠')),chr(ord('♦')),chr(ord('♥'))] * 13)]

import random
random.shuffle(deck)

phand = deck[:5]
del deck[:5]

for Round in range(3):
	print("You Have:",end=" ")

	for [n, val] in enumerate(phand):
		print(chr(ord('a')+n) + '.', *val, end = '  ')	        
    	
	todiscard = input("\nEnter the letters (a-e) all of the cards you want to discard:").strip()
	
	for ch in sorted(list(set(todiscard)), reverse = True):
		if ch.isalpha() and ch.lower() in [chr(ord('a') + i) for i in range(5)]:
			del phand[ord(ch.lower()) - ord('a')]

	if len(todiscard) == 0:
	    break

	tmp = deck[:5 - len(phand)]
	del deck[:5 - len(phand)]
	phand.extend(tmp)
	        
else:
	print("In the end, you have: ", end = '')
	for [n, val] in enumerate(phand):
		print(chr(ord('a')+n) + '.', *val, end = '  ')
   
print()

F, S = zip(*phand)

flush = all(x == S[0] for x in S)

counts = [F.count(x) for x in F]

if 4 in counts: print("Four of a kind!")

elif 3 in counts and 2 in counts: print("Full House!")

elif 3 in counts: print("3 of a kind!")

elif counts.count(2) == 4: print("2 pair!")

elif counts.count(2) == 2: print("1 pair.")

else:
	listF = list(F)
	mapp = {'J':11, 'Q':12, 'K':13, 'A':14}
	for key in mapp:
		while key in listF:
			listF[listF.index(key)] = mapp[key]
	F = listF
	F.sort()

	if F[0] == 10 and F[4] == 14:
		if flush:
			print("Royal straight flush!")
		else:
			print("Royal straight!")

	elif (F[0] == 2 and F[3] == 5 and F[4] == 14) or any(F[0] == x and F[4] == x + 4 for x in range(2,9)):
		if flush:
			print("Straight flush!")
		else:
			print("Straight!")

	elif flush: print("Flush!")
	elif 14 in F: print("Ace high.")
	elif 13 in F: print("King high.")
	elif 12 in F: print("Queen high.")
	elif 11 in F: print("Jack high.")
	else: print(F[4],"high.")
print()

