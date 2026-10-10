import csv
while True:
    print("\t\t expense tracker")
    print("1. add expense")
    print("2. show total")
    print("3. exit")
    choice=int(input("enter your choice"))
    if choice==1:
        f=open("name.csv",'a',newline='\n')
        wob=csv.writer(f)
        name=input("enter your name:")
        amount=float(input("Enter the amount"))
        note=input("Enter the use of amount")
        expenses={'amount':amount,'note':note}
        data=[name,amount,note]
        wob.writerow(data)
        print("amount added")
        f.close()
    elif choice==2:
        f=open("name.csv",'r')
        sum1=0
        rob=csv.reader(f)
        b=input("Enter your name")
        a=0
        for j in rob:
            if j[0]==b:
                if a==0:
                    print("the expenses are")
                print(j[1],'------->',j[2])
                sum1+=float(j[1])
                a+=1
        if a==0:
            print("data not found")
        else:
            print("total expense:",sum1)
    else:
        print("exitting .....")
        break
            

