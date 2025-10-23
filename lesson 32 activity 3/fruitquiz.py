import random
class quiz:
    def __init__(self):
        self.fruits= {'apple':'red','orange':'orange','watermelon':'green','banana':'yellow'}
    def fruitquiz(self):
        while(True):
            fruit,colour= random.choice(list(self.fruits.items()))
            print("what is the colour of {}".format(fruit))
            user_answer= input()
            if (user_answer.lower()==colour):
                print("correct answer")
            else:
                print("wrong answer")
            option= int(input("enter 0,if u want to play a game else enter 1"))
            if (option):
                break
print("welcome to fruit quiz")
fq= quiz()
fq.fruitquiz()
