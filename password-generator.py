import random
print('\t\tpassword generator')
a=int(input("enter the legnth of password"))
b=input("should your password contains one special character?(yes/no)")
c=input('does your password contain any number?(yes/no) ')
passw=''
for i in range(a):
	d=random.randint(1,a-1)
	sp='~`!@#$%&*?'
	if b=='yes' and c=='yes':
		if d==random.randrange(0,a):
			passw=passw+sp[random.randrange(0,len(sp))]
		elif i==a-2:
			for j in sp:
				if j in passw:
					break
				elif j=='?':
					passw=passw+sp[random.randrange(0,len(sp))]
			for k in range(10):
					if str(k) in passw:
						break
					elif k==9:
						passw=passw+str(random.randint(0,9))
		elif d==random.randrange(0,a):
			passw=passw+str(random.randrange(0,10))		
		elif len(passw)!=a:
			e=random.randrange(65,90)
			passw=passw+chr(e)
	elif b=='yes' and c=='no':
		if d==random.randrange(0,a):
			passw=passw+sp[random.randrange(len(sp))]
		elif i==a-1:
			for j in range(len(sp)):
				if sp[j] in passw:
					break
				elif j==len(sp)-1:
					passw=passw+sp[random.randrange(0,len(sp))]
		elif len(passw)!=a:
			e=random.randrange(65,90)
			passw=passw+chr(e)
	elif c=='yes' and b=='no':
		if d==random.randrange(0,a):
			passw=passw+str(random.randrange(0,10))
		elif i==a-1:
			for j in range(10):
				if str(j) in passw:
					break
				elif j==9:
					passw=passw+str(random.randint(0,9))
		elif len(passw)!=a:
			e=random.randrange(65,90)
			passw=passw+chr(e)
	elif c=='no' and b=="no":
		e=random.randrange(65,90)
		passw=passw+chr(e)	
print('your password is',passw)