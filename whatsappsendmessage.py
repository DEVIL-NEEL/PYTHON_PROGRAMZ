import pywhatkit 
t=int(input("ENTER THE NUMBER OF MESSAGES U WANNA SEND? "))
for i in range(t):
    s=input("ENTER UR TEXT: ")
    x=input("ENTER UR NUMBER: ")
    pywhatkit.sendwhatmsg_instantly(x,s)
print("SUCCESS!!!!")