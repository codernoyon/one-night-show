text = "I am learning Python. Becoming Python Pro"
count = 0
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for char in text:
    if char in vowels:
        count = count + 1
print("Your number of vowels is", count)