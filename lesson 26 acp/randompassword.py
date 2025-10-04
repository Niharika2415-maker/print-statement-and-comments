import random 
print("welcome to password generator")
characters= "abcdefghijklmnopqrstuvwxyz"
password_length=int(input("what length would you like ur password to be: "))
for i in range(password_length):
   password.append(random.choice(characters))
   password="".join(password)
   pass
print("your password is:" + password)
