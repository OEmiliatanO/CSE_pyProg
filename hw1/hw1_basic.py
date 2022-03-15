deck= [(2,'♠'),(3,'♣'),(4,'♥'),(5,'♦'),(6,'♠'),(7,'♣'),(8,'♥'),(9,'♦'),(10,'♠'),('J','♣'),('Q','♥'),('K','♦'),('A','♠'),(2,'♣'),(3,'♥'),(4,'♦'),(5,'♠'),(6,'♣'),(7,'♥'),(8,'♦'),(9,'♠'),(10,'♣'),('J','♥'),('Q','♦'),('K','♠'),('A','♣'),(2,'♥'),(3,'♦'),(4,'♠'),(5,'♣'),(6,'♥'),(7,'♦'),(8,'♠'),(9,'♣'),(10,'♥'),('J','♦'),('Q','♠'),('K','♣'),('A','♥'),(2,'♦'),(3,'♠'),(4,'♣'),(5,'♥'),(6,'♦'),(7,'♠'),(8,'♣'),(9,'♥'),(10,'♦'),('J','♠'),('Q','♣'),('K','♥'),('A','♦')]

import random
random.shuffle(deck)

phand = deck[:5]
del deck[:5]

for Round in range(3):
	print("You Have:",end=" ")
	for [n, val] in enumerate(phand):
		print(chr(ord('a')+n) + '.' + str(val[0]) + str(val[1]), end = ' ')

	todiscard = input("\nEnter the letters (a-e) all of the cards you want to discard: ").strip()

	for ch in sorted(list(todiscard), reverse = True):
		if ch.isalpha() and ch.lower() in [chr(ord('a') + i) for i in range(5)]:
			del phand[ord(ch.lower()) - ord('a')]
	if len(todiscard) == 0:
		break

	tmp = deck[:5 - len(phand)]
	del deck[:5 - len(phand)]
	phand.extend(tmp)

print("In the end, you have: ", end = '')
for [n, val] in enumerate(phand):
	print(chr(ord('a')+n) + '.' + str(val[0]) + str(val[1]), end = ' ')
	        
print()

F = tuple([f[0] for f in phand])
S = tuple([s[1] for s in phand])

flush = all(x == S[0] for x in S)

counts = [F.count(x) for x in F]

if 4 in counts: print("Four of a kind!")

elif 3 in counts and 2 in counts: print("Full House!")

elif 3 in counts: print("3 of a kind!")

elif counts.count(2) == 4: print("2 pair!")

elif counts.count(2) == 2: print("1 pair.")


