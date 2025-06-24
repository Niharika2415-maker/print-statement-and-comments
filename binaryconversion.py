num = float(input("Enter a decimal number: "))
binary = ""
while num > 0:
    r = num % 2
    num //= 2
    for i in range(2):
        if i == r:
            binary = str(i) + binary
if binary == "":
    binary = "0"
print("Binary:", binary)
