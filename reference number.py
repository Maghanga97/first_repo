import datetime

x = datetime.datetime.now()
attachment= "REF"
userid = input("Enter username:")
print("Username is: " + userid)
int_user= int(userid)
#d=7
n= 1
while n < int_user:
  b= str(n) 
  print(attachment+"/"+x.strftime("%G")+"/"+b)
  n +=1

