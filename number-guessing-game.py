import random 
print("number guessing game")
print ('rules: \n i will pick up a number between 1 and 100 and you have to guess it and the number guesses you take decides your score')
a=random.randint(1,100)
score=1
while True:
	b=int(input('enter your guess'))
	if b==a:
		print(' bingo you took',score,'guesses')
		break
	elif b>a:
		print('your guess is higher')
		score+=1
	else:
		print('your guess is lower')
		score+=1