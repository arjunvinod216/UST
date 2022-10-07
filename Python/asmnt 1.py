# 1

def days():
    num = int(input("Enter the Number : "))
    years = num//365
    months = (num-years*365)//30
    days = (num-years*365-months*30)
    print(years," Year ",months," Months ",days," Days ")
days()


# 2

def fib():
    a=1
    b=1
    while (a<20):
        print (a)
        c=a+b
        a=b
        b=c
print("Fibonacci Series") 
fib()


# 3

player1 = input("Enter Player name 1 :")
player2 = input("Enter Player name 2 :")
s=[]
for i in range(2):
    choice = input("Enter the choice ('R'  for Rock | 'S' for Scissor | 'P' for Paper)  : ")
    s.append(choice.upper())
if (s[0]=='R' and s[1]=='S'):
    print(player1,s[0]," wins ")
elif (s[0]=='P' and s[1]=='R'):
    print(player1,s[0]," wins ")
elif (s[0]=='S' and s[1]=='P'):
    print(player1,s[0]," wins ")
elif (s[0]=='S' and s[1]=='R'):
    print(player2,s[1]," wins ")
elif (s[0]=='R' and s[1]=='P'):
    print(player2,s[1]," wins ")
elif (s[0]=='P' and s[1]=='S'):
    print(player2,s[1]," wins ")
elif ((s[0]=='P' and s[1]=='P') or (s[0]=='S' and s[1]=='S') or (s[0]=='R' and s[1]=='R')):
    print("Tie")
else :
    print("Invalid")


# 4

def allowance():
    total=(22/100)*amount+(18/100)*amount+(10/100)*amount
    return total

def deduction():
    if amount>8000:
        profitax = 200
    else:
        profitax = 150
    sumtotal=profitax+(12/100)*amount+(8/100)*amount
    return sumtotal

def gross(allo):
    return amount+allo
    
def netsalary(gro):
    d=deduction()
    return gro-d

amount = int(input("Enter the Basic Salary : "))
print(" Allowances : " ,allowance())
print(" Deduction : " ,deduction())
a=allowance()
b=deduction()
print(" GrossSalary : ",gross(a))
c=gross(a)
print(" NetSalary : ",netsalary(c))


# 5

str2 = "Python is a widely used general-purpose, high level programming language. \nIt was created by Guido van Rossum in 1991 and further developed by the Python Software Foundation.\n It was designed with an emphasis on code readability,\n and its syntax allows programmers to express their concepts in fewer lines of code"
str1=str2.upper()
c1=0
c2=0
for i in range(len(str1)):
    if((str1[i]=='A') or (str1[i]=='E') or (str1[i]=='I') or (str1[i]=='O') or (str1[i]=='U')):
        c1=c1+1
    elif(str1[i].isalpha()):
        c2=c2+1
print("No of vowels : ",c1)
print("No of constraints : ",c2)


# 6

str1 = input("Enter the string : ")
str2 = str1.upper()
str3 = str2[::-1]
for i in range(len(str2)):
    if str2 != str3:
        print("Not Pallindrome ")
        break
    else:
        print("Pallindrome ")
        break


# 7

str1 = input("Enter the Email ID : ")
if (str1[0]!='@' and str1[0]!='.') and (str1[:1]!='@' and str1[:1]!='.') and (str1.count('@')==1) and (str1.count('.')==1):
    print(str1,"is Valid ")
else:
    print(str1,"is InValid ")


# 8

def hotel_cost(night):
    return 140*night

def plane_ride_cost(city):
    if city == 'charlotte':
        return 183
    elif city == 'tampa':
        return 220
    elif city == 'pittsburgh':
        return 222
    elif city == 'los angeles':
        return 475
    else:
        print("Invalid ")

def rental_car_cost(days):
    if days >= 7:
        car_cost = (40*days)-50
    elif days >= 3:
        car_cost = (40*days)-20
    else:
        car_cost = 40*days
    return car_cost

def trip_cost(city,days,spending_money):
    cost= int(rental_car_cost(days)+ plane_ride_cost(city) + hotel_cost(days)+spending_money)
    print ("Total Cost : ",cost)

c = input("Enter the city (charlotte,tampa,pittsburgh,los Angeles) : ")
city = c.lower()
days = int(input("Enter the no. of days : "))
spending_money = int(input("Enter the amount : "))
trip_cost(city,days,spending_money)


# 9

def viewBakery():
    for i in bakery_items:
        print(i,'-','Rs',bakery_items[i])
        
def addItem():
    i=input("""Enter the item:
               Bread
               Butter
               Jam
               Cheese
               Crossiant
               :""")
    item = i.lower()
    if(item not in bakery_items):
        print("Invalid item")
    elif item not in cart:
        cart[item]=1
        
def view_cart():
    for i in cart:
        print(i,'-','Qt',cart[i])

def updateItem():
    i=input("""Enter the item:
               Bread
               Butter
               Jam
               Cheese
               Crossiant
               :""")
    item = i.lower()
    if(item in cart):
        quantity=int(input("Enter Quantity:"))
        cart[item]=quantity
    else:
        print("Invalid Item")
    
    
def removeItem():
    i=input("""Enter the item:
               Bread
               Butter
               Jam
               Cheese
               Crossiant
               :""")
    item = i.lower()
    if(item in cart):
        del cart[item]
    else:
        print("Invalid Item")
    

def checkOut():
    print("Bill info : ")
    print("item \t","cost")
    cost=0
    for item in cart:
          print(item,"\t",cart[item]*bakery_items[item])
          cost=cost+cart[item]*bakery_items[item]
    print("Total cost:",cost)

bakery_items = {"bread":40, "butter":120, "jam":200, "cheese":220, "crossiant":60}
cart={}   
flag=True
while(flag==True):
    choice=int(input("""Enter the choice
                       1. View the bakery items
                       2. Add the item into the cart
                       3. View the cart
                       4. Update item in the cart
                       5. Remove item from the cart
                       6. Checkout and generate bill
                       : """))
    if(choice==1):
        viewBakery()
        print()
    elif(choice==2):
        addItem()
        print()
    elif(choice==3):
        view_cart()
        print()
    elif(choice==4):
        updateItem()
        print()
    elif(choice==5):
        removeItem()
        print()
    elif(choice==6):
        checkOut()
        print()
        flag=False

