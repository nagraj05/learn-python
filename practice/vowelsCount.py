name = input("Enter a text: ")

def countVowels(name):
    vowels = ["a","e","i","o","u"]
    count = 0

    for word in name.lower():
        if word in vowels:
            count +=1
    return count
print(countVowels(name))
