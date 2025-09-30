import random
def guess_the_number():
    number= random.randint(1,20)
    attempts=0
    print("welcome to the guess the number game!!")
    print("i have choosen a number between 1-20.can u guess it??")
    while True:
        try:
            guess= int(input("enter ur guess"))
            attempts+=1
            if guess<number:
                print("too low!try again")
            elif guess>number:
                print("too high!try again")
            else:
                print(f"congratulations!! u guessed it in {attempts} attempts")
                break
        except ValueError:
            print("pls enter a valid number")
if __name__=="__main__":
    guess_the_number()
