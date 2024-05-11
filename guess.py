import random
number = random.randint(1, 10)


print("-----------Welcome to the game--------\n")
# option for start the game
class guessnum:
     
     def game2(self): 
        
        computer = 1     
        name = input("Enter your name = ")
        print("")
       
        print("")
# logic for the game
        
        while True:
            usernum = int(input("enter the number in 1 to 10 : "))
            if usernum > 10:
                print("enter the number in the given range")
                print("try it again")
                continue

            if usernum > number:
                print("your guess is above the number, try again\n")
                computer+=1
            elif usernum == number:
                print("you got it right\n")
                break
            else:
                print("your guess is below the number, try again\n")
                computer+=1
                
                
        print("************Your result*************\n")
        
        
        
        if computer>=5:
            print("better luck next time",name,"your guess is",computer,"\n\n")
        else:
            print("Nice",name," you got in",computer,"guesses\n\n")
        
        
        
        
        
        
        
        
        
while True:
 print("1) play the game  press 1 ")
 print("2) About the game press 2")
 print("3) exit the game press 3\n")
 option = int(input("enter  the number : "))
 if option > 3:
    print("enter the number from 1 to 3")
 elif option == 2:
    print("This is the game about guessing the number with the computer, play it and enjoy!\n")
    continue
 elif option == 1:
     print("Lets play the game \n")
     game1=guessnum()
     game1.game2()    
 else:
    print("Have a nice day, bye bye! ")
    break