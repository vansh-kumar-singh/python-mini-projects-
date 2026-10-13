import random
print('\t\tpassword generator')
a=int(input("enter the legnth of password"))
b=input("should your password contains one special character?(yes/no)")
c=input('does your password contain any number?(yes/no) ')
sp="~!@#$%^&*?"
passw=''
d=random.randrange(a)
for i in range(a):
	if b=="yes" and c=="yes":
		if i==d:
			passw=passw+str(random.randint(0,9))
		elif i==d+1:
			passw=passw+sp[random.randrange(len(sp))]
		else:
			passw=passw+chr(random.randrange(65,91))
	elif b=="yes" and c=="no":
		if i==d:
			passw=passw+sp[random.randrange(len(sp))]
		else:
			passw=passw+chr(random.randrange(65,91))
	elif c=="yes" and b=="no":
		if i==d:
			passw=passw+str(random.randrange(10))
		else:
			passw=passw+chr(random.randrange(65,91))
	else:
		passw=passw+chr(random.randrange(65,91))
print("your password is",passw)