import random 

number = random.randint(1,9)
#print(number)
while True:
    num = input("enter number between 1 to 9")
    num = int(num)
    print(num)

    if(num<number):
        print("the number is to small enter number agian")
    
    elif(num>number):
        print("number is to big enter number agian") 


    else:
        print("conguralition you guessed the number") 
        break

