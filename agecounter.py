def check_age():
    while True:
        try:
            age_input = input("Please enter your age: ")
            age = int(age_input)  
            if age % 2 == 0:
                print(f"Your age ({age}) is an even number.")
            else:
                print(f"Your age ({age}) is an odd number.")
            break 
        except ValueError:
            print("Value Error: Please enter a valid integer for your age (e.g., 25).")
check_age()