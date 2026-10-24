ch = input("Enter a character: ")

vowels = ["a", "e", "i", "o", "u"]

if ch.lower() in vowels:
    print(ch, "is a vowel")
else:
    print(ch, "is not a vowel")
