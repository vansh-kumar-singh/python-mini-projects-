import random
import time
print('\t\trock paper scissors game')
a=input('do you want to play(y/n)')
c=['rock','paper','scissors']
score1=0
score2=0
while True:
	d=random.randint(1,len(c))
	if a.lower()=='y':
		b=int(input("enter your choice\n1.rock\n2.paper\n3.scissors\n"))
		if b>3:
			print("enter valid choice(1-3)")
			continue
		elif b==1:
			print('3')
			time.sleep(0.5)
			print('2')
			time.sleep(0.5)
			print('1')
			time.sleep(0.5)
			print("you chose:",c[b-1])
			print("computer chose:",c[d-1])
			if d==1:
				print('tied')
			elif d==2:
				print('computer won')
				score2+=1
			else:
				print('you won')
				score1+=1
		elif b==2:
			print('3')
			time.sleep(0.5)
			print('2')
			time.sleep(0.5)
			print('1')
			time.sleep(0.5)
			print("you chose:",c[b-1])
			print("computer chose:",c[d-1])	
			if d==1:
				print('you won')
				score1+=1
			elif d==2:
				print('tied')
			else:
				print('computer won')
				score2+=1
		else:
			print('3')
			time.sleep(0.5)
			print('2')
			time.sleep(0.5)
			print('1')
			time.sleep(0.5)
			print("you chose:",c[b-1])
			print("computer chose:",c[d-1])
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