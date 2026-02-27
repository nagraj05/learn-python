numbers = input("Enter numbers")
split_numbers = numbers.split(",")
convertToNum = list(map(int, split_numbers))
print(max(convertToNum))

