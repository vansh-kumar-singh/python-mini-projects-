import random
import time
print("\t\tdice roller")
ch=input("do you want to roll the dice(y/n)")
c=0
while True:
	if ch=="n":
		break
	c+=1
	a=random.randint(1,6)
	print("rolling dice in..")
	time.sleep(0.75)
	print("3")
	time.sleep(0.75)
	print("2")
	time.sleep(0.75)
	print('1',end='\n\n')
	for i in range(a):
		if a==4  or a==6:
			if i%2==0:
				print("*",end='\t')
			else:
				print('*',end='\n')
		elif a==5:
			if i==2:
				print('    *',end='\n')
			elif i==0 or i==3:
				print('*',end='\t')
			elif i==1 or i==4:
				print("*",end="\n")
		else:
			print("\t"*i,"*")
	print("\nyou got a",a)
	ch=input("do you want to roll again(y/n)")
if c>0:
	print("\nthanks for rolling")
else:
	print("\ntry rolling soon")