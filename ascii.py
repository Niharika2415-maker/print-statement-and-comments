character= input("enter a letter")
if len(character)==1:
    if ord(character)<128:
        print(f"enter ascii value of'(charater)' is {ord(character)}")
else:
    print("character is not in ascii range")
