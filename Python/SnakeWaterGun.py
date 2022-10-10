player1 = input("Enter Player name 1 :")
player2 = input("Enter Player name 2 :")
s=[]
for i in range(2):
    choice = input("Enter the choice ('S'  for Snake | 'W' for Water | 'G' for Gun)  :  ")
    s.append(choice.upper())
if (s[0]=='S' and s[1]=='W'):
    print(player1,s[0]," wins ")
elif (s[0]=='G' and s[1]=='S'):
    print(player1,s[0]," wins ")
elif (s[0]=='W' and s[1]=='G'):
    print(player1,s[0]," wins ")
elif (s[0]=='W' and s[1]=='S'):
    print(player2,s[1]," wins ")
elif (s[0]=='S' and s[1]=='G'):
    print(player2,s[1]," wins ")
elif (s[0]=='G' and s[1]=='W'):
    print(player2,s[1]," wins ")
elif ((s[0]=='S' and s[1]=='S') or (s[0]=='W' and s[1]=='W') or (s[0]=='G' and s[1]=='G')):
    print("Tie")
else :
    print("Invalid")
