t=int(input("ENTER NO OF TEST CASES: ")) #no of test cases
for i in range(t):
    
    while(True): #menu driven while loop
        print("ENTER 1 TO ADD")
        print("ENTER 2 TO SUB")
        print("ENTER 3 TO MULTIPLY")
        print("ENTER 4 TO DIV")
        print("ENTER 5 TO MOD")
        print("ENTER 6 TO FLOOR DIV")
        print("ENTER 7 TO XOR")
        print("ENTER 0 TO EXIT")
        n=int(input("ENTER UR OPTION: ")) #different operations based on user's input
        if n==1:
            m=int(input("ENTER THE NO OF NUMBERS U WANNA ADD:"))
            s=0
            for i in range(m):
                a=int(input("ENTER NO: "))
                s+=a 
            print("ANS =",s)
            print()
        elif n==2:
            
            m=int(input("ENTER THE NO OF NUMBERS U WANNA SUB:"))
            s=0
            for i in range(m):
                a=int(input("ENTER NO: "))
                if i==0:
                    s=a 
                else:
                    s-=a 
            print("ANS =",s)
            print()
        elif n==3:
            
            m=int(input("ENTER THE NO OF NUMBERS U WANNA MULTIPLY:"))
            s=1
            for i in range(m):
                a=int(input("ENTER NO: "))
                s*=a 
            print("ANS =",s)
            print()
        elif n==4:
            m=int(input("ENTER THE NO OF NUMBERS U WANNA DIV:"))
            s=0
            for i in range(m):
                a=int(input("ENTER NO: "))
                if i==0:
                    s=a
                else:
                    if a==0:
                        a=int(input("DIV BY 0 NOT POSSIBLE ENTER A DIFFERENT NUMBER: "))
                    s/=a 
            print("ANS =",s)
            print()
        elif n==5:
            
            m=int(input("ENTER THE NO OF NUMBERS U WANNA MOD:"))
            s=0
            for i in range(m):
                a=int(input("ENTER NO: "))
                if i==0:
                    s=a 
                else:
                    if a==0:
                        a=int(input("MOD BY 0 NOT POSSIBLE ENTER A DIFFERENT NUMBER: "))

                    s%=a  
            print("ANS =",s)
            print()
        elif n==6:
            
            m=int(input("ENTER THE NO OF NUMBERS U WANNA FLOOR DIV:"))
            s=0
            for i in range(m):
                a=int(input("ENTER NO: "))
                if i==0:
                    s=a 
                else:
                    if a==0:
                        a=int(input("FLOOR DIV BY 0 NOT POSSIBLE ENTER A DIFFERENT NUMBER: "))
                    
                    s//=a 
            print("ANS =",s)
            print()
        elif n==7:
            
            m=int(input("ENTER THE NO OF NUMBERS U WANNA XOR:"))
            s=0
            for i in range(m):
                a=int(input("ENTER NO: "))
                if i==0:
                    s=a 
                else:
                    s^=a 
            print("ANS =",s)
            print()
        elif n==0:
            break
        else:
            print("INVALID NUMBER") #for any input other than specified