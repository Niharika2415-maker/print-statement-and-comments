import random
playing= True
number= str(random.randint(10,20))
print("i will generate a number from 0 to 9")
print("the game ends when u get 1")
while playing:
    guess= input("give me ur best guess")
    if number==guess:
        print("u won the game")
        print("the number was",number)
        break
    else:
        print("try again")
        