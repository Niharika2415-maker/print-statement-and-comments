num = int(input("Enter a number: "))
odd_numbers = [i for i in range(1, num) if i % 2 != 0]
even_numbers = [i for i in range(1, num) if i % 2 == 0]
print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)

fruits = ["apple", "banana", "cherry", "date"]
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print("Updated fruits:", capitalized_fruits)
