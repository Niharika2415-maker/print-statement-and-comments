number = input("Enter a number: ")
if number.startswith('-'):
    number = number[1:]
count = 0
index = 0
while index < len(number):
    if number[index].isdigit():
        count += 1
    index += 1
print("Number of digits:", count)
