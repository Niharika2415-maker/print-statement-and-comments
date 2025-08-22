start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
squares = []
even_squares = []
odd_squares = []
for num in range(start, end + 1):
    sq = num ** 2
    squares.append(sq)
    if sq % 2 == 0:
        even_squares.append(sq)
    else:
        odd_squares.append(sq)
print(f"\nSquares of numbers from {start} to {end}: {squares}")
print(f"Even squares: {even_squares}")
print(f"Odd squares: {odd_squares}")
