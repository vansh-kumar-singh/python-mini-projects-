import random
import time
print('\t\trock paper scissors game')
a=input('do you want to play(y/n)')
c=['rock','paper','scissors']
score1=0
score2=0
while True:
	d=random.randint(1,len(c))
	if a=='y':
		b=int(input("enter your choice\n1.rock\n2.paper\n3.scissors\n"))
		print('3')
		time.sleep(1)
		print('2')
		time.sleep(1)
		print('1')
		if b==1:
			if d==1:
				print('tied')
			elif d==2:
				print('computer won')
				score2+=1
			else:
				print('you won')
				score1+=1
		elif b==2:
			if d==1:
				print('you won')
				score1+=1
			elif d==2:
				print('tied')
			else:
				print('computer won')
				score2+=1
		else:
			if d==1:
				print('computer won')
				score2+=1
			elif d==2:
				print('you won')
				score1+=1
			else:
				print('tied')
		a=input("do you want to play again(y/n)")
	else:
		break
print("the score is\ncomputer",score2,"you",score1)